from kivy.app import App
from kivy.uix.label import Label
from plyer import gps


class Main(App):
    def build(self):
        return Label(text="Wsh les gars")

Main().run()