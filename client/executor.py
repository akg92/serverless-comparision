"""
    To execute the job. job name is the first argument in the command line.
"""
import sys 
from response import SingleResponse,Responses
from urllib import request
from config import ConfigReader
from threading import Thread
"""
    Sing thrahd
"""

def execute_single(id,config,response_list):
    response = SingleResponse(id)
    response_list.add_response(response)
    req = request.urlopen(config.end_point)
    data = req.read()
    response.set_q_time(data)
    response.end()


def execute_job(job_name):
    config = ConfigReader.get_configuration(job_name)
    responses = Responses(config)
    thread_list = []

    for i in range(config.threads):
        th = Thread(target=execute_single,args=(i,config,responses))
        thread_list.append(th)
        th.start()
    #wait all

    for th in thread_list:
        th.join()

    # write the response in csv

    responses.finished()


def execute_job_all_platfrom(threads):

    # number of threads.
    threads = int(threads)
    ## cmd line job options.
    ## slice from second option.
    cmd_jobs = sys.argv[2:]

    configs = ConfigReader.get_configurations(threads,cmd_jobs=cmd_jobs)

    

    ## for each item in the configuration. 
    ## for multi also configuration objects are adjusted to be the same.
    for config in configs:
        responses = Responses(config)
        thread_list = []

        for i in range(config.threads):
            th = Thread(target=execute_single,args=(i,config,responses))
            thread_list.append(th)
            th.start()
        #wait all
        for th in thread_list:
            th.join()
        # write the response in csv
        responses.finished()



if len(sys.argv)<2:
    print("provide the proper commandline option")
else:
    execute_job_all_platfrom(sys.argv[1])
    
    


