import flet as ft

class Mybutton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor= ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text