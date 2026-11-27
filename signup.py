import flet as ft
from flet import *


def main(page: ft.Page):
    page.title = 'Signup'
    page.vertical_alignment =ft.MainAxisAlignment.CENTER
    page.width = 400
    page.height = 400
    page.window_resizable = False 

    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='I agree to stuff', value=False)
    button_submit: ft.Button = ft.Button(content='Sign UP', width=200, disabled=True)



    def validate(e: ft.ControlEvent):
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled=False
        else:
            button_submit.disabled= True

        page.update()

    def submit(e: ft.ControlEvent):
        print('Username', text_username.value)
        print('text_password', text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.run(main)