import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt



DATA_PATH="dataset.json"

def load_data(data_path):
    with open (data_path,"r")as fp:
        data=json.load(fp)

    x=np.array(data["mfcc"])
    y = np.array(data["labels"])

    return x, y

def plot_history(history):

    fig, axs = plt.subplots(2)

    # create accuracy sublpot
    axs[0].plot(history.history["accuracy"], label="train accuracy")
    axs[0].plot(history.history["val_accuracy"], label="test accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy eval")

    # create error sublpot
    axs[1].plot(history.history["loss"], label="train error")
    axs[1].plot(history.history["val_loss"], label="test error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error eval")

    plt.show()


def prepare_dataset(test_size,validation_size):
    x,y=load_data(DATA_PATH)

    x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=test_size)

    x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=validation_size)

    x_train = x_train[..., np.newaxis]
    x_validation = x_validation[..., np.newaxis]
    x_test = x_test[..., np.newaxis]
    print(x_train.shape)

    return x_train, x_validation, x_test, y_train, y_validation, y_test

def build_model(input_shape):

    model=keras.Sequential()

    model.add(keras.layers.Conv2D(32,(3,3),activation="relu",input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((3,3),strides=(2,2),padding="same"))
    model.add(keras.layers.BatchNormalization())

    model.add(keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides=(2, 2), padding="same"))
    model.add(keras.layers.BatchNormalization())

    model.add(keras.layers.Conv2D(32, (2, 2), activation="relu", input_shape=input_shape))
    model.add(keras.layers.MaxPool2D((2, 2), strides=(2, 2), padding="same"))
    model.add(keras.layers.BatchNormalization())

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64,activation="relu"))
    model.add(keras.layers.Dropout(0.5))

    model.add(keras.layers.Dense(2,activation="softmax"))

    return model


def predict(model, x, y):
    # add a dimension to input data for sample - model.predict() expects a 4d array in this case
    x = x[np.newaxis, ...] # array shape (1, 130, 13, 1)

    # perform prediction
    prediction = model.predict(x)

    # get index with max value
    predicted_index = np.argmax(prediction, axis=1)

    print("Target: {}, Predicted label: {}".format(y, predicted_index))
    if predicted_index==0:
        print("Emergency Vehicle")
    else:
        print(("Non-Emergency Vehicle"))

if __name__=='__main__':
    x_train,x_validation,x_test,y_train,y_validation,y_test=prepare_dataset(0.25,0.2)

    input_shape = (x_train.shape[1],x_train.shape[2],x_train.shape[3])
    model=build_model(input_shape)

    optimizer=keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer,
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])


    history=model.fit(x_train,y_train,validation_data=(x_validation,y_validation),epochs=34,batch_size=32)

    plot_history(history)

    test_error,test_accuracy=model.evaluate(x_test,y_test,verbose=1)
    model.save('saved_model/')
    print("Accuracy on test set is {} :".format(test_accuracy))

    # pick a sample to predict from the test set
    x_to_predict = x_test[11]
    y_to_predict = y_test[11]

    # predict sample
    predict(model, x_to_predict, y_to_predict)


