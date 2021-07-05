from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class PlayGame(App):
    def build(self):
        window = BoxLayout(orientation="vertical")
        Window.clearcolor = (1, 1, 1, 1)
        gameTitle = Label(
            text="Rock Paper Scissors",
            font_size=20,
            size_hint=(.1, .1),
            pos_hint={"center_x": .5, "center_y": .5},
            color="#03C04A",
            bold=True
        )
        window.add_widget(gameTitle)
        logo = Image(source="favicon.png", pos_hint={"center_x": .5, "center_y": .5})
        window.add_widget(logo)
        startButton = Button(
            text="Start",
            size_hint=(1, .25),
            pos_hint={"center_x": .5, "center_y": .5},
            background_color="#03C04A",
            bold=True,
            background_normal="",
            font_size=18
        )
        window.add_widget(startButton)
        window.size_hint = (.6, .9)
        window.pos_hint = {"center_x": .5, "center_y": .5}

        return window


if __name__ == "__main__":
    PlayGame().run()
