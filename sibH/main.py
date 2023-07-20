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
special = ["!","#","$","%","^","&","*"]

functions= ['attrs','inner']

tags=["!DOCTYPE",
"html",
"head",
"title",
"meta",
"link",
"script",
"style",
"body",
"h1",
"h2",
"h3",
"h4",
"h5",
"h6",
"p",
"br",
"hr",
"a",
"img",
"ul",
"ol",
"li",
"dl",
"dt",
"dd",
"table",
"tr",
"th",
"td",
"thead",
"tbody",
"tfoot",
"caption",
"div",
"span",
"form",
"input",
"textarea",
"button",
"select",
"option",
"label",
"fieldset",
"legend",
"iframe",
"audio",
"video",
"canvas",
"svg",
"nav",
"header",
"footer",
"section",
"article",
"aside",
"main",
"address",
"time",
"abbr",
"blockquote",
"q",
"cite",
"em",
"strong",
"i",
"b",
"s",
"u",
"sub",
"sup",
"code",
"pre",
"small",
"big",
"mark",
"del",
"ins",
"progress",
"meter",
"details",
"summary",
"menu",
"menuitem",
"dialog"

]

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
        if ord(item) == 58 or ord(item) == 59 or ord(item) == 39 or ord(item) in special or ord(item) in openers or ord(item) in closers:
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
            tStack.append(item)
            temp = (''.join(tStack).strip())
            tStack.clear()
        if ord(item) != 32 and ord(item) != 40 and ord(item) != 41 and ord(item) != 123 and ord(item) != 125 : #letters and numbers and 
            tStack.append(item)  
        if ord(item) == 40 or ord(item) == 41 or ord(item) == 123 or ord(item) == 125 or ord(item) == 39 or ord(item) in special or ord(item) in openers or ord(item) in closers:
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
            tStack.append(item)
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
        if ord (item) == 32 or ord(item) == 10 or ord(item) in special or ord(item) in openers or ord(item) in closers:
            temp = (''.join(tStack).strip(whitespaces))
            vStack.append(temp)
            temp = ''
            tStack.clear()
        
    return vStack

def setType(cont):
            if cont in functions:
                return 'Functiion'
            elif cont in tags:
                return 'Tag'
            elif cont in openers:
                return 'Opener'
            elif cont in closers:
                return 'Closer'
            elif cont == selector:
                return 'Selector'
            elif cont in chars:
                return "Char"
            elif cont in breaks:
                return 'Break'
            elif cont in tags:
                return 'Tag'
            elif cont.isalpha():
                return 'Alpha'
            elif cont.isdigit():
                return 'Digit'
            elif cont in whitespaces:
                return 'Whitespace'
            elif '://www' in cont:
                return 'Link'
            elif 'https' in cont:
                return 'Protocol'

# Turns string Tokens into Token Objects
def GenTok(vStack):
    counter = 0
    temp = []
    hop = []
    for i in range(len(vStack)):
        j = Token(vStack[i],vStack[i-1],None, setType(vStack[i]))
        temp.append(j)
        counter+=1
    counter = 0
    for i in temp:
        if i.typeOf != "Whitespace":
            hop.append(temp[counter])
        counter +=1
    vStack.clear()
    for i in temp:
        vStack.append(i)
    return vStack 

# def genComps(vStack):
#     counter = 0
#     temp = []
#     for i in vStack:
#         if i in tags:
#             j = tag(tags[counter])
#             temp.append(j)
#         counter+=1
#     return temp
    
class Token:
    def __init__(self,cont, prevT,nextT, typeOf):
        self.cont = cont
        self.prevT = prevT
        self.nextT = nextT
        self.typeOf = typeOf
    def __repr__(self) -> str:
        return f'Token is:   -  {self.cont}  -   , \t , Previous is {self.prevT} , \t , Next is {self.nextT}, \t ,Type is: {self.typeOf} \n\n'

class tag:
    def __init__(self, tag) -> None:
        self.tag = tag


class Element():
    def __init__(self, tag, ELid,attributes,innercontent, ELclass):
        self.tag = tag
        self.ELid = ELid
        self.attrubtes = attributes
        self.innerContent = innercontent
        self.ELclass = ELclass
    def genEL(tag, ELid,attributes,innercontent, ELclass):
        return f'<{tag} id={ELid} class={ELclass} {attributes}>{innercontent}</{tag}'
        


def main():
    if (input_file_exists(entry_file)):  # Success
        file = os.path.join(ROOT_DIR, entry_file)
        try:
            createStack(file)
            tokenize(cStack)
            GenTok(vStack)
            # genComps(vStack)
            print(vStack)
            # code to write out to html file here
            return sys.exit(0)
        except Exception as e:
            raise e
    else:  # Failure
        return sys.exit(1)

main()
