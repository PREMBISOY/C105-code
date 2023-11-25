import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
h,w,channels = frame.shape
size = (w,h)
print(size)
#out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)
#out.release()