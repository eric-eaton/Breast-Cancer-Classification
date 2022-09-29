Abstract— Breast cancer is one of the most common types of cancer in women, representing 30% of new cancer cases in the United States per year and is the leading cause of cancer-induced mortality among women. Diagnosis is determined through mammography screenings and biopsies followed by analysis of histopathological images. Machine Learning has been proven to be an essential tool in image classification, with Convolutional Neural Networks (CNN) providing high accuracy, but long training time. In a medical setting, fast and efficient diagnoses are imperative to life-saving treatment. To provide the optimal machine learning model for medical use, we converted unstructured data to structured data to further explore model performance. We utilized Singular Value Decomposition to extract features from 277,524 histopathological images and implemented Recursive Feature Selection to reduce the dimensionality of our resultant dataset. We then trained the Logistic Regression, Decision Tree, XGBoost, K-Nearest Neighbors and Multi-layer Perceptron machine learning algorithms on our dataset. K-nearest Neighbors was found to have the highest accuracy of 77.94%%. While our models trained faster on the dataset than a CNN, the low accuracy led us to conclude these models are not suitable for image classification applications.

To view the jupyter notebook containing all the elements of the program and the view the pipline we developed use this link:

https://nbviewer.org/github/eric-eaton/Breast-Cancer-Classification/blob/main/Project%20Instructions.ipynb

The dataset used for this project can be found https://www.kaggle.com/paultimothymooney/breast-histopathology-images.

Our research paper can be read here https://drive.google.com/file/d/1SD6T5L08VmJ7y0LMUg9IVFeIMPSnE2e1/view?usp=sharing at request.

Our paper was submitted to inderscience and we are currently awaiting response. 
