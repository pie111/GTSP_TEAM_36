import os
path =os.chdir("C:\\Users\\KURUR MANA\\Desktop\\dataset\\Non_emergency_vehicles")

i=0
for file in os.listdir(path):
    new_file_name="{}.wav".format(i)
    os.rename(file,new_file_name)
    i=i+1
