import os
import sys
import argparse
import random
import re

img_filenames = []
txt_filenames = []

if (len(sys.argv) < 2):
    print "Argument required: Enter path for input data"
    sys.exit(0)
elif (len(sys.argv) > 2):
    print "Input arguments more than 1 not valid!"
    sys.exit(0)
imgdir=sys.argv[1]
testFilename = imgdir+"test.txt"
trainFilename = imgdir+"train.txt"
for root, dirs, files in os.walk(imgdir):
    for file in files:
        if file.endswith(".jpg"):
            img_filenames.append(file)
            #print(os.path.join(root, file))
        if file.endswith(".txt"):
            txtFileName = file
            if '.xml' in txtFileName:
                #In case .txt file name contains .xml after image name, remove it!
                txtFileName = txtFileName.replace('.xml','')
                print txtFileName
                os.rename(root+'/'+file, root+'/'+txtFileName)
print ("Total files: %d"%len(img_filenames))
# Shuffle all images in the filename list
img_filenames.sort()
random.seed(230)
random.shuffle(img_filenames)
# Split images for Train / Test with 80:20 ratio
split_a = int(0.8 * len(img_filenames))
#split_b = int(0.9 * len(filenames))
train_files = img_filenames[:split_a]
#dev_filenames = filenames[split_a:split_b]
test_files = img_filenames[split_a:]
#print ("Train files: %d"%len(train_files))
#print train_files
#print ("Test files: %d"%len(test_files))
#print test_files
filenames = {'train': train_files,
             'test': test_files}
with open(trainFilename, "w") as f:
   for img_filename in train_files:
        f.write(imgdir+'images/'+img_filename+'\r\n')
with open(testFilename, "w") as f:
   for img_filename in test_files:
        f.write(imgdir+'images/'+img_filename+'\r\n')
print "Done!"
print "Train files listed in "+trainFilename
print "Test files listed in "+testFilename

