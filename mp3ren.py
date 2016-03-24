# purpose 	rename mp3 files using the OCD-like formatting I have for my personal library.
# usage		$user: python mp3ren.py /path/to/folder/with/files

import re
import glob
import os
import sys

from eyed3 import id3

#
def renamer():
	fn = sys.argv[1]
	print fn
	if os.path.exists(fn):
		filepath = os.path.abspath(fn + "/*.mp3")
		rfile = filepath.replace("\\", "/")
		for pathname in glob.glob(rfile):
			basename= pathname

			tag = id3.Tag()
			tag.parse(basename)

			artist = tag.artist
			title = tag.title

			print "artist/title: " + artist + "-" + title

			new_filename = artist + " - " + title + ".mp3"
			if new_filename != basename:
				os.rename(pathname, os.path.join(os.path.dirname(pathname), new_filename))
				print "rename: " + pathname + " - to: " + new_filename

renamer()