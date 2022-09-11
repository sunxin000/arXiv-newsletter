from ruamel import yaml
with open('./config.yml', encoding="utf-8") as config_file:
    content = yaml.load(config_file, Loader=yaml.RoundTripLoader)
    content['mail']['password'] =  '124'
    yaml.dump(content, config_file, Dumper=yaml.RoundTripDumper)