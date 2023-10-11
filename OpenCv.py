#Open Cv
'''
import cv2

#how to read image

img=cv2.imread("me3.jpeg")
cv2.imshow('output image',img)

cv2.waitKey(0)
'''
#################################################
#how to write image
'''
img=cv2.imread("me3.jpeg")
cv2.imwrite('output image',img)

cv2.waitKey(0)
'''
########################################################
#Get image information using OpenCv
'''
img = cv2.imread('me3.jpeg')
print(img.shape)      #(1166, 645, 3) 1.height ,2.width,3.deth
print('height:',img.shape[0])
print('width:',img.shape[1])
print('deth:',img.shape[2])

cv2.waitKey(0)
'''
######################################################
#image roatation using OpenCv
'''
img=cv2.imread('me3.jpeg')
height,width=img.shape[: 2]
rotateimg=cv2.getRotationMatrix2D((width /2, height /2), 70, .5)
finalimg=cv2.warpAffine(img,rotateimg,(width,height))
cv2.imshow('Rotated image', finalimg)
cv2.imshow("original",img)

cv2.waitKey(0)
'''
##########################################
#transfer the image roatate
'''
img=cv2.imread('me3.jpeg')
rotateimg =cv2.transpose(img)

cv2.imshow('transpose',rotateimg)
cv2.imshow('Original', img)

cv2.waitKey(0)
'''
############################
#CAPTURING VIDEO USING OPENCV
'''

video= cv2.VideoCapture(0)   #CAMERA VIEDEO IS OPEN

while True:
    check,frame=video.read()
    cv2.imshow('frame',frame)
    cv2.waitKey(0)
'''
###########################
#HOW TO BLUR IMAGE USING OPENCV
'''
img=cv2.imread('me3.jpeg')
kernel= np.ones((7,7), np.float32) /49
blurred= cv2.filter2D(img,-1,kernel)
cv2.imshow('Blurred',blurred)

cv2.waitKey(0)
'''
##################################
#IMAGE PYRAMID USING OPENCV
'''
img=cv2.imread('me3.jpeg');
smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)

cv2.imshow('Oroginal',img)
cv2.imshow('larger',img)
cv2.imshow('smaller',img)

cv2.waitKey(0)
'''
######################################
#EDGE DETECTION IN OPENCV

#img=cv2.imread('me3.jpeg')
#canny= cv2.Canny(img,20,170)
#cv2.imshow('Canny',canny)

#cv2.waitKey(0)