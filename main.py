import sys
from pyVHR.signals.video import Video
from pyVHR.methods.pos import POS
from pyVHR.methods.chrom import CHROM
from pyVHR.methods.pbv import PBV
from pyVHR.analysis.testsuite import TestSuite, TestResult

try :
	videoFilename = (sys.argv[1],sys.argv[2])
except :
	print("Video filename and extension : python -m main.py video_filename mp4")
	exit()

video = Video(videoFilename)






# -- extract faces
video.getCroppedFaces(detector='mtcnn', extractor='skvideo')



import numpy as np
import cv2
import os

c=0
for i in video.faces:
	
	cv2.imwrite(os.path.join('D:/pyVHR/out/'+str(c) + '.jpg'), cv2.cvtColor(i, cv2.COLOR_RGB2BGR))
	c+=1
























video.printVideoInfo()

print("\nShow video cropped faces, crop size:", video.cropSize)
video.showVideo()



video.setMask(typeROI='rect', rectRegions=['forehead', 'lcheek', 'rcheek', 'nose'])
video.printROIInfo()
video.showVideo()

video.setMask(typeROI='skin_adapt',skinThresh_adapt=0.2)
video.printROIInfo()
video.showVideo()


video.setMask(typeROI='skin_fix',skinThresh_fix=[20, 50])
video.printROIInfo()
video.showVideo()


cfgFilename = 'pyVHR/analysis/sample.cfg'

# -- apply the pipeline until GT comparison
test = TestSuite(configFilename=cfgFilename)

# -- run exp and save results on a pandas file
#    change verb to see more details as follow:
#       0 - not verbose
#       1 - show the main steps
#       2 - display graphic 
#       3 - display spectra  
#       4 - display errors
#       (use also combinations, e.g. verb=21, verb=321)
result = test.start(outFilename='sampleExp.h5', verb=2)

result.dataFrame

#params = {"video": video, "verb":2, "ROImask":"rect","rectRegions":['forehead', 'lcheek', 'rcheek', 'nose'], "skinAdapt":0.2,"csv_filename":sys.argv[1]+".csv"}
#params = {"video": video, "verb":2, "ROImask":"rect","rectRegions":[ 'lcheek', 'rcheek'], "skinAdapt":0.2,"csv_filename":sys.argv[1]+".csv"}
#params= {"video": video, "verb":2, "ROImask":"rect", "rectCoords":[ [ 150 ,125 , 250 , 125 ] ],"csv_filename":sys.argv[1]+".csv"}

params = {"video": video, "verb":2, "ROImask":"skin_adapt", "skinAdapt":0.2,"csv_filename":sys.argv[1]+".csv"}

# -- invoke the method
m = CHROM(**params)
#m = POS(**params)

# -- invoke the method
bpmES, timesES = m.runOffline(**params)



















result.dataFrame
