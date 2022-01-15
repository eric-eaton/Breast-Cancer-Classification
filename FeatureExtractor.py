"""
FeatureExtractor.py
This module contains the class FeatureExtractor, which extracts the features from the images
"""

from sklearn.decomposition import PCA

"""
FeatureExtractor
Main Class
This class extracts the feautures from the dataset and returns their features to the data loader

"""

class FeatureExtractor:
    """
    __init__
    CONSTRUCTOR
    This function is the constructor, and creates the principal component analysis object pca
    It also sets the number of classes, which by default is 2, since we are pursuing bionary classification
    in_features is defaulted to 0.95, which calculates the number of features by the variance.
    TRAINING is being added later
    """
    def __init__(self, in_features=0.95, out_classes = 2):
        self.pca = PCA(n_components=in_features)
        self.out_classes = out_classes
        self.training = True
    """
    extract_features
    MAIN function
    This function return the sigular values of the components in the pca
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
    is reached in the addition, it rolls over, counting up from 10. 

    NOTE
    matplotlib pyplot has a function called imshow() which plots an image from an imread() array. If you load an image using imread() and pass
    it to imshow(), it will plot a 50x50 pixel grid of the image. Futhermore, if you pass the image through the image condenser, and then 
    into imshow() you can see that the image retains most details of the original, producing a heatmap effect. This can be seen in the 
    testImages directory. What this means is that we are still extracting features based on the same image, just flattended to work with 
    Principal Component Analysis. 

    TO TEST: copy and paste this whole section
    #I recommend doing this in the pycharm console in the project folder you have saved all the files in

    from matplotlib import pyplot as plt
    from imageio import imread
    #select any image in datasetTEST
    image = imread("processed/negative/8863_idx5_x101_y1201_class0.png")
    #with the image loaded pass it to imshow
    plt.imshow(image)
    #this will plot the image
    #now you pass image to the condenser function from FeatureExtractor
    #import the FeatureExtractor Class
    from FeatureExtractor import FeatureExtractor
    #create a new instance of the class as an object
    feature_extractor = FeatureExtractor()
    #call the function
    image_flat = feature_extractor.condenser(image)
    #plot the condensed image
    plt.imshow(image_flat)
    """
    #I made this method static becuase it was giving me an error when trying to pass image. This might have been fixed by adding self as one
    #of the variables but it works so I am going to leave it for now.
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
