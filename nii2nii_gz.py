import os
from subprocess import call

A = open("sessid_all")
sublist = [line.strip() for line in A]

for i in sublist:
    file = os.getcwd()+"/"+i+"/resting/002/rest.nii"
    call(["gzip", file])
