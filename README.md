# AMBULANCE ALERT SYSTEM
An ambulance alert system that alerts the drivers in the traffic beforehand to enable route clearance for the ambulance.
## Problem Statement
The massive traffic jams in our country restricts the  easy movement of ambulances depriving the patients with emergency medical care thus risking their lives and denying immediate medical care.The need of the hour is a smart notification system that can  alert the drivers in the traffic beforehand to enable the route clearance for the ambulance.

## Solution
An advanced notification system to alert the drivers when the ambulance is at a vicinity of 3-4 KM enabling them to clear route for the ambulance.The system monitors the traffic and detect traffic congestions  and manage them for the emergency route clearance.A display monitor at traffic intersection delivers a notification about the location of the ambulance along with a hardware unit embedded on vehicles with a buzer to alert the driver about the proximity of ambulance.

# Workflow
![architecture](https://user-images.githubusercontent.com/48887731/167126122-583a5b0d-66b5-4716-b05d-f1298a46bfc5.jpeg)

An ambulance driver sets the location with the start and destination points before commencing the journey.The location of the ambulance is monitored along with the traffic at vicinity of 3 to 4 km. An alert to drivers in the proximity region is made by the buzzer embedded with the hardware unit.A  monitor at the traffic intersection displays the location of the ambulance (Eg: 500 meters away)to alert the drivers for giving way to ambulance.The notification is also  passed to the traffic contol room for further help from police.

## Implementation Status

The implentation done so far is based on realtime data that could be obtained  from the traffic cameras rather than the hardware unit along with GPS embedded with it.The implemntation is divided in to the following modules:
* Front end UI
* Ambulance detection
* Camera Identification
* Traffic congestion detection


The front end consists of an interface through which an ambulance driver can set the location with the start and destination points before commencing the journey.The ambulance is then detected using either through real time data from camera or the siren sound.
The real time data was used and  CNN Model was trained to predict the presence of ambulance.Video from camera was sampled at an interval of 2 sec to obtain images.The images were then passed on  to the trained model.The model predicts the presence of ambulance and also returns the time at which it was predicted.Ambulance detection was aslo implemented by detecting the sound at a particular range.The sound from the ambulance was processed and converted to spectrum using librosa library in python and it was passed to a CNN model for detection.

The ambulance detection is followed by identifying the cameras and retrieving the position cordinates that comes in range of 4km around the coordinates from where ambulance was detected.A database of all cameras along with their position cordinates was created and mainted.The position coordinates are then retrieved to identify cameras within range of 3 to 4 kms to monitor the traffic and detect congestion.

Two approaches were implemented to detect traffic congestion which included an object detection based approch to find traffic volume and a classification based approach.Efficentnet pretrained classification model was used  for training the model to detect traffic congestion.Object detection using opencv was implemented to keep track of traffic volume and thus predictiong congestion if it exceeds a thresold.


## DEMO

* Traffic congestion detection based on traffic volume :-https://drive.google.com/drive/folders/1dW07yUFWz-3sYH7qy6yNF46WorJNBXJ7?usp=sharing
* Traffic congestion detection based on classification approach:-https://drive.google.com/drive/folders/1rK3pCLns19ZKrTSyZQGoPOe3qwcg_BYX?usp=sharing

## Algorithms Used

### Convolutional neural network
![cnn 1](https://user-images.githubusercontent.com/48887731/167438737-61727e7c-e613-423f-b005-1aea3cbe749e.jpeg)
A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other.The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.
[Read more](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53).




## References:

>1 https://www.researchgate.net/publication/356515102_Ambulance_detection_using_image_processing_and_neural_networks

>2 https://www.ijert.org/emergency-vehicle-detection-by-autonomous-vehicle

>3 https://towardsdatascience.com/covolutional-neural-network-cb0883dd6529

>4 https://ieeexplore.ieee.org/abstract/document/7440510

>5 http://proceedings.mlr.press/v97/tan19a.html


## Contributors
- Anol Joseph, _NSS College of Engineering, Palakkad_
- Maritta Stephen, _NSS College of Engineering, Palakkad_
- Jahfar Swalih, _TKM College of Engineering,Kollam_
- Vyshnav, _NSS College of Engineering, Palakkad_
- Rahul K, _NSS College of Engineering, Palakkad_
- Pranav K S, _NSS College of Engineering, Palakkad_ 
