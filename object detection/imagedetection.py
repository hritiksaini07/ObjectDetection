import cv2
from matplotlib import pyplot as plt

#opening image
image=cv2.imread("image.jpg")

#converting BRG image to RGB and grayscale version
img_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img_rgb= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

  #use minSize because for not
#bothering with extra small
#dots that would look like STOP SIGNS

found=stop_data.detectMultiScale(img_gray,minSize=(20,20))

#don't do anything if there's
#no sign

amount_found=len(found)

if amount_found !=0:
    #there may be more than one sign in the image
    for (x,y,width,height) in found:
        #draw green rectangle around every recognized sign
        cv2.rectangle(img_rgb,(x,y),(x+height,y+width),(0,255,0),5)


#creating enviornment of the picture and displaying it
plt.subplot(1,1,1)
plt.imshow(img_rgb)
plt.show()









        
