

#importing required libraries

import pandas as pd
import cv2

#intialising global variables for later use

clicked = False
r = g = b = xpos = ypos = 0

#reading the image from which the colors should be extracted 

image_path = "colorpic.jpg"
image = cv2.imread(image_path)

#reading the csv file containing reference data

index = ['color','color_name','hex','R','G','B']
file_path = "colors.csv"
dataset = pd.read_csv(file_path, names = index, header = None)

#function to get color

def getcolor(R ,G ,B ):
    minimum = 10000
    for i in range(len(dataset)):
        d =abs( R - int(dataset.loc[i ,'R'])) + abs(G - int(dataset.loc[i,'G'])) + abs(B - int(dataset.loc[i, 'B']))
        if d<=minimum:
            minimum = d
            col_name = dataset.loc[i, "color_name"]
    return col_name

#when you click on the image

def draw_func(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

#showing a named window 

cv2.namedWindow('image')
cv2.setMouseCallback("image", draw_func)


while True:

    cv2.imshow('image',image)
    if clicked:
        cv2.rectangle(image, (20, 20),(700,60),(b, g, r), -1)
        text = getcolor(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + 'B=' + str(b)
        cv2.putText(image,text,(50,50), 2, 0.8,(255, 255, 255), 2, cv2.LINE_AA)

        if r +g + b >= 600:
            cv2.putText(image,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()