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
from fpdf import FPDF
import numpy as np

class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self.image)

        self.save_img_button = MDRaisedButton(
            text="Trkk Her!",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None)
        )
        self.save_img_button.bind(on_press=self.imageToText)

        layout.add_widget(self.save_img_button)

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        # frame
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def imageToText(self, *args):
        image_name= "bildeFraKamera.png"
        cv2.imwrite(image_name, self.image_frame)
        img = cv2.imread('bildeFraKamera.png')

        reader = easyocr.Reader(['en'], gpu=False)  # bedre om du har gpu og raaskere
        #result = reader.readtext(img)  # matrise av ordene

        result = reader.readtext(img, detail=0, blocklist="-.:';,",
        slope_ths=0.1,ycenter_ths=0.2)

        print(result)

if __name__ == '__main__':
    MainApp().run()