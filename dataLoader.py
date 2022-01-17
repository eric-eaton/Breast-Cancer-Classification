"""
dataLoader.py
Contains the DataLoader class
"""

from FeatureExtractor import FeatureExtractor
from imageLoader import imageLoader
from data_preprocessor import preprocessor
from tqdm import tqdm
import random

"""
DataLoader()
Main Class
This is the class which takes the folder which contains the images and creates a dataset which can be used for machine 
learning with SciKit Learn. The only thing which must be passed to the class is the data_file_path, which is the name
of the folder containing the data. T

"""
class DataLoader:
    """
    __init__
    CONSTRUCTOR
    This function takes at least one argument, which is the folder containining the data.
    The feature_extractor class extracts the features from each image.
    The preprocessor returns count, which is the total number of images. prepreocessor creates the folders which
    contain the sorted images, counts the number of images, and copies all the images into the correct folder.
    imageLoader() recieves the count so the progress bar can be displayed while the images are loaded.
    The image loader loads each image into a (50,50,3) numpy array. The dataset is a dictionary object containing other
    dictionaries. The main keys are 'positive' and 'negative'. There are four dictionaries within each key. The 'train'
    key's values are the numpy arrays representing the training images. The 'validation' key's values are the numpy
    arrays representing the validation images. The data is split for 90% testing and 10% validation.
    The 'train_file' key's values and the 'validation_file' key's values are the file paths for each image

    mode is the mode, either training or validation.
    the train_list will contain a list of the indexes for positive and negative training images
    the validation_list will contain a list of the indexes for positve and negative validation images
    shuffle is a boolean and determines whether the images are shuffled
    train_images and validation_images will contain a list of the image arrays
    train_features and validation_features will contain an array with the features
    of the images(explained in FeatureExtractor NOTE)



    """
    def __init__(self, data_file_path, shuffle=False):
        self.feature_extractor = FeatureExtractor()
        self.count = preprocessor(data_file_path)
        self.dataset = imageLoader(self.count)
        self.mode = 'train'
        self.train_list = []
        self.validation_list = []
        self.shuffle = shuffle
        self.train_images = []
        self.validation_images=[]
        self.train_features=[]
        self.validation_features=[]
        print("\n-Loading Data-")
        progressBar = tqdm(total = self.count)
        for key in self.dataset:
            #for loop for the training images
            for index in range(len(self.dataset[key]['train'])):
                self.train_list.append((key,index))
                image = self.dataset[key]['train'][index]
                features = self.feature_extractor.extract_features(image)
                self.train_features.append(features)
                self.train_images.append(image)
                progressBar.update(1)
            #for loop for the validation images
            for index in range(len(self.dataset[key]['validation'])):
                self.validation_list.append((key,index))
                image = self.dataset[key]['validation'][index]
                features = self.feature_extractor.extract_features(image)
                self.validation_images.append(image)
                self.validation_features.append(features)
                progressBar.update(1)

        self.set_mode('train', False)
    """
    set_mode()
    Main function. 
    mode must be 'train' or 'val'
    """
    def set_mode(self,mode,shuffle):
        self.set_shuffle(shuffle)
        #this is an error message
        assert mode == 'train' or mode == 'val', 'only supports training and validation'
        self.mode = mode
        if mode == 'train':
            self.data_list = self.train_list
            self.data = self.train_images
            self.features = self.train_features
        else:
            self.data_list = self.validation_list
            self.data = self.validation_images
            self.features = self.validation_features
        self.reset_shuffle()

    """
    set_shuffle() 
    sets shuffle to true or false
    """
    def set_shuffle(self, shuffle):
        self.shuffle = shuffle
    """
    reset_shuffle()
    if shuffle is currently true, the indexes of the data are shuffled. 
    """
    def reset_shuffle(self):
        self.indexes = list(range(len(self.data_list)))
        if self.shuffle:
            random.shuffle(self.indexes)

    """
    Enables the use of the len() function on an object created by calling the class
    """
    def __len__(self):
        return len(self.data_list)

    """
    the getitem function allows the enumerable() function to be used on an object created by calling the class.
    
    """
    def __getitem__(self, data_index):
        i = self.indexes[data_index]
        key, idx = self.data_list[i]
        if data_index == len(self.data_list):
            self.reset_shuffle()
        return self.data[i], self.features[i], key



#uncomment to test in console
"""
from imageLoader import imageLoader
from dataLoader import DataLoader
dataset = imageLoader()
idc_dataloader = DataLoader(dataset)
imgs=[]
count=0
for i, (image, features, class_id) in enumerate((idc_dataloader)):
  imgs.append(image)
  count += 1
  if count >= 10:
    break    """





