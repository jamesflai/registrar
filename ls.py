#!/usr/bin/env python3

from pathlib import Path
import sys
import os
import datetime
import stat

#check if directory specified
dir_given=False
if len(sys.argv)>1:
	dir_given=True

if dir_given==False:
	path=os.getcwd()
else:
	path=sys.argv[1]

try:
	p=Path(path)
	parent=p.parents[0]
	files=p.glob('*')
	#execute if directory
	if stat.filemode(p.stat().st_mode).startswith('d'):
		print('drwxr-xr-x+ '+str(p.stat().st_nlink)+' '+p.owner()+' '+p.group()+' '+str(p.stat().st_size)+' '+str(datetime.datetime.fromtimestamp(p.stat().st_mtime))+' .')
		print('drwxr-xr-x+ '+str(parent.stat().st_nlink)+' '+parent.owner()+' '+parent.group()+' '+str(parent.stat().st_size)+' '+str(datetime.datetime.fromtimestamp(parent.stat().st_mtime))+' ..')
		for file in files:
			currP=Path(file)
			name=str(file).split('/')
			print(stat.filemode(currP.stat().st_mode)+' '+str(currP.stat().st_nlink)+' '+currP.owner()+' '+currP.group()+' '+str(currP.stat().st_size)+' '+str(datetime.datetime.fromtimestamp(currP.stat().st_mtime))+' '+name[-1])
	else:
		#this is the case where a file is provided
		#if wildcard used python interpreter takes sys.argv as the expanded wildcard and not the character * so this works
		p=sys.argv
		p.remove(sys.argv[0])
		files=p #these three lines remove the './ls.py' from the iterable (remove is inplace and return NoneType so made a copy)
		print(files)
		for file in files:
			currP=Path(file)
			name=str(file).split('/')
			print(stat.filemode(currP.stat().st_mode)+' '+str(currP.stat().st_nlink)+' '+currP.owner()+' '+currP.group()+' '+str(currP.stat().st_size)+' '+str(datetime.datetime.fromtimestamp(currP.stat().st_mtime))+' '+name[-1])		

#error catch for invalid path
except FileNotFoundError:
	print('ls: cannot access '+path+': No such file or directory')