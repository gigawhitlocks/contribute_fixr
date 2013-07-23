#!/usr/bin/python2
from __future__ import print_function
from sys import argv, stdout
import os
import random
from datetime import datetime, timedelta
import subprocess
import pickle

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
    total = 0
    for i in range(0, 365):
        if ( random.randint(0,5) != 3 ): # why 3? why not?
            hour_drift = random.randint(-6,6)
            minute_drift = random.randint(0,60)
            time = time + timedelta(hours=hour_drift,minutes=minute_drift)
            formatted_time = time.strftime("\'%a %b %d %H:%M:%S %Y -0500\'")
            subprocess.call("fortune > DONT_README", shell=True)
            subprocess.call("git add DONT_README", shell=True)
            subprocess.call("env GIT_AUTHOR_DATE="\
                    + formatted_time \
                    +" GIT_COMMITTER_DATE="+formatted_time\
                    +"> /dev/null git commit DONT_README -m \"" + random.choice(messages) + "\"", shell=True)
            time = time - timedelta(days=1, hours=hour_drift, minutes=minute_drift)
            total += 1

        else:
            pass

    return total


total = 0
for x in range(1000):
    total += generate_commits()
    print("Roughly %d commits generated per day, %d actual total." %(x+1, total), end='\r')
    stdout.flush() # not sure why it wont let me add flush=True as a keyword argument to print()
