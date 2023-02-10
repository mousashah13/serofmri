import numpy as np
import nibabel as nib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load fMRI data
img = nib.load('preprocessed_fmri_data.nii')
data = img.get_fdata()

# Flatten the data to a 2D array
data = np.reshape(data, (np.prod(data.shape[:3]), data.shape[3]))

# Labels for neurotransmitter expression
labels = np.zeros(data.shape[0])
labels[np.mean(data, axis=1) < 0] = 0 # low values correspond to serotonin
labels[np.mean(data, axis=1) >= 0] = 1 # high values correspond to dopamine

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=0)

# Train a SVM classifier
classifier = SVC(kernel='linear').fit(X_train, y_train)

# Predict neurotransmitter expression using the test set
y_pred = classifier.predict(X_test)

# Calculate the accuracy of the classifier
acc = accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}%'.format(acc * 100))

# Evaluate the classifier using cross-validation
scores = cross_val_score(classifier, data, labels, cv=5)
print("Cross-Validation Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
