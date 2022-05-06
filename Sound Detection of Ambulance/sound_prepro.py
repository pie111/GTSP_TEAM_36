import os
import librosa
import math
import json
import numpy as np



DATA_SETPATH="recordings"
JSON_PATH="recordings.json"
SAMPLE_RATE=22050
DURATION=3
SAMPLES_PER_TRACK=SAMPLE_RATE*DURATION


def save_mfcc(dataset_path,json_path,n_mfcc=13,n_fft=2048,hop_length=512,num_segments=1):
    data={
        "mapping":[],
        "mfcc":[],
        "labels":[]

    }
    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length)

    for i,(dirpath,dirnames,filenames)in enumerate(os.walk(dataset_path)):
        if dirpath is not dataset_path:

            dirpath_components=dirpath.split("/")
            semantic_label=dirpath_components[-1]
            data["mapping"].append(semantic_label)
           # print("\nProcessing {}".format(semantic_label))

        for f in filenames:
            file_path=os.path.join(dirpath,f)
            signal,sr=librosa.load(file_path,sr=SAMPLE_RATE)

            mfcc=librosa.feature.mfcc(signal,
                                          sr=sr,
                                          n_fft=n_fft,
                                          n_mfcc=n_mfcc,
                                          hop_length=hop_length)

            mfcc=mfcc.T

            if len(mfcc)==expected_num_mfcc_vectors_per_segment:
                data["mfcc"].append(mfcc.tolist())
                data["labels"].append(i-1)

                print("{} ".format(file_path))

    with open(json_path,"w")as fp:
        json.dump(data,fp,indent=4)

#if __name__=='__main__':
  #  save_mfcc(DATA_SETPATH,JSON_PATH,num_segments=1)






