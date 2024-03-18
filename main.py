#!/usr/bin/env pypy
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.core.window import Window
from moviepy.editor import VideoFileClip
from kivymd.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivymd.uix.filemanager import MDFileManager
from kivy.metrics import dp
import os
from kivymd.uix.snackbar import MDSnackbar,MDSnackbarText
from kivymd.uix.dialog import MDDialog,MDDialogIcon,MDDialogHeadlineText
Config.set('graphics', 'resizable',False)
Config.write()

class MainWindow(ScreenManager):
    pass

class ConvertApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Snow'
        Builder.load_file('Style.kv')
        self.title = 'Convert video to gif'
        self.icon = 'Yooopy.png'
        return MainWindow()
    def convert(self):

        if (os.path.exists(self.root.ids.target_mp4.text)
                and os.path.exists(self.root.ids.target_gif.text)
                and self.root.ids.target_mp4.text != ''
                and self.root.ids.target_gif.text != ''
                and self.root.ids.gif_name.text != ''):
            video = VideoFileClip(str(self.root.ids.target_mp4.text))
            video.write_gif(str(self.root.ids.target_gif.text+'\\'+self.root.ids.gif_name.text+'.gif'),fps=30)
            self.Dialog_cmp()
        else:
            MDDialog(
                MDDialogIcon(
                    icon = 'alert'
                ),
                MDDialogHeadlineText(
                    text = 'Patch Doesnt exist or Is Not a Video file'
                )
            ).open()

    def select_path(self, path: str):
        texxt = path
        self.root.ids.target_mp4.text = texxt
        self.exit_manager()
    def file1(self):
        global file_manager
        path = os.path.expanduser("~")
        file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        file_manager.show(path)

    def exit_manager(self, *args):

        self.manager_open = False
        file_manager.close()
    #-------------------------------------


    def select_path2(self, path: str):
        texxt = path
        self.root.ids.target_gif.text = texxt
        self.exit_manager2()
    def file2(self):
        global file_manager2
        path = os.path.expanduser("~")
        file_manager2 = MDFileManager(
            exit_manager=self.exit_manager2,
            select_path=self.select_path2,
        )
        file_manager2.show(path)

    def exit_manager2(self, *args):

        self.manager_open = False
        file_manager2.close()
    def Dialog_cmp(self):
        MDSnackbar(
            MDSnackbarText(
                text="When you close App, Gif is ready",
            ),
            y=dp(40),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()



    def close_application(self):
        pass
    def change_theme(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.root.ids.theme.icon = 'weather-night'
            self.root.ids.hello.md_bg_color = '#808080'
        elif self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
            self.root.ids.theme.icon = 'weather-sunny'
            self.root.ids.hello.md_bg_color = '#191919'
    def color_set(self,instance):
        self.theme_cls.primary_palette = instance
        self.root.transition.direction = 'right'
        self.root.current = 'main'
    def main1(self):
        self.root.transition.direction = 'left'
        self.root.current = 'main2'




ConvertApp().run()