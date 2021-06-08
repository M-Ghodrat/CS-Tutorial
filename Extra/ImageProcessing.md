Image - Deep Learning

Problems:
- Classification
- Segmentation (pixel-level classification)
- Object detection
- Image to image 

Preprocessing --> not much, maybe increase the contrast

Main problem --> train

Issues:
- overfit
- underfit
- bias
-variance

read these:
U-Net, Rez-Net (classification), Residual block, transfer learning

batch size, kernel size (for high-detail images)

Data augmentation: Flip, Rotate --> this make the algorithm robust

Imbalance --> play with Loss, better way is to give them more weight

Loss --> Cross-entropy

Other things:

Reading data is batch-batch due to to the big size of data

Network: 
- discriminator ---> classification
- generator ---> generate human pictures

should know classic methods 
-pca
-svm
that are used for image, too

---------------------------

Circle's Interview:
- ML concepts
- what are the losses?
- what are the metrics? e.g., what metrics are used for segmentation?
- what is regualarization?
- what do you do in the case of overfit/underfit?
- what is dropout?
- what do you do when you have saturation in the learning curve? 
- what is precision recall curve?
- auto encoders?

---------------------------

Deep Learning --> MIT --> online book
deeplearningbook.org
