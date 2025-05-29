import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("420x560")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.TOP, fill="both")

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), bd=10, relief='ridge', justify='right')
        input_field.grid(row=0, column=0, ipadx=8, ipady=20, columnspan=5, sticky="nsew")

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ["7", "8", "9", "/", "sqrt"],
            ["4", "5", "6", "*", "log"],
            ["1", "2", "3", "-", "ln"],
            ["0", ".", "+", "x^y", "π"],
            ["sin", "cos", "tan", "!", "e"]
        ]

        # Create all buttons except "Clear" and "Result"
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(btns_frame, text=btn_text, font=('Arial', 14), height=2, width=5,
                                command=lambda x=btn_text: self.on_button_click(x))
                btn.grid(row=i, column=j, padx=3, pady=3)

        # Last row for "Clear" and "Result"
        clear_button = tk.Button(btns_frame, text="Clear", font=('Arial', 14, 'bold'), height=2,
                                 bg="tomato", fg="white",
                                 command=lambda: self.on_button_click("Clear"))
        clear_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)

        result_button = tk.Button(btns_frame, text="Result", font=('Arial', 14, 'bold'),
                                  height=2, bg="lightgreen",
                                  command=lambda: self.on_button_click("Result"))
        result_button.grid(row=5, column=2, columnspan=3, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        try:
            if char == "Result":
                self.expression = str(eval(self.expression))
                self.input_text.set(self.expression)
            elif char == "Clear":
                self.expression = ""
                self.input_text.set("")
            elif char == "sqrt":
                self.expression = str(math.sqrt(eval(self.expression)))
                self.input_text.set(self.expression)
            elif char == "log":
                self.expression = str(math.log10(eval(self.expression)))
                self.input_text.set(self.expression)
            elif char == "ln":
                self.expression = str(math.log(eval(self.expression)))
                self.input_text.set(self.expression)
            elif char == "sin":
                self.expression = str(math.sin(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == "cos":
                self.expression = str(math.cos(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == "tan":
                self.expression = str(math.tan(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == "!":
                self.expression = str(math.factorial(int(eval(self.expression))))
                self.input_text.set(self.expression)
            elif char == "π":
                self.expression += str(math.pi)
                self.input_text.set(self.expression)
            elif char == "e":
                self.expression += str(math.e)
                self.input_text.set(self.expression)
            elif char == "x^y":
                self.expression += "**"
                self.input_text.set(self.expression)
            else:
                self.expression += str(char)
                self.input_text.set(self.expression)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
