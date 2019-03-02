import os
import json

"""
    Single configuration object. The init method loops through all the configuration. 
    Should be modified if hits hits performance.
"""
class Configuration:

    def __init__(self,name,json_data,threads=-1,c_type='single'):

        if(c_type=='multi'):
            self.platform = json_data['platform']
            self.threads = threads
            self.end_point = json_data['base_url']+'?name='+name
            ## file name
            self.job_name = name+"_"+self.platform+"_"+str(self.threads)
            self.dir_name = name 
        else:
            self.job_name = name 
            self.dir_name = name
            for obj in json_data:
                if obj['job_name']==name:
                    self.threads = obj['threads']
                    self.end_point = obj['end_point']

        
"""
Static class. This may be used later point as factory.
"""

class ConfigReader:

    CONFIG_FILE = 'config.json'
    CONFIG_MULTI_FILE = 'config_multi.json'
    json_data = None
    json_multi_data = None
    @staticmethod
    def get_configuration(name):
        if not ConfigReader.json_data:
            with open(os.path.join(os.path.dirname(__file__),ConfigReader.CONFIG_FILE)) as f:
                ConfigReader.json_data =  json.load(f)
        
        return Configuration(name,ConfigReader.json_data)

    """

        To run all the functionalities in  oneshot.
    """

    @staticmethod
    def get_configurations(threads,cmd_jobs=None):
        if not ConfigReader.json_data:
            with open(os.path.join(os.path.dirname(__file__),ConfigReader.CONFIG_MULTI_FILE)) as f:
                ConfigReader.json_multi_data =  json.load(f)

        ## get for all jobs. The other part is not implemented now.
        ## this is required due to warm and cold startup difference.
        all_configs = []
        for job in ConfigReader.json_multi_data['jobs']:

            ## if job list is passed
            if cmd_jobs and (job not in cmd_jobs):
                continue 

            for platform in ConfigReader.json_multi_data['platforms']:
                all_configs.append( Configuration(job,platform,threads,c_type='multi'))

        return all_configs

        
        
    