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


tags = [
    '<!DOCTYPE>',
    '<html>',
    '<head>',
    '<title>',
    '<meta>',
    '<link>',
    '<script>',
    '<style>',
    '<body>',
    '<h1>',
    '<h2>',
    '<h3>',
    '<h4>',
    '<h5>',
    '<h6>',
    '<p>',
    '<br>',
    '<hr>',
    '<a>',
    '<img>',
    '<ul>',
    '<ol>',
    '<li>',
    '<dl>',
    '<dt>',
    '<dd>',
    '<table>',
    '<tr>',
    '<th>',
    '<td>',
    '<thead>',
    '<tbody>',
    '<tfoot>',
    '<caption>',
    '<div>',
    '<span>',
    '<form>',
    '<input>',
    '<textarea>',
    '<button>',
    '<select>',
    '<option>',
    '<label>',
    '<fieldset>',
    '<legend>',
    '<iframe>',
    '<audio>',
    '<video>',
    '<canvas>',
    '<svg>',
    '<nav>',
    '<header>',
    '<footer>',
    '<section>',
    '<article>',
    '<aside>',
    '<main>',
    '<address>',
    '<time>',
    '<abbr>',
    '<blockquote>',
    '<q>',
    '<cite>',
    '<em>',
    '<strong>',
    '<i>',
    '<b>',
    '<s>',
    '<u>',
    '<sub>',
    '<sup>',
    '<code>',
    '<pre>',
    '<small>',
    '<big>',
    '<mark>',
    '<del>',
    '<ins>',
    '<progress>',
    '<meter>',
    '<details>',
    '<summary>',
    '<menu>',
    '<menuitem>',
    '<dialog>'
]

openers = ['[','{','(']
closers = [']','}',')']
breaks = [':',";"]
chars = ["'",'"',".",","]
selector = '@'

nonLetters = [openers,closers,breaks,chars,selector]

whitespaces = string.whitespace

def createStack(file):
    with open(file, 'r')as f:
        for line in f:
            for letter in line:
                temp = ''
                temp+= letter        
                cStack.append(temp)
        return cStack
    
def tokenize(cStack):
    for item in cStack:
        if ord(item) != 32: #letters and numbers and characters
            tStack.append(item)
        if ord (item) == 32 or ord(item) == 10:
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()

    # temp = (''.join(tStack).strip(whitespaces))
    
    



def main():
    if (input_file_exists(entry_file)):  # Success
        file = os.path.join(ROOT_DIR, entry_file)
        try:
            createStack(file)
            
            print(tokenize(cStack))
            return sys.exit(0)
        except Exception as e:
            raise e
    else:  # Failure
        return sys.exit(1)

main()
