#!/usr/bin/python2
from sys import argv
import os
import random
from datetime import datetime, timedelta
import subprocess
import pickle
import sys

if (len(argv) != 2):
    print("USAGE: ./fixr.py PATH/TO/REPOSITORY")
    exit(1)

runpath = os.getcwd()
path = argv[1]
os.chdir(path)

with open(runpath+"/commit_messages.pickle", 'r') as fh:
    messages = pickle.load(fh)

for m in messages :
    if m == "":
        messages.remove(m)

def generate_commits():
    time = datetime.now()
    for i in range(0, 365):
        formatted_time = time.strftime("\'%a %b %d %H:%M:%S %Y -0500\'")
        subprocess.call("fortune > DONT_README", shell=True)
        subprocess.call("git add DONT_README", shell=True)
        subprocess.call("env GIT_AUTHOR_DATE="\
                + formatted_time \
                +" GIT_COMMITTER_DATE="+formatted_time\
                +"> /dev/null git commit DONT_README -m \"" + random.choice(messages) + "\"", shell=True)
        time = time - timedelta(days=1)


for x in range(1000):
    sys.stdout.write("%d commits generated per day, %d total.\r\n" %(x, x*365))
    generate_commits()
