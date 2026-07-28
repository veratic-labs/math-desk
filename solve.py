import customtkinter as ctk
import sympy as sp

class SolveEquation(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #title
        self.title_label = ctk.CTkLabel(self, text="Solve Equation", font=("Arial", 24, "bold"))
        self.title_label.pack(anchor="w", padx=20, pady=(20, 10))

        #choose mode
        self.mode_var = ctk.StringVar(value="Symbolic")
        self.mode_menu = ctk.CTkOptionMenu(self, values=["Symbolic", "Numerical"], height=25, variable=self.mode_var, command=self.change_mode)
        self.mode_menu.pack(anchor="w", padx=20, pady=(0, 15))

        #enter equation
        self.equation_entry = ctk.CTkEntry(self, width=400, placeholder_text="Enter an equation...")
        self.equation_entry.pack(anchor="w", padx=20, pady=(0, 15))

        #initial guess for numerical solution
        self.numerical_frame = ctk.CTkFrame(self, fg_color="transparent", height=0)
        self.numerical_frame.pack(anchor="w", padx=20, fill="x")

        self.initial_guess_label = ctk.CTkLabel(self.numerical_frame, text="Initial Guess")
        self.initial_guess_entry = ctk.CTkEntry(self.numerical_frame, width=150)

        #solve button
        self.solve_button = ctk.CTkButton(self, text="Solve", command=self.solve_equ)
        self.solve_button.pack(anchor="w", padx=20, pady=(10, 15))

        #result
        self.result_title = ctk.CTkLabel(self, text="Result", font=("Arial", 16, "bold"))
        self.result_title.pack(anchor="w", padx=20, pady=(10, 5))

        self.result_label = ctk.CTkLabel(self, text="", justify="left", wraplength=300)
        self.result_label.pack(anchor="w", padx=20)

        #default mode
        self.mode = "Symbolic"

    def change_mode(self, mode):
        self.mode = mode

        if mode == "Symbolic":
            self.initial_guess_label.pack_forget()
            self.initial_guess_entry.pack_forget()

            self.numerical_frame.configure(height=0)

        elif mode == "Numerical":
            self.initial_guess_label.pack(anchor="w")
            self.initial_guess_entry.pack(anchor="w", pady=(0, 10))

    def solve_equ(self):
        try:
            equation_text = self.equation_entry.get()

            #user can enter equation or just expression
            if "=" in equation_text:
                left_text, right_text = equation_text.split("=", 1)
            else:
                left_text = equation_text
                right_text = "0"

            #convert into sympy expressions
            left_expr = sp.sympify(left_text)
            right_expr = sp.sympify(right_text)

            equation = sp.Eq(left_expr, right_expr)

            #start solve function with unknown x
            x = sp.symbols("x")

            if self.mode == "Symbolic":
                solutions = sp.solve(equation, x)
                self.result_label.configure(text=f"x = {', '.join(map(str, solutions))}")

            elif self.mode == "Numerical":
                initial_guess_text = self.initial_guess_entry.get()
                initial_guess = sp.simplify(initial_guess_text)

                expression = left_expr - right_expr
                solution = sp.nsolve(expression, x, initial_guess)

                self.result_label.configure(text=f"x ≈ {solution}")

        except Exception:
            self.result_label.configure(text="Input Invalid")

