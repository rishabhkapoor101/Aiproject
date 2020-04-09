import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')



cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h+10),(0,0,500),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 

    cv2.imshow('img',img)#to project image from webcam to screne
    k = cv2.waitKey(30)#program will stop on pressing escape 
    if k == 27:
        break

cap.release() #to release control of opencv over webcam
cv2.destroyAllWindows()# to close webcam window



# Sir, the code is just a explanation and not a formal report…

# Libraries used:  cv2 from opencv for the program to run please install “opencv”.

# I have used haarcascade by intel link: - https://github.com/opencv/opencv/tree/master/data/haarcascades

# Hear we can find various “.xml” files for different object detections and all. I have used two of them 
# 1.	Frontal face.     2. Eye.

# The thing I found weird about opencv is that for colours the parameters are 
# as “B G R” and not as ”R G B” 

# basically opencv gives us the starting and ending coordinates of the object in discussion and then we use those coordinates to draw different shapes.  Like : circle, rectangle and even a pentagone…
# cv2.rectangle(img,(x,y),(x+w,y+h+10),(0,0,500),2)

# in above line img is the live feed from the web cam that we were capturing in cap and when we entered while loop we assigned it to img…  (x,y) are the starting coordinates of the face w is width and h is hight and (x+w,y+h+10) are ending coordinates… and 2 here is the line width…

# we can create a circle as well but the (x,y) will be then the coordinates of the center of the face and (x+w,y+h+10) will be replaced with the radius as we please…and line width remains unchanged.
# THANKS SIR.                       
# Regards.
# Yours obediently,
# Rishabh kapoor.

