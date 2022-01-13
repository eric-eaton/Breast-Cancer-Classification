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

#tqdm is a loading bar module
from tqdm import tqdm


"""
preprocessor()
MAIN
This function utilizes the create_dirs and image_lister helper functions to create the file structure and sort
the images to be utilized in the program
"""

def preprocessor():
    positive, negative = create_dirs()
    originalPaths, count = images_lister(dataset)
    progressBar = tqdm(total=count)
    for file in originalPaths:
        if file[-5] == '0':
            shutil.copy2(file, negative)
            progressBar.update(1)
        elif file[-5] == '1':
            shutil.copy2(file,positive)
            progressBar.update(1)




"""
create_paths()
Helper Method
This method generates the paths for the project. Creates the processed folder as well as two sub folders
for storing the postive and negative IDC images
os.getcwd() allows the program to work on any machine
os.path.join() takes two arguments. The first is the base path name, or the path which we wish to join to. 
The second is the file name or path name we wish to join to it. 
ex) C:\\USER would be the base path and file1 would be the file names
if you pass them as string to os.path.join("C:\\USER","file1")
you will get "C:\\USER\\file1" returned
"""
def create_paths():
    #the path of the project on any system
    project_path = os.getcwd()
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
    count = 0
    for (rootDir, dirNames, filenames) in os.walk(dataset):
        for filename in filenames:
            if filename == "":
                continue
            path = os.path.join(rootDir,filename)
            imageList.append(path)
             count = count + 1
    return imageList, count
















