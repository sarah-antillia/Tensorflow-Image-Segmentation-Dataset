# Tensorflow-Image-Segmentation-Dataset
Tensorflow Image Segmentation Dataset

<h2> Segmentation Data Collection (2023/11/11) </h2>
We have the following dataset.<br>

<li><a href="./dataset/ALL">ALL</a></li>
<li><a href="./dataset/BrainTumor">BrainTumor</a></li>
<li><a href="./dataset/Breast-Cancer">Brest-Cancer</a></li>
<li><a href="./dataset/CervicalCancer">CervicalCancer</a></li>
<li><a href="./dataset/GastrointestinalPolyp">GastrointestinalPolyp</a></li>
<li><a href="./dataset/Lung">Lung</a></li>
<li><a href="./dataset/Mammogram">Mammogram</a></li>
<li><a href="./dataset/MultipleMyeloma">MultipleMyeloma</a></li>
<li><a href="./dataset/Nerve">Nerve</a></li>
<li><a href="./dataset/Ovarian-Tumor">Ovarian-Tumor</a></li>
<li><a href="./dataset/Pap-Smear">Pap-Smear</a></li>
<li><a href="./dataset/Retinal-Vessel">Retinal-Vessel</a></li>
<br>

We appreciate all contributions of these dataset providers.<a href="#100">Dataset citations</a><br>

<br>
<h2>
<a id="100">
Dataset citations
</a>
</h2>
<h3></h3>

<b>1. <a href="./dataset/ALL">ALL</a></b><br>
<pre>
Acute Lymphoblastic Leukemia (ALL) image dataset
https://www.kaggle.com/datasets/mehradaria/leukemia
</pre>
<pre>
If you use this dataset in your research, please credit the authors.
Data Citation:
Mehrad Aria, Mustafa Ghaderzadeh, Davood Bashash, Hassan Abolghasemi, Farkhondeh Asadi, 
and Azamossadat Hosseini, “Acute Lymphoblastic Leukemia (ALL) image dataset.” Kaggle, 
(2021). DOI: 10.34740/KAGGLE/DSV/2175623.

Publication Citation:
Ghaderzadeh, M, Aria, M, Hosseini, A, Asadi, F, Bashash, D, Abolghasemi, 
H. A fast and efficient CNN model for B-ALL diagnosis and its subtypes 
classification using peripheral blood smear images. Int J Intell Syst. 2022; 37: 5113- 5133. doi:10.1002/int.22753
</pre>

<b>2. <a href="./dataset/BrainTumor">BrainTumor</a></b><br>
<pre>
Brain MRI segmentation
https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation
</pre>
<pre>
LGG Segmentation Dataset<br>
Dataset used in:<br>

Mateusz Buda, AshirbaniSaha, Maciej A. Mazurowski "Association of genomic subtypes of 
lower-grade gliomas with shape features automatically extracted by a deep learning 
algorithm." Computers in Biology and Medicine, 2019.
and
Maciej A. Mazurowski, Kal Clark, Nicholas M. Czarnek, Parisa Shamsesfandabadi, 
Katherine B. Peters, Ashirbani Saha "Radiogenomics of lower-grade glioma: 
algorithmically-assessed tumor shape is associated with tumor genomic subtypes 
and patient outcomes in a multi-institutional study with 
The Cancer Genome Atlas data." Journal of Neuro-Oncology, 2017.

This dataset contains brain MR images together with manual FLAIR abnormality 
segmentation masks.
The images were obtained from The Cancer Imaging Archive (TCIA).
They correspond to 110 patients included in The Cancer Genome Atlas (TCGA) 
lower-grade glioma collection with at least fluid-attenuated inversion recovery (FLAIR) 
sequence and genomic cluster data available.
Tumor genomic clusters and patient data is provided in data.csv file.
</pre>

