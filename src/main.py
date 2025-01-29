
import flet as ft


class Mybutton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor= ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text
        self.on_click = on_click

def main(page: ft.Page):

    def ok_clickecd(e):
        """methode pour ok"""
        print("Ok i'm go")
    
    def cancel_clicked(e):
        """Methode pour cancel"""
        print("Sorry bro your mon it not ok.")

    page.add(Mybutton(text="OK it work", on_click=ok_clickecd), Mybutton(text="cancel", on_click=cancel_clicked))
    

ft.app(main)
