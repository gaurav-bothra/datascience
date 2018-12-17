# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import cv2


image1 = cv2.imread("journal1.jpg")
output1_par = image1.copy()

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ret1,th1 = cv2.threshold(gray1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)



def process_par(thresh,output):	
	kernel = np.ones((5,5), 'uint8')	
	par_img = cv2.dilate(thresh,kernel,iterations=3)
	
	(_, contours, _) = cv2.findContours(par_img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	count-0
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		crop_img = output[y:y+h, x:x+w] 
        cv2.imwrite("D:\DataScience\cosc428-structor\layout\document-layout-analysis\output{no}_par.jpg".format(no=count), )
        count = count +1

#processing margin with paragraph boxing
def process_margin(thresh,output):	
	# assign a rectangle kernel size
	kernel = np.ones((20,5), 'uint8')	
	margin_img = cv2.dilate(thresh,kernel,iterations=5)
	
	(_, contours, _) = cv2.findContours(margin_img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),1)

	return output

output1_margin = process_margin(th1,output1_par)


output1_par = process_par(th1,output1_par)
output1_margin = process_margin(th1,output1_par)
plt.imshow(output1_margin)

cv2.imwrite("D:\DataScience\cosc428-structor\layout\document-layout-analysis\output3_par.jpg", output1_margin)
cv2.waitKey(0)
