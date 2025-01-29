import time
import flet as ft


def main(page: ft.Page):
    
    def checkbox_changed(e):
        output_text.value =(
            f"Tu as apris a comment skyer {todo_check.value}"
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="Todo: Apprendre a faire du sky", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)
ft.app(main)
