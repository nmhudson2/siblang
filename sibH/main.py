import os
import sys
import json
import errno

# Global variables
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
tStack = []
cStack = []

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

closures = {
    '(': ')',
    '{': '}'
}
op = ';'
selector = '@'


# def consume(word):
#     for letter in word.split:


# class element:
#     def __init__(self, ID, params):
#         self.ID = ID
#         self.params = params


# class Token:
#     def __init__(self, text, nextVal):
#         self.text = text
#         self.nextVal = nextVal

# def consumeToken():
#     cur = 0
#     next = cur + 1


def main():
    if (input_file_exists(entry_file)):  # Success
        file = os.path.join(ROOT_DIR, entry_file)
        try:
            with open(file, 'r')as f:
                for line in f:
                    for word in line:
                        print(word.split())

            return sys.exit(0)
        except Exception as e:
            raise e
    else:  # Failure
        return sys.exit(1)


main()
