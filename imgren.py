# purpose 	rename image files using the OCD-like formatting I have for my personal library.
# usage		$user: python imgren.py /path/to/folder/with/files

import os
import datetime
import sys

#
def renamer():
	target = sys.argv[1]
	os.chdir(target)

	allfiles = os.listdir(target)
	for filename in allfiles:
		t = os.path.getmtime(filename)
		v = datetime.datetime.fromtimestamp(t)
		x = v.strftime('%d-%m-%Y-%H_%M_%S')
		os.rename(filename, "IMG_" + x +".jpg")
		print("renamed: " + filename)

renamer()