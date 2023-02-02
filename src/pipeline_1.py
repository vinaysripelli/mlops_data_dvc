import os
import argparse
import yaml # define the configurations
import logging

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config
def main(config_path,data_source):
    config = read_params(config_path)
    print(config)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    default_config_path= os.path.join("config","params.yaml")
    args.add_argument("--config",default=default_config_path) #configuration files consists of the all the parameters required
    args.add_argument("--datasource",default=None)
    parsed_args= args.parse_args()
    #print(parsed_args)
    #print(parsed_args.config)
    #print(parsed_args.datasource)
    main(config_path=parsed_args.config,data_source=parsed_args.datasource)