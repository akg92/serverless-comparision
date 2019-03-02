from time import gmtime
from datetime import datetime
import csv 
import json
import os 
class SingleResponse:

    def __init__(self,id,start_time=None,q_time=None,end_time=None):
        self.id = id
        if not start_time:
            self.start_time = round(datetime.timestamp(datetime.utcnow())*1000)
        else:
            self.start_time = start_time
        
        # qtime is not valid as of now.
        #self.q_time = q_time
        #
        self.end_time = end_time

    def end(self):
        self.end_time = round(datetime.timestamp(datetime.utcnow())*1000)

    def set_q_time(self,response):
        json_response = json.loads(response)
        if json_response and ('server_start_time' in json_response):
            self.server_start_time = int(json_response['server_start_time'])
            self.server_end_time = int(json_response['server_end_time'])
            self.additional_info = int(json_response['additional_info'])
        else:
            self.server_start_time = -1
            self.server_end_time = -1

    
    def __str__(self):
        return '{},{},{},{},{},{}'.format(self.id,self.start_time,self.server_start_time,self.server_end_time,self.end_time)

    def get_row(self):
        return [self.id,self.start_time,self.server_start_time,self.server_end_time,self.additional_info,self.end_time]


class Responses: 

    CSV_HEADERS = ['id','start_time','server_start_time','server_end_time','additional_info','end_time']
    def __init__(self,config):
        self.job_name = config.job_name
        self.dir_name = config.dir_name
        self.responses = []
    
    def create_add_response(self,id,start_time=None,q_time=None,end_time=None):
        single_response = SingleResponse(id,start_time,q_time,end_time)
        self.responses.append(single_response)

    def get_file_name(self,time_stamp=True):
        
        file_name = None
        if time_stamp:
            file_name = self.job_name+"_"+str(round(datetime.timestamp(datetime.utcnow())*1000))+".csv"
        else:
            file_name = self.job_name+".csv"

        return os.path.join(self.dir_name,file_name)

    def add_response(self,r_object):
        self.responses.append(r_object)

    def make_dir_if_not_exist(self):
        
        ## try to create and catch on fail.
        try:
            os.mkdir(self.dir_name)
        except:
            pass
            

    
    """
        Write all the result
    """

    def finished(self):

        self.make_dir_if_not_exist()
        out_file_name = self.get_file_name()
        with open(out_file_name,'w') as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow(self.CSV_HEADERS)

            for response in self.responses:
                writer.writerow(response.get_row())

        print("Finished writing {}".format(self.job_name))



