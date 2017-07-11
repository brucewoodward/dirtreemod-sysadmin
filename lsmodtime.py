#!/usr/bin/env python

import os, sys, time
from stat import *

def walktree(dir, condition):
	"""walk directory, stating each file; return filename and value from stat"""
	results = []
	for root, dirs, files in os.walk(dir):
		for f in files:
			fullpath = os.path.join(root, f)
			stat = os.stat(fullpath)
			if condition(fullpath, stat):
				results.append((fullpath, stat))
	return results

if __name__ == '__main__':
	dir = sys.argv[1] if len(sys.argv) > 1 else "/etc" # default /etc
	regular_files = walktree(dir, lambda filename, stat: S_ISREG(stat.st_mode))
	files_sorted_by_modtime = sorted(regular_files, key=lambda file: file[1].st_mtime)
	for f in files_sorted_by_modtime:
		filename, mtime = f[0], time.ctime(float(f[1].st_mtime))
		print '{:<35}'.format(filename), '{:<15}'.format(mtime)
