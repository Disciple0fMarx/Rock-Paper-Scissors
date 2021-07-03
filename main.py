from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class PlayGame(App):
    def build(self):
        self.window = GridLayout()
        Window.clearcolor = (1, 1, 1, 1)
        self.window.cols = 1
        self.gameTitle = Label(
            text="Rock Paper Scissors",
            font_size=20,
            size_hint=(.5, .5),
            color="#03C04A",
            bold=True
        )
        self.window.add_widget(self.gameTitle)
        self.logo = Image(source="favicon.png")
        self.window.add_widget(self.logo)
        self.startButton = Button(
            text="Start",
            size_hint=(.5, .5),
            background_color="#03C04A",
            bold=True,
            background_normal="",
            font_size=18
        )
        self.window.add_widget(self.startButton)
        self.window.size_hint = (.6, .9)
        self.window.pos_hint = {"center_x": .5, "center_y": .5}

        return self.window


if __name__ == "__main__":
    PlayGame().run()
