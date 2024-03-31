import os
import cv2

path = "C:/Users/akshajaryash/Desktop/C105 Project/Images"
imagesList = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print("NAME OF THE FILE IN CURRENT ITERATION:  ",file_name)
        imagesList.append(file_name)
count = len(imagesList)
print("total number of images in imagesList: ",count)
frame = cv2.imread(imagesList[0])
height, width, channels = frame.shape
size = (width,height)
print("SIZE of a single image from the imagesList as a reference: ",size)
vidOUTPUT = cv2.VideoWriter('y7artworkgallery.mp4v',cv2.VideoWriter_fourcc(*'DIVX'), 0.5, size)
for i in range(count-1,0,-1):
    frame = cv2.imread(imagesList[i])
    vidOUTPUT.write(frame)
vidOUTPUT.release() 
print("Done!!!")


