import os
import sys
import json
import errno

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Verifies that the configuration file exists


def config_file_path():
    file = 'sibH\config.json'
    if os.path.exists(file):
        try:
            with open(file, 'r') as f:
                config = json.load(f)
                input = config['entry']
                return input
        except Exception as e:
            print(e)
    else:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), file
        )


entry_file = config_file_path()  # main.sibh

# Verifies that the input file exists


def input_file_exists(entry_file):
    file = (ROOT_DIR + "\\" + entry_file)
    if os.path.exists(file):
        return True
    else:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), file
        )


def main():
    if (input_file_exists(entry_file)):  # Success
        try:
            return sys.exit(0)
        except Exception as e:
            raise e
    else:  # Failure
        return sys.exit(1)
