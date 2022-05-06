import time
from record_sound import *
from sound_prepro import *
from predict_model import *
#predict_model.popupmsg.root.destroy()
while __name__=='__main__':
    record()
    save_mfcc(DATA_SETPATH, JSON_PATH, num_segments=1)
    x,y= prepare_dataset()
    x_to_predict = x[0]
    y_to_predict = y[0]

    predict(model,x_to_predict,y_to_predict)





