import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from datetime import datetime,timedelta


def load_job_files():
    # The Job File Names
    job_file_aws = 'io(0)_aws_100_1551736728297.csv'
    job_file_gcp = 'io(0)_gcp_100_1551736760932.csv'
    job_file_azure = 'io(0)_azure_100_1551736740304.csv'
    job_df_aws = pd.read_csv(job_file_aws)
    job_df_gcp = pd.read_csv(job_file_gcp)
    job_df_azure = pd.read_csv(job_file_azure)
    return job_df_aws, job_df_azure,job_df_gcp


def preprocess_df(job_df):
    job_df['start_time'] = pd.to_datetime(job_df['start_time'],unit='ms')
    job_df['server_start_time'] = pd.to_datetime(job_df['server_start_time'], unit='ms')
    job_df['server_end_time'] = pd.to_datetime(job_df['server_end_time'], unit='ms')
    job_df['end_time'] = pd.to_datetime(job_df['end_time'], unit='ms')


def compute_queue_time(job_df):
    #Extract server start time and start time from data frame
    start_time = job_df['start_time'].values
    server_start_time = job_df['server_start_time'].values
    return (server_start_time-start_time)/int(1e6)


def compute_response_time(job_df):
    #Extract server start time and start time from data frame
    start_time = job_df['start_time'].values
    end_time = job_df['end_time'].values
    return (end_time-start_time)/int(1e6)


def bar_plot_save(avg_times,yaxlabel,title,figname):
    platforms = ('AWS', 'GCP', 'AZURE')
    y_pos = np.arange(len(platforms))
    plt.xticks(y_pos, platforms)
    plt.bar(y_pos, avg_times, align='center', alpha=0.5)
    plt.ylabel(yaxlabel)
    plt.title(title)
    plt.savefig(figname)


def save_avg_plots(oper_name,job_df_aws,job_df_gcp,job_df_azure):
    res_time_vec_aws = compute_response_time(job_df_aws)
    res_time_vec_gcp = compute_response_time(job_df_gcp)
    res_time_vec_azure = compute_response_time(job_df_azure)

    q_time_vec_aws = compute_queue_time(job_df_aws)
    q_time_vec_gcp = compute_queue_time(job_df_gcp)
    q_time_vec_azure = compute_queue_time(job_df_azure)
    platforms = ('AWS', 'GCP', 'AZURE')

    q_times = np.array([np.mean(q_time_vec_aws), np.mean(q_time_vec_gcp), np.mean(q_time_vec_azure)])
    res_times = np.array([np.mean(res_time_vec_aws), np.mean(res_time_vec_gcp), np.mean(res_time_vec_azure)])

    q_time_vec_aws = q_time_vec_aws/np.timedelta64(1, 'ms')
    q_time_vec_gcp = q_time_vec_gcp/np.timedelta64(1, 'ms')
    q_time_vec_azure = q_time_vec_azure/np.timedelta64(1, 'ms')

    res_time_vec_aws = res_time_vec_aws / np.timedelta64(1, 'ms')
    res_time_vec_gcp = res_time_vec_gcp / np.timedelta64(1, 'ms')
    res_time_vec_azure = res_time_vec_azure / np.timedelta64(1, 'ms')

    q_times_std = np.array([np.std(q_time_vec_aws), np.std(q_time_vec_gcp), np.std(q_time_vec_azure)])
    res_times_std = np.array([np.std(res_time_vec_aws), np.std(res_time_vec_gcp), np.std(res_time_vec_azure)])
    print('Results for '+oper_name+' Function:' )
    print(platforms)
    print('Queue Times(ms):')
    print(q_times)
    print('Queue Times(ms) STD:')
    print(q_times_std)

    print(platforms)
    print('Response Times(ms):')
    print(res_times)
    print('Response Times(ms) STD:')
    print(res_times_std)

    # Save q_time bar plot
    title = 'Average Queue Time(ms) for '+oper_name+' Function Across all Three Platforms'
    bar_plot_save(q_times,'Average Queue Time '+oper_name+' Function(ms)', title, 'AvgQTime'+oper_name+'.png')
    plt.clf()

    # Save r_time bar plot
    title = 'Average Response Time(ms) for ' + oper_name + ' Function Across all Three Platforms'
    bar_plot_save(res_times, 'Average Response Time ' + oper_name+' Function(ms)', title, 'AvgResTime' + oper_name + '.png')
    plt.clf()


def cold_start_batch_plot(job_df_aws1,job_df_gcp,job_df_azure):
    job_df_aws = pd.read_csv('matmul_aws_20_1551621171961.csv')
    preprocess_df(job_df_aws)
    time_origin = job_df_aws['start_time'][0]
    # Subtract each entry with this time origin
    job_df_aws['start_time'] = (job_df_aws['start_time']-time_origin)/int(1e6)
    job_df_aws['end_time'] = (job_df_aws['end_time'] - time_origin) / int(1e6)
    yval = job_df_aws['id'].values + 1
    width = job_df_aws['end_time'].values - job_df_aws['start_time'].values
    width = width/np.timedelta64(1, 'ns')
    print(width)
    start = job_df_aws['start_time'].values
    start = start/np.timedelta64(1, 'ns')
    plt.xlabel('Time Elapsed')
    plt.ylabel('Job Number')
    plt.title('4 Triggers at a time JOB Execution')
    plt.barh(y=yval.ravel(),width=width.ravel(),left=start.ravel(),height=0.3)
    plt.show()











job_df_aws, job_df_azure, job_df_gcp = load_job_files()
preprocess_df(job_df_aws)
preprocess_df(job_df_azure)
preprocess_df(job_df_gcp)
#cold_start_batch_plot(job_df_aws,job_df_gcp,job_df_azure)
save_avg_plots('IO',job_df_aws,job_df_gcp,job_df_azure)