<b>3. <a href="./dataset/CervicalCancer">CervicalCancer</a></b><br>
<pre>
Cervical Cancer largest dataset (SipakMed)
https://www.kaggle.com/datasets/prahladmehandiratta/cervical-cancer-largest-dataset-sipakmed
</pre>
<b>About Dataset</b><br>
<pre>
Please don't forget to upvote if you find this useful.
Context
Cervical cancer is the fourth most common cancer among women in the world, estimated more than 0.53 million 
women are diagnosed in every year but more than 0.28 million women’s lives are taken by cervical cancer 
in every years . Detection of the cervical cancer cell has played a very important role in clinical practice.

Content
The SIPaKMeD Database consists of 4049 images of isolated cells that have been manually cropped from 966 cluster
 cell images of Pap smear slides. These images were acquired through a CCD camera adapted to an optical microscope. 
 The cell images are divided into five categories containing normal, abnormal and benign cells.

Acknowledgements
IEEE International Conference on Image Processing (ICIP) 2018, Athens, Greece, 7-10 October 2018.

Inspiration
CERVICAL Cancer is an increasing health problem and an important cause of mortality in women worldwide. 
Cervical cancer is a cancer is grow in the tissue of the cervix . It is due to the abnormal growth of cell that 
are spread to the other part of the body.
Automatic detection technique are used for cervical abnormality to detect Precancerous cell or cancerous cell 
than no pathologist are required for manually detection process.
</pre>

<b>4. <a href="./dataset/GastrointestinalPolyp">GastrointestinalPolyp</a></b><br>
<pre>
Kvasir-SEG Data (Polyp segmentation & detection)
https://www.kaggle.com/datasets/debeshjha1/kvasirseg
</pre>

<b>5. <a href="./dataset/Mammogram">Mammogram</a></b><br>
<pre>
http://www.eng.usf.edu/cvprg/mammography/database.html
</pre>
<pre>
# Digital Database for Screening Mammography segmentation annotation data
The images files in this directory are 66 Digital Database for Screening Mammography (DDSM) 
mammograms and the corresponding manual annotations of mammograms which show
the fibroglandular, adipose, and pectoral muscle tissue regions. To our knowledge, the dataset 
is the first publicly available breast tissue segmentation masks for screen film mammography 
in the world. The permission for the use of DDSM data is explained in our paper.
The dataset includes manual annotations for 16 Type A, 20 Type B, 17 Type C, and 13 Type D mammograms. 
Manual annotation file names are the original mammogram file name
concatenated with “_LI”, which stands for “labelled image”. Mammograms and the manual annotations have
a resolution of 960x480. 64, 128, 192, and 255 intensity pixels in the manual annotations show background, 
adipose tissue, fibroglandular tissue, and pectoral muscle
tissue regions, respectively. The images are grayscale. Mammograms and manual annotations  are located 
under "fgt_seg" and "fgt_seg_labels" subdirectories of
"train_valid" and "test" directories. These are the training, validation, and test mammograms that were 
used for modelling the mammogram segmentation in our article. We
have given the names of the cross-validation file names in the supplementary materials document. 
You may find the methods about preprocessing of mammograms and manual
annotations in our journal article.
</pre>

