from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from plyer import gps


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text ="First Name : "))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text ="Last Name : "))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text ="email : "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        firstname = self.firstname.text
        lastname = self.lastname.text
        email = self.email.text

        print("Name : ", firstname, "Last Name : ", lastname, "Email : ", email)
        self.firstname.text = ""
        self.lastname.text = ""
        self.email.text = ""



class Main(App):
    def build(self):
        return Grid()

Main().run()