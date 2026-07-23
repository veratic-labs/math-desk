import customtkinter as ctk
from sympy import symbols, sympify, integrate, diff

class Calculus(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #title
        self.title_label = ctk.CTkLabel(self, text="Calculus", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(anchor="w", padx=20, pady=(20, 10))

        #select operational modes
        self.operation_menu = ctk.CTkOptionMenu(
            self, 
            values=[
                "Indefinite Integral", 
                "Definite Integral", 
                "Derivative", 
                "Derivative at Point"
                ], 
            width=150, 
            height=25, 
            font=ctk.CTkFont(size=14), 
            dropdown_font=ctk.CTkFont(size=14),
            command=self.change_operation
            )
        
        self.operation_menu.pack(anchor="w", padx=20, pady=(0, 15))

        #default
        self.operation_menu.set("Indefinite Integral")

        #input function
        self.function_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.function_frame.pack(fill="x", padx=20, pady=(10, 15))

        self.function_label = ctk.CTkLabel(self.function_frame, text="f(x) =", font=ctk.CTkFont(size=16))
        self.function_label.pack(side="left", padx=(0, 10))

        self.function_entry = ctk.CTkEntry(self.function_frame, placeholder_text="Enter a function...")
        self.function_entry.pack(side="left", fill="x", expand=True)

        #frame for extra inputs
        self.parameter_frame = ctk.CTkFrame(self, fg_color="transparent", height=0)
        self.parameter_frame.pack(fill="x")
        
        #upper bound and lower bound for definite integral
        self.bounds_frame = ctk.CTkFrame(self.parameter_frame, fg_color="transparent")

        self.lower_label = ctk.CTkLabel(self.bounds_frame, text="Lower Bound")
        self.lower_label.pack(side="left")

        self.lower_entry = ctk.CTkEntry(self.bounds_frame, width=100)
        self.lower_entry.pack(side="left", padx=(5, 20))

        self.upper_label = ctk.CTkLabel(self.bounds_frame, text="Upper Bound")
        self.upper_label.pack(side="left")

        self.upper_entry = ctk.CTkEntry(self.bounds_frame, width=100)
        self.upper_entry.pack(side="left", padx=(5, 0))

        #the point for derivative
        self.point_frame = ctk.CTkFrame(self.parameter_frame, fg_color="transparent")

        self.point_label = ctk.CTkLabel(self.point_frame, text="Point")
        self.point_label.pack(side="left")  

        self.point_entry = ctk.CTkEntry(self.point_frame, width=100)
        self.point_entry.pack(side="left", padx=(5, 0))

        #calculate button
        self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.calculate)
        self.calculate_button.pack(padx=20, pady=(10, 20))

        #show result
        self.result_title = ctk.CTkLabel(self, text="Result", font=ctk.CTkFont(size=16, weight="bold"), anchor="w")
        self.result_title.pack(fill="x", padx=20, pady=(15, 5))

        self.result_label = ctk.CTkLabel(self, text="", anchor="w", justify="left")
        self.result_label.pack(fill="x", padx=20)

        #set default operation
        self.operation = "Indefinite Integral"
        
    def change_operation(self, operation):
        self.operation = operation
        
        self.bounds_frame.pack_forget()
        self.point_frame.pack_forget()
        self.parameter_frame.configure(height=0)

        if operation == "Definite Integral":
            self.bounds_frame.pack(fill="x", padx=20, pady=(0, 15))
        elif operation == "Derivative at Point":
            self.point_frame.pack(fill="x", padx=20, pady=(0, 15))

    def calculate(self):
        try:
            #convert input to expression
            x = symbols("x")
            function = self.function_entry.get()

            expression = sympify(function)

            if self.operation == "Indefinite Integral":
                result = integrate(expression, x)
                self.result_label.configure(text=f"{result} + C")

            elif self.operation == "Definite Integral":
                #get the lower and upper bound
                lower = self.lower_entry.get()
                upper = self.upper_entry.get()

                result = integrate(expression, (x, lower, upper))
                self.result_label.configure(text=str(result))

            elif self.operation == "Derivative":
                result = diff(expression, x)
                self.result_label.configure(text=str(result))

            elif self.operation == "Derivative at Point":
                #get the point
                point = self.point_entry.get()
                point = sympify(point)

                #calculate the result
                result = diff(expression, x)
                result = result.subs(x, point)

                self.result_label.configure(text=str(result))
            
        except Exception:
            self.result_label.configure(text="Invalid input")




