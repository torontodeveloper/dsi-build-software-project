from typing import Any,Optional
import argparse
import yaml

class Analysis():
    def __init__(self,analysis_config:str):
        CONFIG_PATHS =['system_config.yml','user_config.yml','job_config.yml']
        parser = argparse.ArgumentParser()
        parser.add_argument('job_config',type=str)

        args = parser.parse_args()
        paths_to_load = CONFIG_PATHS + [args.job_config]
        print(args)

        config = {}

        for path in paths_to_load:
            print('Loading',path)
        with open(path,'r') as file:
            this_config = yaml.safe_load(file)
            print('this config',this_config)
        
        config.update(this_config)
    
    def load_data(self,):
        pass
    def compute_analysis(self) -> Any:
        pass
    
    def plot_data(self,save_path:Optional[str] = None) -> matplotlib.Figure:
        pass
        