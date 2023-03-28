from tkinter import Image

import cv2
from easyocr import easyocr
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
class MyApp(App):

    def build(self):
        root = StackLayout()

        for i in range(10):


            btn = Image(source= 'cropped_image.jpg' ,size_hint_y= 0.05, size_hint_x= None)

            root.add_widget(btn)


        return root

MyApp().run()

