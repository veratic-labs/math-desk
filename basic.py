"""
Copyright (c) Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import customtkinter as ctk
import math

SAFE_GLOBALS = {
    "__builtins__": {},
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round,
}

class BasicCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Title
        self.title_label = ctk.CTkLabel(self, text="Basic Calculator", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(anchor="w", padx=20, pady=(20, 10))

        # Input area
        self.input_box = ctk.CTkEntry(self, placeholder_text="Enter an expression...")
        self.input_box.pack(fill="x", padx=20, pady=(20, 10))

        # Button frame
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(anchor="w", padx=20, pady=(0, 20))

        # Calculate button
        self.calculate_button = ctk.CTkButton(self.button_frame, text="Calculate", command=self.calculate, width=100)
        self.calculate_button.pack(side="left")

        # Clear button
        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear", width=80, command=self.clear)
        self.clear_button.pack(side="left", padx=(10, 0))

        # Result title
        self.result_title = ctk.CTkLabel(self, text="Result", font=ctk.CTkFont(size=16, weight="bold"))
        self.result_title.pack(anchor="w", padx=20, pady=(15, 5))

        # Result label
        self.result_label = ctk.CTkLabel(self, text="", anchor="w")
        self.result_label.pack(fill="x", padx=20)

    def calculate(self):
        expression = self.input_box.get()

        try:
            result = self.evaluate_expression(expression)
            self.result_label.configure(text=str(result))
        
        except Exception:
            self.result_label.configure(text="Invalid input")

    def evaluate_expression(self, expression):
        return eval(expression, SAFE_GLOBALS, {})

    def clear(self):
        self.input_box.delete(0, "end")
        self.result_label.configure(text="")
    