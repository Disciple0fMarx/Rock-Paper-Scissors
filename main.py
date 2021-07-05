from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

__author__ = "Dhya El Bahri"


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
        Button:
            text: "Go back"
            background_color: "#03C04A"
            background_normal: ""
            pos_hint: {"x": 0, "y": 0}
            size_hint: .2, .2
            on_release: app.root.current = "start"
        BoxLayout:
            orientation: "horizontal"
            size_hint: 1, .25
            Label:
                text: "You: 0"
                color: "#000000"
                font_size: 20
            Label:
                text: "Computer: 0"
                color: "#000000"
                font_size: 20
        Label:
            text: "Make a move"
            color: "#000000"
            font_size: 20
        BoxLayout:
            orientation: "horizontal"
            size_hint: 1, .5
            Button:
                text: "Rock"
                font_size: 20
            Button:
                text: "Paper"
                font_size: 20
            Button:
                text: "Scissors"
                font_size: 20
""")


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
