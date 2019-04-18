import os
from PIL import Image
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
dataDirectory = './leapgestrecog/leapGestRecog/'
output_left = './data/test/'
output_right = './data/train/'


subdirs = [x[0] for x in os.walk(dataDirectory)]
"""
1600 Train
400 Test
"""
counter = 0

#Find all the L pictures
for folder in subdirs:
    if "02_l" in folder:
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            path = folder + '/' + filename

            picture= Image.open(path)

            #Flip and save left 
            left_image = picture.rotate(90, expand=True)
            if ("_08_" in path or "_09_" in path):
                left_image.save('data/test/left/' + filename)
            else:
                left_image.save('data/train/left/' + filename)

            #Flip and save right
            right_image = left_image.transpose(Image.FLIP_LEFT_RIGHT)

            if ("_08_" in path or "_09_" in path):
                right_image.save('data/test/right/' + filename)
            else:
                right_image.save('data/train/right/' + filename)

  

