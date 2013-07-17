#!/usr/bin/python2
from sys import argv
import os
import random
from datetime import datetime, timedelta
import subprocess
import string

if (len(argv) != 3):
    print("USAGE: ./fixr.py PATH/TO/REPOSITORY github_username")

path = argv[1]
os.chdir(path)
def generate_commits():
    time = datetime.now()
    for i in range(0, 365):
        message = "".join(
                [random.choice(string.ascii_letters) for x in range (0,10)])

        subprocess.call("echo "+message+" > DONT_README", shell=True)
        subprocess.call("git add DONT_README", shell=True)
        subprocess.call("env GIT_AUTHOR_DATE="\
                +time.strftime("\'%a %b %d %H:%M:%S %Y -0500\'")\
                +" git commit DONT_README -m " + message, shell=True)


        time = time - timedelta(days=1)
        #print(time.strftime("%a %b %d %H:%M:%S %Y -0500"))
generate_commits()
#commits = {}
#for commit in subprocess.check_output("git log | grep commit", shell=True).split("\n")[:-1]:
#    commit = commit.split(" ")[1] # drop the word 'commit' and get the actual id
#    commits[time] = commit



