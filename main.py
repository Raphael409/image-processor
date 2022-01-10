from tkinter import *
import sys
import cv2
import numpy as np
from PIL import ImageTk, Image

root = Tk()
root.geometry('1255x944+50+50')
root.title('Video Processor')


def sel(self):
    selection = "Threshold: " + str(th_val.get())
    thresholdValue.config(text=selection)


class Frame_Grab:
    def __init__(self, image, threshold):
        self.image = image
        self.threahold = threshold

    def transform(self):
        img1 = cv2.imread('image.jpg')
        retval, threshold = cv2.threshold(img1, 30, 255, cv2.THRESH_BINARY)
        photo = Image.open("download.png")
        photo1 = ImageTk.PhotoImage(photo)
        cv2.imshow("threshold", threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class Sliders_Data:
    def set_slider_data(self):
        print("Slider data")


class Region1(Frame_Grab, Sliders_Data):
    def Pixel_Calculation(self):
        super().__init__(self)
        super().position(self)
        print("Region 1 calculated")


class Region2(Frame_Grab, Sliders_Data):
    def Pixel_Calculation(self):
        super().__init__(self)
        super().position(self)
        print("Region 2 calculated")


class Region3(Frame_Grab, Sliders_Data):
    def Pixel_Calculation(self):
        super().__init__(self)
        super().position(self)
        print("Region 3 calculated")


class Filter(Frame_Grab, Sliders_Data):
    def Filter_Implement(self):
        super().__init__(self)
        super().position(self)
        print("implimented")
        return


# Variables declaration
th_val = DoubleVar()
lH1_val = DoubleVar()
uH1_val = DoubleVar()
lH2_val = DoubleVar()
uH2_val = DoubleVar()
lH3_val = DoubleVar()
uH3_val = DoubleVar()

# video regions

labelRegion1 = Label(root, text="Region 1", bg="blue", height=15, width=30, borderwidth="5", relief="groove")
# labelRegion1.image = photo1
labelRegion1.place(x=10, y=10)

labelRegion2 = Label(root, text="Region 2", bg="red", height=15, width=30, borderwidth="5", relief="groove")
labelRegion2.place(x=220, y=10)

labelRegion3 = Label(root, text="Region 3", bg="grey", height=15, width=30, borderwidth="5", relief="groove")
labelRegion3.place(x=430, y=10)

# sliders labels

lH1 = Label(root, text=f"LH: 0.0")
lH1.place(x=150, y=300)

uH1 = Label(root, text=f"UH: 0.0")
uH1.place(x=150, y=330)

lH2 = Label(root, text=f"LH: 0.0")
lH2.place(x=150, y=390)

uH2 = Label(root, text=f"UH: 0.0")
uH2.place(x=150, y=420)

lH3 = Label(root, text=f"LH: 0.0")
lH3.place(x=150, y=480)

uH3 = Label(root, text=f"UH: 0.0")
uH3.place(x=150, y=510)

thresholdValue = Label(root, text=f"Threshold: 0.0")
thresholdValue.place(x=130, y=570)

# Sliders

sldlH1 = Scale(root, variable=lH1_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
sldlH1.place(x=220, y=300)

slduH1 = Scale(root, variable=uH1_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
slduH1.place(x=220, y=330)

sldlH2 = Scale(root, variable=lH2_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
sldlH2.place(x=220, y=390)

slduH2 = Scale(root, variable=uH2_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
slduH2.place(x=220, y=420)

sldlH3 = Scale(root, variable=lH3_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
sldlH3.place(x=220, y=480)

slduH3 = Scale(root, variable=uH3_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
slduH3.place(x=220, y=510)

sldthreshold = Scale(root, variable=th_val, from_=0, to=255, orient=HORIZONTAL, command=sel, showvalue=0)
sldthreshold.place(x=220, y=570)

# Buttons

applyThreshold = Button(root, text="Apply Threshold", font=('arial', 13), width=30)
applyThreshold.place(x=700, y=100)

calculateRegion1 = Button(root, text="Calculate for region 1", font=('arial', 13), width=30)
calculateRegion1.place(x=700, y=150)

calculateRegion2 = Button(root, text="Calculate for region 2", font=('arial', 13), width=30)
calculateRegion2.place(x=700, y=200)

calculateRegion2 = Button(root, text="Calculate for region 3", font=('arial', 13), width=30)
calculateRegion2.place(x=700, y=250)
root.mainloop()
