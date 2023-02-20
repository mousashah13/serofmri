# serofmri
## Goal
This Python program utilizes machine learning to predict the type of neurotransmitter expressed in fMRI data by analyzing changes in blood flow. The program uses algorithms such as decision trees, random forests, and neural networks to analyze the data and make predictions. The program is trained on a dataset of fMRI data and corresponding neurotransmitter information to accurately identify patterns and relationships.

## Concept
Change in blood flow in a fMRI scan can indicate the presence of certain neurotransmitters as blood flow is tightly regulated by the neurovascular system, which responds to changes in neuronal activity. The neurovascular system increases blood flow to areas of the brain that are more active, which is detected by fMRI as an increase in signal intensity.

Different neurotransmitters have distinct effects on the neurovascular system and can therefore be associated with specific patterns of blood flow changes in the brain. For example, the release of the neurotransmitter dopamine can lead to vasodilation, causing an increase in blood flow to certain areas of the brain, while the release of the neurotransmitter serotonin can lead to vasoconstriction, causing a decrease in blood flow.

By analyzing the changes in blood flow in a fMRI scan, machine learning algorithms can identify patterns that correspond to specific neurotransmitters, allowing the prediction of the type of neurotransmitter expressed in the brain.

##Pre-processing data
The raw fMRI data underwent pre-processing using the Statistical Parametric Mapping toolbox (SPM-12) in MATLAB, which involved a series of operations to obtain denoised fMRI data. The data was first converted from DICOM format to the standard neuro imaging format (.nii or Nifti). Slice time realignment was then performed to ensure that the data was acquired simultaneously and normalized with the acquisition time. Next, realign and estimate operations were used to correct for translational and rotational motion and generate a mean image, which was used to set the origin based on standard brain anatomy configurations. Finally, co-registration of structural and functional brain images was performed to compensate for the high temporal resolution and low spatial resolution of fMRI data.
