from kivymd.app import MDApp
from kivy.app import App
# from kivy.lang import Builder
# from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from screens.screens import *
from kivy.core.window import Window

Window.size = (337.5, 750)


class WindowManager(ScreenManager):
    pass


class Voyage(MDApp):
    # CLASSES = {
    #     'Travel': 'screens.travel',
    #     'Hasil': 'screens.hasil',
    # }

    # AUTORELOADER_PATHS = [
    #     ('.', {'recursive': True})
    # ]

    # KV_FILES = [
    #     'kv/travel.kv',
    #     'kv/hasil.kv',
    # ]

    def build_app(self):
        self.icon = "./kv/voyage.png"
        self.wm = WindowManager()
        self.wm.add_widget(Travel(name="travel"))
        self.wm.add_widget(Hasil(name="hasil"))
        # screens = [
        #     Travel(name="travel"),
        #     Hasil(name="hasil"),
        # ]

        
        # for screen in screens:
        #     self.wm.add_widget(screen)
        return self.wm
        # ScreenManager = screens()
        



if __name__ == '__main__':
    LabelBase.register(name="RPoppins", fn_regular="kv/Poppins-Regular-400.ttf")
    LabelBase.register(name="BPoppins", fn_regular="kv/Poppins-Bold-700.ttf")
    LabelBase.register(name="MPoppins", fn_regular="kv/Poppins-Medium.ttf")
    LabelBase.register(name="SBPoppins", fn_regular="kv/Poppins-SemiBold.ttf")

    Voyage().run()
