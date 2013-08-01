#!/usr/bin/env python
from time import strftime, localtime
import os
import os.path
import sys
pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname) 
files = os.listdir(fullpath)
for file in files:
	if file == "strattondata.csv":
		newname = strftime("/"+"%B"+"%Y", localtime())+"sd.csv"
		os.rename(fullpath+"/strattondata.csv", fullpath+newname)
	elif file == "conroedata.csv":
		newname = strftime("/"+"%B"+"%Y", localtime())+"cd.csv"
		os.rename(fullpath+"/conroedata.csv", fullpath+newname)
