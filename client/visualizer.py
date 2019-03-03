"""
    To execute the script. The CSV Job File Name is the first argument in the command line.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime,timedelta

def load_job_file():
    #job_file_name = sys.argv[1]
    job_file_name = 'add_aws_100_1551593531154.csv'
    job_data_frame = pd.read_csv(job_file_name)
    return job_data_frame

def preprocess_df(job_df):
    job_df['start_time'] = pd.to_datetime(job_df['start_time'],unit='ms')
    job_df['server_start_time'] = pd.to_datetime(job_df['server_start_time'], unit='ms')
    job_df['server_end_time'] = pd.to_datetime(job_df['server_end_time'], unit='ms')
    job_df['end_time'] = pd.to_datetime(job_df['end_time'], unit='ms')


def compute_queue_time(job_df):
    #Extract server start time and start time from data frame
    start_time = job_df['start_time'].values
    server_start_time = job_df['server_start_time'].values
    return (server_start_time-start_time)


def compute_response_time(job_df):
    #Extract server start time and start time from data frame
    start_time = job_df['start_time'].values
    end_time = job_df['end_time'].values
    return (end_time-start_time)/int(1e6)



job_df= load_job_file()
preprocess_df(job_df)
print(compute_response_time(job_df))

plt.plot(job_df['id'].values,compute_response_time(job_df))
plt.savefig('responseVThreads.png')


