""""
    To execute the job. job name is the first argument in the command line.
""""
import sys 
from response import SingleResponse,Responses
from urllib import request
from config import ConfigReader
from threading import Thread
""""
    Sing thrahd
"""

def execute_single(id,config,response_list):
    response = SingleResponse(id)
    response_list.add_response(response)
    req = request.urlopen(config.end_point)
    data = req.read()
    respone.set_q_time(data)
    response.end()


def execute_job(job_name):
    config = ConfigReader.get_configuration(job_name)
    responses = Responses(job_name)
    thread_list = []

    for i in range(config.threads):
        th = Thread(target=execute_single,args=(i,config,responses))
        thread_list.append(th)
        th.start()
    //wait all

    for th in thread_list:
        th.join()

    // write the response in csv

    responses.finished()




if len(sys.argv)!=2:
    print("provide the proper commandline option")
else:
    execute_job(sys.argv[1])
    
    


