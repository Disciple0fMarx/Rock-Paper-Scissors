from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

__author__ = "Dhya El Bahri"


Builder.load_string("""
<StartWindow>:
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        Label:
            text: "Rock Paper Scissors"
            font_size: 22
            size_hint: .1, .1
            pos_hint: {"center_x": .5}
            color: "#03C04A"
            bold: True
        Image:
            source: "img/logo.png"
            pos_hint: {"center_x": .5, "center_y": .5}
        Button:
            text: "Start"
            size_hint: None, None
            width: 200
            height: 100
            pos_hint: {"center_x": .5}
            background_color: "#03C04A"
            bold: True
            background_normal: ""
            font_size: 18
            on_release: app.root.current = "game"
<GameWindow>:
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        Button:
            text: "Go back"
            background_color: "#03C04A"
            background_normal: ""
            pos_hint: {"x": 0, "y": 0}
            size_hint: None, None
            height: 50
            width: 50
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
            pos_hint: {"center_x": .5, "center_y": .5}
        AnchorLayout:
            anchor_x: "center"
            anchor_y: "bottom"
            padding: 20
            BoxLayout:
                orientation: "horizontal"
                size_hint: None, None
                width: 300
                height: 100
                Button:
                    size_hint: None, None
                    width: 100
                    height: 100
                    background_color: 1, 1, 1, 1
                    background_normal: ""
                    background_down: ""
                    on_press: root.rock_on()
                    on_release: root.rock_off()
                    Image:
                        id: "rock"
                        source: "img/rock.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                Button:
                    size_hint: None, None
                    width: 100
                    height: 100
                    background_color: 1, 1, 1, 1
                    background_normal: ""
                    background_down: ""
                    on_press: root.paper_on()
                    on_release: root.paper_off()
                    allow_stretch: False
                    Image:
                        id: "paper"
                        source: "img/paper.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                Button:
                    size_hint: None, None
                    width: 100
                    height: 100
                    background_color: 1, 1, 1, 1
                    background_normal: ""
                    background_down: ""
                    on_press: root.scissors_on()
                    on_release: root.scissors_off()
                    Image:
                        id: "scissors"
                        source: "img/scissors.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
""")


class StartWindow(Screen):
    """The start screen"""
    pass


class GameWindow(Screen):
    """The actual game screen"""
    def rock_on(self):
        self.ids['"rock"'].source = "img/rock_pressed.png"

    def rock_off(self):
        self.ids['"rock"'].source = "img/rock.png"

    def paper_on(self):
        self.ids['"paper"'].source = "img/paper_pressed.png"

    def paper_off(self):
        self.ids['"paper"'].source = "img/paper.png"
    
    def scissors_on(self):
        self.ids['"scissors"'].source = "img/scissors_pressed.png"

    def scissors_off(self):
        self.ids['"scissors"'].source = "img/scissors.png"


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
