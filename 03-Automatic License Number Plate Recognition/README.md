![project3](auto.jpg)  
The original code : https://techvidvan.com/tutorials/download-automatic-license-number-plate-recognition-project-source-code/  
Automatic License Number Plate Recognition using Deep Learning offers several significant benefits, particularly in the context of law enforcement, traffic management, and security.  
  
The techniques utilized with the powerful OpenCV are:
1) Gaussian Blur to smooth the image.  
2) Sobel to detect edges in the horizontal direction.  
3) Morphological operation (Closing) to fill small gaps in the binary image.  
4) Contour detection to find contours in the thresholded image.  
Additionally, in the Jupyter notebook with Tesseract OCR, I can extract the text from the plate.  
The Python GUI file gives us the opportunity to easily upload an image, extract the plate from it, and save the extracted image as a result.png file.  
  
In this project i used the following libraries:  
--> Opencv  
--> Pytesseract  
--> Numpy  
--> PIL   
--> tkinter  (in oreder to show the algorithm in graphical window so you can upload your prefered image and then click to extract the plate from the original image ) . 
