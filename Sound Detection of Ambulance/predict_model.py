
import tkinter as tk
import keras.models
import time
import winsound
import json
import numpy as np
import tensorflow.keras as keras

DATA_PATH="recordings.json"
model = keras.models.load_model('saved_model')

def load_data(data_path):
    with open (data_path,"r")as fp:
        data=json.load(fp)

    x = np.array(data["mfcc"])
    y = np.array(data["labels"])

    return x, y

def prepare_dataset():
    x,y=load_data(DATA_PATH)

    x= x[..., np.newaxis]

    return x,y

def popupmsg(msg, title):

    root = tk.Tk()
  #  root.after(4000, lambda: root.destroy())
    root.title(title)
    root.geometry('400x240')
    label = tk.Label(root, text=msg,bg='black',fg='red')
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 3000  # Set Duration To 1000 ms == 1 second
    B1.pack()
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
   # winsound.Beep(frequency, duration)

    root.mainloop()





def predict(model, x, y):
    # add a dimension to input data for sample - model.predict() expects a 4d array in this case
    x = x[np.newaxis, ...] # array shape (1, 130, 13, 1)

    # perform prediction
    prediction = model.predict(x)

    # get index with max value
    predicted_index = np.argmax(prediction, axis=1)

    print(predicted_index)
    if predicted_index==[0]:
        print('EMERGENCY VEHICLE')

        popupmsg('EMERGENCY SOUND','SIREN DETECTOR')

    else:
        print('NON-EMERGENCY VEHICLE')

if __name__=='__main__':

    x,y= prepare_dataset()
    x_to_predict = x[0]
    y_to_predict = y[0]


    popupmsg('test', 'SR')
    predict(model,x_to_predict,y_to_predict)


