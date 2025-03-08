# from kivy.app import App
# from kivy.uix.button import Button

# class MyApp(App):
#     def build(self):
#         return Button(text="Click Me", on_press=self.on_button_press)

#     def on_button_press(self, instance):
#         instance.text = "You clicked me!"

# if __name__ == "__main__":
#     MyApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        button = Button(
            text="Styled Button",
            size_hint=(0.5, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size="20sp",
            background_color=(1, 0, 0, 1),  # RGBA
        )
        layout.add_widget(button)
        return layout

if __name__ == "__main__":
    MyApp().run()

