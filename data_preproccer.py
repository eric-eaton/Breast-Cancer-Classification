"""
This object loads the IDC dataset.
"""

"""
The IDC dataset contains 277,524 patches of size 50x50. They come from 162 whole mount slide images of Breast Cancer
This loader will sort the data into IDC Negative and IDC Positive. 
Currently the datasetTEST is a subset of the dataset for testing purposes
"""
# the os library will allow the creation of the folders to store the positive and negative IDC samples
import os
#This is the path variable for the original files of the dataset
dataset = "datasetTEST"

#shutil is a library used for copying files
import shutil

"""
preprocessor()
MAIN
This function utilizes the create_dirs and image_lister helper functions to create the file structure and sort
the images to be utilized in the program
"""

def preprocessor():
    positive, negative = create_dirs()
    originalPaths = images_lister(dataset)

    for file in originalPaths:
        if file[-5] == '0':
            shutil.copy2(file, negative)
        elif file[-5] == '1':
            shutil.copy2(file,positive)




"""
create_paths()
Helper Method
This method generates the paths for the project. Creates the processed folder as well as two sub folders
for storing the postive and negative IDC images
"""
def create_paths():
    #the path of the project
    project_path = "C:\\Users\\Eric Eaton\\Documents\\School\\Phyton\\ML Projects\\SKLearnCancerNet"
    # processed_path holds the path to the processed folder where the data will be sorted
    processed_path = os.path.join(project_path, "processed")
    #this creates the positive and
    positive_path = os.path.join(processed_path, "positive")
    negative_path = os.path.join(processed_path, "negative")
    return processed_path, positive_path, negative_path

"""
create_dirs()
HELPER Method
This method uses the helper method create_paths() to generates the actual directories for the project
If the directories already exist, new ones will not be created. 
"""
def create_dirs():
    processed, positive, negative = create_paths()
    if not os.path.exists(processed):
        print("creating \\processed directory")
        os.makedirs(processed)
    if not os.path.exists(positive):
        print("creating \\positive directory")
        os.makedirs(positive)
    if not os.path.exists(negative):
        print("creating \\negative directory")
        os.makedirs(negative)
    return positive,negative

"""
image_lister()
HELPER Method
This method creates a list of filepaths for all the images
This allows the files to be copied into their respective folders
"""
def images_lister(dataset):
    imageList =[]
    for (rootDir, dirNames, filenames) in os.walk(dataset):
        for filename in filenames:
            if filename == "":
                continue
            path = os.path.join(rootDir,filename)
            imageList.append(path)
    return imageList
















