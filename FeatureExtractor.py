"""
FeatureExtractor.py
This module contains the class FeatureExtractor, which extracts the features from the images
NOTE:
To learn about Principal Component Analysis and variance, https://youtu.be/FgakZw6K1QQ watch this video.
"""

from sklearn.decomposition import PCA

"""
FeatureExtractor
Main Class
This class extracts the feautures from the dataset and returns their features to the data loader

NOTE:
Features in this case are the singular values. What are singular values? They are the square root of the eigenvalues
for the components. What are the eigenvalues? they are the sum of the squared distance of each point of data
from the origin. This is explained in 12:00 in the video linked above. 

"""

class FeatureExtractor:
    """
    __init__
    CONSTRUCTOR
    This function is the constructor, and creates the principal component analysis object pca
    It also sets the number of classes, which by default is 2, since we are pursuing bionary classification
    in_features will be 30 to have a uniform PCA.
    TRAINING is being added later
    """
    def __init__(self, in_features=30, out_classes = 2):
        self.pca = PCA(n_components=in_features)
        self.out_classes = out_classes
        self.training = True
    """
    extract_features
    MAIN function
    This function return the singular values of the components in the pca
    """
    def extract_features(self, image):
        condensedImage = self.condenser(image)
        self.pca.fit(condensedImage)
        p = self.pca.singular_values_
        return p

    """
    condenser()
    HELPER function
    PCA can only take in a 2 Dimensional Array, which creates an issue when you want to utilize PCA for a RGB 3D array
    image(explained in NOTE in imageLoader.py). This condenser function adds the Red, Green, and Blue, Value contained
    within each pixel together, which produces a unique 50x50 two dimensional array for the image. From this 2D array,
    the feautures can be extracted. 
    
    NOTE
    imread uses the numpy datatype uint8 to signify the 8 bit color of the image. uint8 stands for 
    'unsigned inter with 8 byte' which means it can represent 0 to 255, which corresponds to the range for RGB values.
    since uint8 is bound to a specific range, adding 247 + 10 does not produce 257. The resultant will be 1. Once 255
    is reached in the addition, it rolls over, counting up from 10. This unique overflow property allows the unique 
    50x50 2D array to be created. 
    """
    @staticmethod
    def condenser(image):
        condensedImage = (image[:, :, 0] + image[:, :, 1] + image[:, :, 2])
        return condensedImage

#uncomment to test on an image and see its feature values
"""from imageio import imread

image = imread("processed\\negative\\8863_idx5_x51_y1251_class0.png")
feature_extractor = FeatureExtractor()

features = feature_extractor.extract_features(image)

print(features)"""

