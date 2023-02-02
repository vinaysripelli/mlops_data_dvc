import os
import argparse
import yaml # define the configurations
import logging



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="default") #configuration files consists of the all the parameters required
    args.add_argument("--datasource",default=None)
    parsed_args= args.parse_args()
    #print(parsed_args)
    print(parsed_args.config)
    print(parsed_args.datasource)