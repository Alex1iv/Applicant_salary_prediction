import json
from dotmap import DotMap

def config_reader(path_to_json_conf: str) -> dict:
    """Load parameters from configuration file.

    Args:
    ------------
    path_to_json_conf (_str_): путь к файлу конфигурации

    Returns:
    ------------
    config (dict): dictionary with parameters
    """    
    with open(path_to_json_conf, 'r') as config_file:
        config_dict = json.load(config_file)
    
    config = DotMap(config_dict)
    
    return config