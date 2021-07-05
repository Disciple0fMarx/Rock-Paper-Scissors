from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_string("""
<StartWindow>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Rock Paper Scissors"
            font_size: 20
            size_hint: .1, .1
            pos_hint: {"center_x": .5, "center_y": .5}
            color: "#03C04A"
            bold: True
        Image:
            source: "favicon.png"
            pos_hint: {"center_x": .5, "center_y": .5}
        Button:
            text: "Start"
            size_hint: 1, .25
            pos_hint: {"center_x": .5, "center_y": .5}
            background_color: "#03C04A"
            bold: True
            background_normal: ""
            font_size: 18
            on_release: app.root.current = "game"
<GameWindow>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "You made it here!"
            color: "#000000"
        Button:
            text: "Go back"
            on_release: app.root.current = "start"
""")


# Declare both classes
class StartWindow(Screen):
    """The start menu"""
    pass


class GameWindow(Screen):
    """The actual game"""
    pass


class PlayGame(App):
    def build(self):
        """The application we're running"""
        Window.clearcolor = (1, 1, 1, 1)
        screen_manager = ScreenManager()
        screen = Screen(name="start")
        self.start_screen = StartWindow()
        screen.add_widget(self.start_screen)
        screen_manager.add_widget(screen)
        self.start_screen.size_hint = (.6, .9)
        self.start_screen.pos_hint = {"center_x": .5, "center_y": .5}
        screen = Screen(name="game")
        self.game_screen = GameWindow()
        screen.add_widget(self.game_screen)
        screen_manager.add_widget(screen)
        return screen_manager


if __name__ == "__main__":
    PlayGame().run()
