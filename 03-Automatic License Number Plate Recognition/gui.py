import tkinter as tk
from tkinter import filedialog 
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import PhotoImage
import numpy as np 
import cv2 
import pytesseract as tess

def clean2_plate(plate):
    gray_img = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_img, 110, 255, cv2.THRESH_BINARY)
    if cv2.waitKey(0) & 0xff == ord('q'):
        pass 
    num_contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if num_contours:
        contour_area = [cv2.contourArea(c) for c in num_contours]
        max_cntr_index = np.argmax(contour_area)

        max_cnt = num_contours[max_cntr_index]
        max_cntArea = contour_area[max_cntr_index]
        x, y, w, h = cv2.boundingRect(max_cnt)

        if not ratioCheck(max_cntArea, w, h):
            return plate, None 
    
        final_img = thresh[y:y+h, x:x+w]
        return final_img, [x, y, w, h]
    else:
        return plate, None 
    

def ratioCheck(area, width, height):
    ratio = float(width) / float(height)
    if ratio < 1:
        ratio = 1 / ratio
    if (area < 1063.62 or area > 73862.51) or (ratio < 3 or ratio > 6):
        return False
    return True


def isMaxWhite(plate):
    avg = np.mean(plate)
    if (avg >= 115):
        return True
    else:
        return False
    

def ration_and_rotation(rect):
    (x, y), (width, height), rect_angle = rect
    if (width > height):
        angle = -rect_angle
    else:
        angle = 90 + rect_angle
    if angle > 15:
        return False 
    if height == 0 or width == 0:
        return False
    area = height * width
    if not ratioCheck(area, width, height):
        return False 
    else:
        return True 
    

top = tk.Tk()
top.geometry('900x700')
top.title('Number Plate Recognition')
#top.iconphoto(True, PhotoImage(file="logo.png"))
img = ImageTk.PhotoImage(Image.open('logo.png'))
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 35, 'bold'))
sign_image = Label(top, bd=0)
plate_image = Label(top, bd=100)

def classify(file_path):
    try:
        res_text = None
        img = cv2.imread(file_path)
        img2 = cv2.GaussianBlur(img, (3, 3), 0)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        img2 = cv2.Sobel(img2, cv2.CV_8U, 1, 0, ksize=3)
        _, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(17, 3))
        morph_img_threshold = img2.copy()
        cv2.morphologyEx(src=img2, op=cv2.MORPH_CLOSE, kernel=element, dst=morph_img_threshold)
        num_contours, hierarchy = cv2.findContours(morph_img_threshold, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(img2, num_contours, -1, (0, 255, 0), 1)

        for i, cnt in enumerate(num_contours):
            min_rect = cv2.minAreaRect(cnt)

            if ration_and_rotation(min_rect):
                x, y, w, h = cv2.boundingRect(cnt)
                plate_img = img[y:y+h, x:x+w]
                cv2.imwrite('resultat.png', plate_img)

                if isMaxWhite(plate_img):
                    clean_plate, rect = clean2_plate(plate_img)
                    if rect:
                        x1, y1, w1, h1 = rect
                        x, y, w, h = x + x1, y + y1, w1, h1
                        plate_im = Image.fromarray(clean_plate)
                        text = tess.image_to_string(plate_im, lang='eng')
                        res_text = text.strip()
                        break

        if res_text:
            label.configure(foreground='#011638', text=f"Plate: {res_text}")
            uploaded = Image.open('resultat.png')
            im = ImageTk.PhotoImage(uploaded)
            plate_image.configure(image=im)
            plate_image.image = im
            plate_image.pack()
            plate_image.place(x=560, y=320)
        else:
            label.configure(foreground='#011638', text="")  # Clear the label if no plate is detected

    except Exception:
        label.configure(foreground='#011638', text="")  # Clear the label on error


def show_classify_button(file_path):
    classify_b = Button(top, text='Extract the plate', command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 15, 'bold'))
    classify_b.place(x=20, y=500)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text=' ')
        show_classify_button(file_path)
    except:
        pass 
    
upload = Button(top, text='Upload an image', command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 15, 'bold'))
upload.pack()
upload.place(x=20, y=20)

sign_image.pack()
sign_image.place(x=70, y=100)

label.pack()
label.place(x=50, y=10)
heading = Label(top, image=img)
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
