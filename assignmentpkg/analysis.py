from typing import Any,Optional
import argparse
import yaml
import requests

class Analysis():
    def __init__(self,analysis_config:str):
        CONFIG_PATHS =['system_config.yml','user_config.yml','job_config.yml']
        parser = argparse.ArgumentParser(description='Analysis package')
        parser.add_argument('job_config',type=str)

        args = parser.parse_args()
        paths_to_load = CONFIG_PATHS + [args.job_config]
        print(args)

        config = {}
        for path in paths_to_load:
            print('Loading',path)
        with open(path,'r') as file:
            this_config = yaml.safe_load(file)
        
        config.update(this_config)
        # topic can be election or movies configured in job_config file
        topic = config["topic"]
        self.url = config["url"]+'articlesearch.json?q='+topic+'&api-key='+config["api_key"]
    
    def load_data(self,):
        response = requests.get(self.url)
        return response
    def compute_analysis(self) -> Any:
        pass
    
    def plot_data(self,save_path:Optional[str] = None) -> None:
        pass
# this is to test this class,  
analysis = Analysis('test')
response = analysis.load_data()
json_resp = response.json()
print('response is',json_resp["response"])
       