from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (350, 600)


class StartScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class SecondScreen(Screen):

    def printTxt(self, text):
        print(text)


class OwnDesk(Screen):

    fulldeck = []
    for k in 'SHDC':
        for v in range(1, 14):
            if k == 'S':
                fulldeck.append({(k, v):Image(source="images/cards/spades/" + str(v) + "_of_spades.png")})
            elif k == 'H':
                fulldeck.append({(k, v):Image(source="images/cards/hearts/" + str(v) + "_of_hearts.png")})
            elif k == 'D':
                fulldeck.append({(k, v):Image(source="images/cards/diamonds/" + str(v) + "_of_diamonds.png")})
            elif k == 'C':
                fulldeck.append({(k, v):Image(source="images/cards/clubs/" + str(v) + "_of_clubs.png")})

    img = fulldeck[0].values()




def on_box(self, *args):
    for i in range(5):
        self.box.add_widget(Button(text=str(i)))

class ThirdScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


kv = Builder.load_file("dirtyfive.kv")


class DirtyFive(App):

    def build(self):
        self.text = None
        self.player_count = None
        return kv

    def player(self):
        pass

    def do(self):
        print("i pressed")
        print(self.text)
        print(self.player_count)


if __name__ == '__main__':
    DirtyFive().run()
