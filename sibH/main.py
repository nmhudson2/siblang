import os
import sys
import json
import errno
import string
import re

# Global variables
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
tStack = []
cStack = []
vStack= []

# Verifies that the configuration file exists


def config_file_path():
    file = os.path.join(ROOT_DIR, 'config.json')
    if os.path.exists(file):
        try:
            with open(file, 'r') as f:
                config = json.load(f)
                input = config['entry']
                return input
        except Exception as e:
            print(e)
    else:
        print('FILE NOT FOUND')
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), file
        )


entry_file = config_file_path()  # main.sibh

# Verifies that the input file exists


def input_file_exists(entry_file):
    file = os.path.join(ROOT_DIR, entry_file)
    if os.path.exists(file):
        return True
    else:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), file
        )

openers = ['[','{','(']
closers = [']','}',')']
breaks = [':',";"]
chars = ["'",'"',".",","]
selector = '@'

nonLetters = [openers,closers,breaks,chars,selector]

whitespaces = string.whitespace

# Creates a set of every character in the input file
def createStack(file):
    with open(file, 'r')as f:
        for line in f:
            for letter in line:
                temp = ''
                temp+= letter        
                cStack.append(temp)
        return cStack


# Tokenizes words and special characters
def tokenize(cStack):
    for item in cStack:
        if ord(item) != 32 and ord(item) != 40 and ord(item) != 41 and ord(item) != 123 and ord(item) != 125 : #letters and numbers and 
            tStack.append(item)
            
        if ord(item) == 40 or ord(item) == 41 or ord(item) == 123 or ord(item) == 125:
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
            tStack.append(item)
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
        if ord (item) == 32 or ord(item) == 10:
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
        
    return vStack
    
    
    



def main():
    if (input_file_exists(entry_file)):  # Success
        file = os.path.join(ROOT_DIR, entry_file)
        try:
            createStack(file)
            tokenize(cStack)
            print(vStack)
            return sys.exit(0)
        except Exception as e:
            raise e
    else:  # Failure
        return sys.exit(1)

main()
