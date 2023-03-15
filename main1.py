from kivy import app
from kivy.uix import layout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
import cv2
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import easyocr
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp, App
from kivy.uix.boxlayout import BoxLayout
from fpdf import FPDF
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.image import Image as CoreImage
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder
from kivymd.app import MDApp

import numpy as np
from kivymd.uix.list import OneLineListItem

KV = '''
ScrollView:

    MDList:
        id: container
'''

#class MyLayout(MDApp):

class Main(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        img = cv2.imread('text.png')
        reader = easyocr.Reader(['en'], gpu=False)  # bedre om du har gpu og raaskere
        result = reader.readtext(img, detail=1, ycenter_ths=0.2, paragraph=False, width_ths=0.1) # Matrise
        for text in result:
            p1 = text[0][0]
            p2 = text[0][2]
            y1 = p1[1]
            y2 = p2[1]
            x1 = p1[0]
            x2 = p2[0]
            cpx = text[0][2]
            detectedText = text[1]
            cropped = img[y1:y2, x1:x2]
            cv2.imwrite("cropped_image.jpg", cropped)

            self.root.ids.container.add_widget(OneLineListItem(text=detectedText))

Main().run()

"""
 def on_kv_post(self, obj):
        img= Image(source="text.png", center_x=self.parent.center_x, center_y=self.parent.center_y)
        self.ids.image.add_widget(Button(img))

    def on_kv_post(self, obj):
        self.ids.image.add_widget(Button(font_size='20sp'))

     for i in range(10):



        img = cv2.imread('text.png')
        reader = easyocr.Reader(['en'], gpu=False)  # bedre om du har gpu og raaskere
        result = reader.readtext(img)  # matrise av ordene

        for text in result:
            p1 = text[0][0]
            p2 = text[0][2]
            y1 = p1[1]
            y2 = p2[1]
            x1 = p1[0]
            x2 = p2[0]
            cpx = text[0][2]
            detectedText = text[1]
            cropped = img[y1:y2, x1:x2]
            cv2.imwrite("cropped_image.jpg", cropped)
            source = Image(source='cropped_image.jpg')


"""
