#!/usr/local/bin/python3.6.lamachine -W all
# ner.py: perform named antity recognition with frog
# usage: ner.py < text
# note adapted from: https://www.tutorialspoint.com/python/python_networking.htm
# 20180604 erikt(at)xs4all.nl

from pynlpl.clients.frogclient import FrogClient
import re
import socket
import sys

PORT = 8080
MAXDATA = 1024
NERID = 4
POSID = 3
TOKENID = 0

def prettyPrint(data):
    prettifiedOutput = ""
    for row in data:
        if len(row) >= NERID+1 and row[0] != None:
            lastLine = row[TOKENID]+" "+row[POSID]+" "+row[NERID]
            prettifiedOutput += (lastLine + "\n")
    prettifiedOutput += "\n"
    return prettifiedOutput
    
def applyNer(lines):
    frogclient = FrogClient('localhost',PORT,returnall=True)
    nerOutput = ""
    for line in lines:
        data = frogclient.process(line)
        nerOutput += prettyPrint(data)
    return nerOutput

if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line)
    print(applyNer(lines))

