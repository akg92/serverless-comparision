from time import gmtime
import csv 
import json 
from datetime import datetime
class SingleResponse:

    def __init__(self,id,start_time=None,q_time=None,end_time=None):
        self.id = id
        if not start_time:
            self.start_time = round(datetime.timestamp(datetime.utcnow())*1000)
        else:
            self.start_time = start_time
        self.q_time = q_time
        self.end_time = end_time

    def end(self):
        self.end_time = round(datetime.timestamp(datetime.utcnow())*1000)

    def set_q_time(self,response):
        json_response = json.loads(response)
        self.q_time = int(json_response['q_time']) 
    
    def __str__(self):
        return '{},{},{},{}'.format(self.id,self.start_time,self.q_time,self.end_time)

    def get_row(self):
        return [self.id,self.start_time,self.q_time,self.end_time]


class Responses: 

    CSV_HEADERS = ['id','start_time','q_time','end_time']
    def __init__(self,job_name):
        self.job_name = job_name
        self.responses = []
    
    def create_add_response(self,id,start_time=None,q_time=None,end_time=None):
        single_response = SingleResponse(id,start_time,q_time,end_time)
        self.responses.append(single_response)

    def get_file_name(self,time_stamp=True):
        
        if time_stamp:
            return self.job_name+"_"+str(round(datetime.timestamp(datetime.utcnow())*1000))+".csv"
        else:
            return self.job_name+".csv"

    def add_response(self,r_object):
        self.responses.append(r_object)
    
    """
        Write all the result
    """

    def finished(self):

        out_file_name = self.get_file_name()
        with open(out_file_name,'w') as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow(self.CSV_HEADERS)

            for response in self.responses:
                writer.writerow(response.get_row())

        print("Finished writing {}".format(self.job_name))



