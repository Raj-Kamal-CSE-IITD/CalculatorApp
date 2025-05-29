from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.expression = ""

        self.input_field = TextInput(
            text="",
            font_size=32,
            size_hint=(1, 0.2),
            multiline=False,
            halign="right",
            readonly=True
        )
        self.add_widget(self.input_field)

        button_grid = GridLayout(cols=5, spacing=5, size_hint=(1, 0.75))
        buttons = [
            "7", "8", "9", "/", "sqrt",
            "4", "5", "6", "*", "log",
            "1", "2", "3", "-", "ln",
            "0", ".", "+", "x^y", "π",
            "sin", "cos", "tan", "!", "e"
        ]

        for label in buttons:
            btn = Button(
                text=label,
                font_size=24,
            )
            btn.bind(on_press=self.on_button_click)
            button_grid.add_widget(btn)

        self.add_widget(button_grid)

        # Last row layout for Clear and Result buttons
        last_row = BoxLayout(size_hint=(1, 0.15), spacing=5)

        clear_btn = Button(
            text="Clear",
            font_size=24,
            background_color=(1, 0, 0, 1),  # Red
            size_hint=(0.4, 1)  # Twice width relative to result (0.4 vs 0.6)
        )
        clear_btn.bind(on_press=self.on_button_click)

        result_btn = Button(
            text="Result",
            font_size=24,
            background_color=(0, 1, 0, 1),  # Green
            size_hint=(0.6, 1)
        )
        result_btn.bind(on_press=self.on_button_click)

        last_row.add_widget(clear_btn)
        last_row.add_widget(result_btn)

        self.add_widget(last_row)

    def on_button_click(self, instance):
        char = instance.text
        try:
            if char == "Result":
                self.expression = str(eval(self.expression))
            elif char == "Clear":
                self.expression = ""
            elif char == "sqrt":
                self.expression = str(math.sqrt(eval(self.expression)))
            elif char == "log":
                self.expression = str(math.log10(eval(self.expression)))
            elif char == "ln":
                self.expression = str(math.log(eval(self.expression)))
            elif char == "sin":
                self.expression = str(math.sin(math.radians(eval(self.expression))))
            elif char == "cos":
                self.expression = str(math.cos(math.radians(eval(self.expression))))
            elif char == "tan":
                self.expression = str(math.tan(math.radians(eval(self.expression))))
            elif char == "!":
                self.expression = str(math.factorial(int(eval(self.expression))))
            elif char == "π":
                self.expression += str(math.pi)
            elif char == "e":
                self.expression += str(math.e)
            elif char == "x^y":
                self.expression += "**"
            else:
                self.expression += char
        except Exception:
            self.expression = "Error"

        self.input_field.text = self.expression


class ScientificCalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    ScientificCalculatorApp().run()
