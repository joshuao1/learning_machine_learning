import numpy as np
from PIL import Image
import os
import csv

directory = "C:/Users/josho/Development/GitHub/learning_machine_learning/small_img"
output = []

for filename in os.listdir(directory):
    img = np.asarray(Image.open(directory + "/"+ filename))
    output.append(img)

first_file = output[0]
#print(type(first_file))
# summarize shape
#print(first_file.shape)
#np.savetxt("output.csv", first_file, delimiter=",")

with open('output.csv','a', newline='') as fd:
   writer = csv.writer(fd, delimiter=',')
   writer.writerow(first_file)