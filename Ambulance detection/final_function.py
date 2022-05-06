

#This funtion detect the presence of Ambulance and then return the date and time 



from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

#Importing OS for accessing local files
import os
from os import listdir

#OpenCv for imageprocessing
import cv2

#time and data
import datetime 





def Detect_Ambulance(model_path,dir_path,video_path):
    
    MODEL_PATH = model_path
    model = load_model(MODEL_PATH) 
    
    
    def video_to_img(video_path):
        cap= cv2.VideoCapture(video_path)
        i=1
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            if i%50 == 0:
                cv2.imwrite('kang'+str(i)+'.jpg',frame)
            i+=1

        cap.release()
        cv2.destroyAllWindows()    
    
    video_to_img(video_path)
    
    
    
    def model_predict(img_path, model):
        img = image.load_img(img_path, target_size=(200, 200))

        # Preprocessing the image
        x = image.img_to_array(img)
        #x = np.true_divide(x, 255)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x, mode='caffe')
        preds = model.predict(x)
        return preds
    
    flag = 0
    arr = []
    # get the path/directory
    folder_dir = dir_path
    for images in os.listdir(folder_dir):    
        # check if the image ends with jpg
        if (images.endswith(".jpg")):
            arr.append(images)
    for i in arr:
        path = dir_path

        # Join various path components
        path_way = os.path.join(path, "", i)
        prediction_val = model_predict(path_way,model)
        val = prediction_val[0][0]
        if val == 0:
            flag = 1
            current_time = datetime.datetime.now() 
            current_time = str(current_time)
    
    
    
    
    

    if flag == 1:
        return "Detected " + "And data and time = " + current_time
    elif flag == 0:
        return "Not Detected"
    
    