<b>6. <a href="./dataset/MultipleMyeloma">MultipleMyeloma</a></b><br>
<pre>
SegPC-2021: Segmentation of Multiple Myeloma Plasma Cells in Microscopic Images
https://www.kaggle.com/datasets/sbilab/segpc2021dataset
</pre>
Citation:<br>
<pre>
Anubha Gupta, Ritu Gupta, Shiv Gehlot, Shubham Goswami, April 29, 2021, "SegPC-2021: Segmentation of Multiple Myeloma Plasma Cells 
in Microscopic Images", IEEE Dataport, doi: https://dx.doi.org/10.21227/7np1-2q42.
BibTex
@data{segpc2021,
doi = {10.21227/7np1-2q42},
url = {https://dx.doi.org/10.21227/7np1-2q42},
author = {Anubha Gupta; Ritu Gupta; Shiv Gehlot; Shubham Goswami },
publisher = {IEEE Dataport},
title = {SegPC-2021: Segmentation of Multiple Myeloma Plasma Cells in Microscopic Images},
year = {2021} }
IMPORTANT:
If you use this dataset, please cite below publications-
1. Anubha Gupta, Rahul Duggal, Shiv Gehlot, Ritu Gupta, Anvit Mangal, Lalit Kumar, Nisarg Thakkar, and Devprakash Satpathy, 
 "GCTI-SN: Geometry-Inspired Chemical and Tissue Invariant Stain Normalization of Microscopic Medical Images," 
 Medical Image Analysis, vol. 65, Oct 2020. DOI: 
 (2020 IF: 11.148)
2. Shiv Gehlot, Anubha Gupta and Ritu Gupta, 
 "EDNFC-Net: Convolutional Neural Network with Nested Feature Concatenation for Nuclei-Instance Segmentation,"
 ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 
 Barcelona, Spain, 2020, pp. 1389-1393.
3. Anubha Gupta, Pramit Mallick, Ojaswa Sharma, Ritu Gupta, and Rahul Duggal, 
 "PCSeg: Color model driven probabilistic multiphase level set based tool for plasma cell segmentation in multiple myeloma," 
 PLoS ONE 13(12): e0207908, Dec 2018. DOI: 10.1371/journal.pone.0207908
License
CC BY-NC-SA 4.0
</pre>

<b>7. <a href="./dataset/Nerve">Nerve</a></b><br>
<pre>
 Ultrasound Nerve Segmentation<br>
 Identify nerve structures in ultrasound images of the neck<br>
</pre>

<pre>
Dataset Description
The task in this competition is to segment a collection of nerves called the Brachial Plexus (BP) in ultrasound images. 
You are provided with a large training set of images where the nerve has been manually annotated by humans. 
Annotators were trained by experts and instructed to annotate images where they felt confident about the existence of 
the BP landmark.

Please note these important points:

The dataset contains images where the BP is not present. Your algorithm should predict no pixel values in these cases.
As with all human-labeled data, you should expect to find noise, artifacts, and potential mistakes in the ground truth. 
Any individual mistakes (not affecting the broader integrity of the competition) will be left as is.
Due to the way the acquisition machine generates image frames, you may find identical images or very similar images.
In order to reduce the submission file sizes, this competition uses run-length encoding (RLE) on the pixel values. 
The details of how to use RLE are described on the 'Evaluation' page.
File descriptions
/train/ contains the training set images, named according to subject_imageNum.tif. Every image with the same subject 
number comes from the same person. This folder also includes binary mask images showing the BP segmentations.
/test/ contains the test set images, named according to imageNum.tif. You must predict the BP segmentation for these 
images and are not provided a subject number. There is no overlap between the subjects in the training and test sets.
train_masks.csv gives the training image masks in run-length encoded format. This is provided as a convenience to 
demonstrate how to turn image masks into encoded text values for submission.
sample_submission.csv shows the correct submission file format.
</pre>

<b>8. <a href="./dataset/Retinal-Vessel">Retinal-Vessel</a></b></br>
<pre>
Retinal Image Analysis
</pre>
<pre>
https://blogs.kingston.ac.uk/retinal/chasedb1/
</pre>

<b>9. <a href="./dataset/Pap-Smearl">Pap-Smear</a></b></br>
<b>PAP-SMEAR (DTU/HERLEV) DATABASES & RELATED STUDIES</b><br>
<pre>
https://mde-lab.aegean.gr/index.php/downloads/
Part II : smear2005.zip [85.17 MB] New Pap-smear Database (images)
This is the new website that hosts the DTU/Herlev Pap Smear Databases, as well as selected studies and papers 
related to these data. For more than 10 years, Dr Jan Jantzen works on pap-smear data acquired from images of 
healthy & cancerous smears coming from the Herlev University Hospital (Denmark), thanks to Dr MD Beth Bjerregaard.
The Old Pap Smear Database was formed in the late 90’s while the New Pap Smear Database (improved) was formed 
within 2005. The analysis of these databases was made through several Master Theses most of which where elaborated 
in Denmark, under the supervision of Dr Jantzen, while he was joining DTU, Dept. of Automation (Denmark) and also 
through collaboration to other researchers from around the world, many of which were made with G.Dounias and his
research team of the MDE-Lab, University of the Aegean. During the last years, Dr Jantzen collaborates with the 
University of the Aegean, Dept. of Financial and Management Engineering (FME) as teaching associate of the 
Postgraduate Program of the FME-Dept. and as research associate of the MDE-Lab. The site will be continuously 
updated with new papers, studies, theses and citations related to the hosted pap-smear databases.
</pre>

<b>10. <a href="./dataset/Ovarina-Tumor">Ovarian-Tumor</a></b></br>
The original image dataset OTU_2d used here has been taken from the following google drive.<br>
<a href="https://drive.google.com/drive/folders/1c5n0fVKrM9-SZE1kacTXPt1pt844iAs1">MMOTU</a><br>

<pre>
MMOTU_DS2Net
https://github.com/cv516Buaa/MMOTU_DS2Net
Dataset
Multi-Modality Ovarian Tumor Ultrasound (MMOTU) image dataset consists of two sub-sets with two modalities, 
which are OTU_2d and OTU_CEUS respectively including 1469 2d ultrasound images and 170 CEUS images. 
On both of these two sub-sets, we provide pixel-wise semantic annotations and global-wise category annotations. 
Many thanks to Department of Gynecology and Obstetrics, Beijing Shijitan Hospital, 
Capital Medical University and their excellent works on collecting and annotating the data.
</pre>

<b>11. <a href="./dataset/Lung">Lung</a></b></br>
<pre>
Chest Xray Masks and Labels
https://www.kaggle.com/datasets/nikhilpandey360/chest-xray-masks-and-labels
</pre>
<pre>
The dataset contains x-rays and corresponding masks. Some masks are missing so it is advised 
to cross-reference the images and masks.
Original Dataset before modification
The OP had the following request:
It is requested that publications resulting from the use of this data attribute the source 
(National Library of Medicine, National 
Institutes of Health, Bethesda, MD, USA and Shenzhen No.3 People窶冱 Hospital, Guangdong Medical
 College, Shenzhen, China) and cite 
the following publications:
Jaeger S, Karargyris A, Candemir S, Folio L, Siegelman J, Callaghan F, Xue Z, Palaniappan K, 
Singh RK, Antani S, Thoma G, Wang YX, 
Lu PX, McDonald CJ. Automatic tuberculosis screening using chest radiographs. 
IEEE Trans Med Imaging. 2014 Feb;33(2):233-45. doi: 10.1109/TMI.2013.2284099. PMID: 24108713
Candemir S, Jaeger S, Palaniappan K, Musco JP, Singh RK, Xue Z, Karargyris A, Antani S, Thoma G, McDonald CJ. 
Lung segmentation in chest radiographs using anatomical atlases with nonrigid registration. 
IEEE Trans Med Imaging. 2014 Feb;33(2):577-90. doi: 10.1109/TMI.2013.2290491. PMID: 24239990
Montgomery County X-ray Set
X-ray images in this data set have been acquired from the tuberculosis control program of the 
Department of Health and Human Services 
of Montgomery County, MD, USA. This set contains 138 posterior-anterior x-rays, of which 80 
x-rays are normal and 58 x-rays are abnormal
 with manifestations of tuberculosis. All images are de-identified and available in DICOM format. 
The set covers a wide range of 
 abnormalities, including effusions and miliary patterns. The data set includes radiology 
readings available as a text file.
Ideas
Experiment with lung segmentation
Build disease classifiers for various conditions
Test models on data across different manufacturers
Build GANs that are able to make the datasets indistinguishable 
(Adversarial Discriminative Domain Adaptation: https://arxiv.org/abs/1702.05464)
</pre>
<b>License</b><br>
CC0: Public Domain
<br>


