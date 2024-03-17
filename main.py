from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.core.window import Window
from moviepy.editor import VideoFileClip
from kivymd.uix.screenmanager import ScreenManager
from kivy.config import Config
import os
Config.set('graphics', 'resizable',False)
Config.write()

class MainWindow(ScreenManager):
    pass

class ConvertApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Snow'
        Builder.load_file('Style.kv')
        return MainWindow()
    def convert(self):
        if (os.path.exists(self.root.ids.target_mp4.text)
                and os.path.exists(self.root.ids.target_gif.text)
                and self.root.ids.target_mp4.text != ''
                and self.root.ids.target_gif.text != ''
                and self.root.ids.gif_name.text != ''):
            video = VideoFileClip('media.mp4')
            video.write_gif('media.gif')
        else:
            print('No video file found')
ConvertApp().run()