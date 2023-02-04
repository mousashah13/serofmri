import numpy as np
import nibabel as nib
from nilearn import image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


img = nib.load('preprocessed_fmri_data.nii')
data = img.get_fdata()


design_matrix = np.zeros((data.shape[3], 2))
design_matrix[:, 0] = 1
design_matrix[:, 1] = np.arange(data.shape[3])

estimated_flows = np.zeros(data.shape[:3])
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            voxel_data = data[i, j, k, :]
            model = LinearRegression(fit_intercept=False).fit(design_matrix, voxel_data)
            estimated_flows[i, j, k] = model.coef_[1]

new_img = nib.Nifti1Image(estimated_flows, img.affine)
nib.save(new_img, 'estimated_flows.nii')

img = nib.load('estimated_flows.nii')
data = img.get_fdata()
data = np.reshape(data, (np.prod(data.shape[:3]), 1))

labels = np.zeros(data.shape[0])
labels[data < 0] = 0 # low values correspond to serotonin
labels[data >= 0] = 1 # high values correspond to dopamine


X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=0)

classifier = LogisticRegression(solver='lbfgs').fit(X_train, y_train)

y_pred = classifier.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}%'.format(acc * 100))
