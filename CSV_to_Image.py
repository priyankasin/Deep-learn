from PIL import Image, ImageDraw
import numpy as np
from numpy import genfromtxt
import os
import scipy.misc

print("Start.....")
g = open('mnist_train.csv','r')
dst='train/'
print(g)
temp = genfromtxt(g, delimiter = ',')
print(temp)
# print(temp)
# temp=temp[1:]
count=1
for img in temp:
	# if count ==1:
	label=img[0]
	img=img[1:]
	i=0
	new_list=[]
	while i<len(img):
	  new_list.append(img[i:i+28])
	  i+=28
	  
	# print(new_list)
	new_list=np.array(new_list)
	# print(new_list)
	# im = Image.fromarray(new_list).convert('RGB')
	# print()
	# pix = im.load()
	# rows, cols = im.size
	# print(rows,cols)
	# print(label	)

	# for x in range(cols):
	#     for y in range(rows):
	#         # print str(x) + " " + str(y)
	#         pix[x,y] = (int(temp[y,x] // 256 // 256 % 256),int(temp[y,x] // 256  % 256),int(temp[y,x] % 256))
	file_name = os. path . join ( dst,str(label),str(count)+'.jpg')
	subject_path= os. path . join ( dst,str(label))
	if not os.path.exists(subject_path):
		os.makedirs(subject_path)
	# im.save(file_name)
	
	scipy.misc.imsave(file_name,new_list)
	count+=1