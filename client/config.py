import os
import json

""""
    Single configuration object. The init method loops through all the configuration. 
    Should be modified if hits hits performance.
"""
class Configuration:

    def __init__(self,name,json_data):
        self.job_name = name 
        for obj in json_data:
            if obj['job_name']==name:
                self.threads = obj['threads']
                self.end_point = obj['end_point']

        
"""
Static class. This may be used later point as factory.
"""

class ConfigReader:

    CONFIG_FILE = 'config.json'
    json_data = None
    @staticmethod
    def get_configuration(name):
        if not ConfigReader.json_data:
            with open(os.path.join(os.path.dirname(__file__),ConfigReader.CONFIG_FILE)) as f:
                ConfigReader.json_data =  json.load(f)
        
        return Configuration(name,ConfigReader.json_data)
        
