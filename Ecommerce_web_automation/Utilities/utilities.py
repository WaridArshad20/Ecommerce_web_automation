import json

def load_config(config_path='config/config.json'):
    """Load the configuration from a JSON file."""
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def load_test_data(data_path='testdata/test_data.json'):
    """Load the test data from a JSON file."""
    with open(data_path, 'r') as data_file:
        test_data = json.load(data_file)
    return test_data
