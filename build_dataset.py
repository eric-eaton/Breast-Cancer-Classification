"""
build_dataset.py
"""
#files
import config

"""
Libraries 
"""
from imutils import paths

import random, shutil, os

#assign original path#

#creates a list of the file paths for the dataset
originalPaths = list(paths.list_images(config.INPUT_DATASET))
random.seed(7)
#shuffles the list
random.shuffle(originalPaths)

#split training and testing paths
index = int(len(originalPaths)*config.TRAIN_SPLIT)
trainPaths = originalPaths[:index]
testPaths = originalPaths[index:]

#split up training and validation paths
index = int(len(trainPaths)*config.VAL_SPLIT)
valPaths = trainPaths[:index]
trainPaths = trainPaths[index:]

datasets = [("training", trainPaths, config.TRAIN_PATH),
            ("validation", valPaths,config.VAL_PATH),
            ("testing", testPaths, config.TEST_PATH)]

#this builds the file system which divides the image data into training, validation, and testing sets.
for (setType, originalPaths, basePath) in datasets:
    print(f'Building {setType} set')

    if not os.path.exists(basePath):
        print(f'Building directory {basePath}')
        os.makedirs(basePath)

    for path in originalPaths:
        file =path.split(os.path.sep)[-1]
        label = file[-5:-4]

        labelPath = os.path.sep.join([basePath,label])
        if not os.path.exists(labelPath):
            print(f'Building directorty {labelPath}')
            os.makedirs(labelPath)

        newPath = os.path.sep.join([labelPath, file])
        shutil.copy2(path,newPath)