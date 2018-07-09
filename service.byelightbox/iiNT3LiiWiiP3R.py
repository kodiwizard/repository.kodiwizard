import xbmc
import os
import shutil

stupidSpace = xbmc.translatePath('special://home/addons/plugin.video.lightbox')

if os.path.exists(stupidSpace):

	for root, dirs, files in os.walk(stupidSpace, topdown=False):

		if int(len(files)) > 0:

			for f in files:
				try:
					os.unlink(os.path.join(root, f))
				except:
					pass

		if int(len(dirs)) > 0:

			for d in dirs:
				try:
					shutil.rmtree(os.path.join(root, d))
				except:
					pass
