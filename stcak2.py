from tkinter import Image

import cv2
from easyocr import easyocr
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class MainApp(App):

    def build(self):
        root = StackLayout()
        img = cv2.imread('text.png')
        reader = easyocr.Reader(['en'], gpu=False)  # bedre om du har gpu og raaskere
        result = reader.readtext(img)  # Matrise
        i =0
        for text in result:
            i=1+i
            p1 = text[0][0]
            p2 = text[0][2]
            y1 = p1[1]
            y2 = p2[1]
            x1 = p1[0]
            x2 = p2[0]
            # cpx = text[0][2]
            detectedText = text[1]
            croppeed = img[y1:y2, x1:x2]
            result1 = reader.readtext(croppeed,detail=1, ycenter_ths=0.2, paragraph=False, width_ths=0.1)  # Matrise
            for text1 in result1:
                i = 1 + i
                px1 = text1[0][0]
                px2 = text1[0][2]
                yx1 = p1[1]
                yx2 = p2[1]
                xx1 = p1[0]
                xx2 = p2[0]
                # cpx = text[0][2]
                detectedText = text1[1]
                croppeed1 = croppeed[yx1:yx2, xx1:xx2]
                cv2.imwrite("IMG{}.png".format(i), croppeed1)
                btn = Image(source= "IMG_{}.png".format(i),size_hint_y= 0.05, size_hint_x=None)
                root.add_widget(btn)


        return root

MainApp().run()

