#!/usr/bin/env python3

from pathlib import Path
import sys
import datetime
import time
import stat

try:
	file=sys.argv[1]
	f=Path(file)
	print('File: '+f.name)
	if stat.filemode(f.stat().st_mode).startswith('d'):
		print('Size: '+str(f.stat().st_size)+'          Blocks: '+str(f.stat().st_blocks)+'          IO Block: '+str(f.stat().st_blksize)+'   directory')
	elif f.stat().st_size==0:
		print('Size: '+str(f.stat().st_size)+'          Blocks: '+str(f.stat().st_blocks)+'          IO Block: '+str(f.stat().st_blksize)+'   regular empty file')
	else:
		print('Size: '+str(f.stat().st_size)+'          Blocks: '+str(f.stat().st_blocks)+'          IO Block: '+str(f.stat().st_blksize)+'   regular file')
	print('Device: '+str(hex(f.stat().st_dev))+'h/'+str(f.stat().st_dev)+'d    Inode: '+str(f.stat().st_ino)+'    Links: '+str(f.stat().st_nlink))
	print('Access: ('+str(oct(f.stat().st_mode)[4:])+'/'+str(stat.filemode(f.stat().st_mode))+')  Uid: ('+str(f.stat().st_uid)+'/   '+f.owner()+')  Gid: ('+str(f.stat().st_gid)+'/   '+f.group()+')')
	print('Access: '+str(datetime.datetime.fromtimestamp(f.stat().st_atime))+' '+'%05d' % (int(-time.timezone/(36)))) #convert from seconds to hours and reverse
	print('Modify: '+str(datetime.datetime.fromtimestamp(f.stat().st_mtime))+' '+'%05d' % (int(-time.timezone/(36))))
	print('Change: '+str(datetime.datetime.fromtimestamp(f.stat().st_ctime))+' '+'%05d' % (int(-time.timezone/(36))))
	print(' Birth: '+str(datetime.datetime.fromtimestamp(f.stat().st_birthtime))+' '+'%05d' % (int(-time.timezone/(36))))
except IndexError:
	print('stat: missing operand')
	print('Try \'stat --help\' for more information.')
except FileNotFoundError:
	print('stat: cannot access '+sys.argv[1]+': No such file or directory')