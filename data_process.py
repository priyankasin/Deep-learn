# Seprate group of data based on class 
# label of data contain in CSV file


from PIL import Image, ImageDraw
import numpy as np
from numpy import genfromtxt
import os
import scipy.misc
import csv
import pandas as pd
import os
import shutil


 = open('/home/priyanka/Pictures/Classification_tensorflow/trainLabels.csv','r')
dst='train_data'
src='/home/priyanka/Pictures/Classification_tensorflow/train'
data = pd.read_csv(g, sep = ",")
# print(data)
print(data.label[data.id==4])


i=1
for img in os.listdir(os.path.join(src)):
	print(img)

	label_id=img[:-4]
	label_id=list(data.label[data.id==int(label_id)-1])
	print(label_id)
	label_id=label_id[0]
	print(label_id)

	file_name = os. path . join (dst,label_id,str(i)+'.jpg')
	subject_path= os. path . join (dst,label_id)
	print(subject_path)
	if not os.path.exists(subject_path):
		os.makedirs(subject_path)

	path_file = os.path.join(src,img)
	print(path_file)
	
	shutil.copy2(path_file,subject_path)
	print('data save')
	  
	i=i+1

