from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import cv2


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

src='/home/priyanka/Downloads/videoplayback.mp4'
webcam = cv2.VideoCapture(0) 
while True:
    (rval, im) = webcam.read()
    # im=cv2.flip(im,1,0) #Flip to act as a mirror

    # Resize the image to speed up detection
    if im  is None:
        break
    else:
    	# test_image = image.load_img(im, target_size = (64, 64))
    	cv2.imshow("img",im)
    	cv2.waitKey(100)
    	test_image= cv2.resize(im, (64,64))

    	test_image = image.img_to_array(test_image)
    	test_image = np.expand_dims(test_image, axis = 0)
    	result = loaded_model.predict(test_image)
    	if result[0][0] == 1:
    	 prediction = 'dog'
    	else:
    	  prediction = 'cat'
    	print(prediction)
