import numpy as np
import cv2
import functions as funcs

imageName=input()#image_name.jpg
img0= cv2.imread(imageName, 0)
img=funcs.correctRotation(img0)
img1,circles1=funcs.getCircles(img,10,15)
img2,circles2=funcs.getFilledCircles(img,10,15)
circles1 = funcs.arrangeXY(circles1)
circles2 = funcs.arrangeXY(circles2)
gender, semester, program, answers=funcs.scann(circles1,circles2,img)

print(gender)
print(semester)
print(program)
print(answers)

text_file = open("output.txt", "w")
text_file.write("The output of image: "+ imageName +"\n")
text_file.write("\n")
text_file.write("Gender: "+ gender +"\n")
text_file.write("Semester: "+ semester+"\n")
text_file.write("Program: "+ program+"\n")
for i in range(len(answers)):
    text_file.write("answer of Q"+str(i+1)+" is:"+ answers[i]+"\n")
text_file.close()
