"""
imageLoader.py
This module allows the images sorted by data_preprocessor to be loaded into numpy arrays
"""

#os will allow creating a path to the images usable by imread
import os

#imageio is a python library containing imread, which is used to load images into numpy arrarys,
#which can then be utilized by scikitlearn
from imageio import imread as imread

#tqdm for loading bar
from tqdm import tqdm

#these are the base directories where all the images are stored
#originally created by data_preproccer
positive_dir = 'processed\\positive'
negative_dir = 'processed\\negative'

"""
imageLoader()
MAIN
Uses the helper function create_dictionary() and imageLoader() to load the dataset with numpy arrays of the images
For now, we will be splitting 10% for validation during the testing phase
"""
def imageLoader():
    images_dict = create_dictionary()
    progressBar = tqdm(total=18938)
    print("-Loading Images into Dataset-")
    dataset = {}
    for key in images_dict:
        images_list = images_dict[key]
        train_stop = int(len(images_list)*0.9)
        train_files_paths=images_list[:train_stop]
        validation_files_paths = images_list[train_stop:]
        train_images = loadImages(train_files_paths, progressBar)
        validation_images = loadImages(validation_files_paths, progressBar)
        dataset[key] = {'train':train_images,
                        'val': validation_images,
                        'train_files':train_files_paths,
                        'validation_files': validation_files_paths}
    return dataset
#uncomment to visualize data
#    for key in dataset:
 #       print('train {}'.format(key),dataset[key]['train_files'])
  #      print('validation {}'.format(key), dataset[key]['validation_files'])


"""
loadImages()
HELPER
In this function, imread from imageio is used to load the image data into a numpy array, which is then stored in a list.
This list is returned to the datasetLoader to be loaded into the dataset 
imread returns a numpy array. the best way to visualize this is to import numpy and then load a single image into a
variable. Then use the numpy shape method to show the shape of the array. Since all the images have the same shape,
you should have an output of (50, 50, 3)
"""
def loadImages(list,progressBar):
    train_images = []
    for filePath in list:
        loadedImage = imread(filePath)
        train_images.append(loadedImage)
        progressBar.update(1)
    return train_images





"""
create_dictionary()
HELPER
Dictionaries store a key and values associated with the key. 
in this case, since we are utilizing binary classification, we use two keys, positive and negative.
The paths to the images will be stored as values in the dictionary
"""
def create_dictionary():
    images_dict = {"positive": [], "negative": []}
    for filename in (os.listdir(positive_dir)):
        images_dict["positive"].append(os.path.join(positive_dir, filename))

    for filename in (os.listdir(negative_dir)):
        images_dict["negative"].append(os.path.join(negative_dir, filename))

    return images_dict