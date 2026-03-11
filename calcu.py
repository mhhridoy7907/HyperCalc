import math
import tkinter as tk


class ScientificCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.geometry("430x560")
        self.root.resizable(False, False)

        self.max_decimal_places = 10

        self.colors = {
            "bg": "#111827",
            "entry_bg": "#1F2937",
            "entry_fg": "#F9FAFB",
            "number_bg": "#374151",
            "number_fg": "#F9FAFB",
            "operator_bg": "#F59E0B",
            "operator_fg": "#111827",
            "function_bg": "#2563EB",
            "function_fg": "#E5E7EB",
            "clear_bg": "#DC2626",
            "clear_fg": "#FFFFFF",
            "equal_bg": "#10B981",
            "equal_fg": "#06281C",
        }

        self._configure_window()
        self._build_ui()
        self._bind_keyboard()
        self.allowed_names = self._build_allowed_names()

    def _configure_window(self):
        self.root.configure(bg=self.colors["bg"])

    def _build_ui(self):
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            self.root,
            textvariable=self.entry_var,
            font=("Segoe UI", 22, "bold"),
            bd=0,
            relief=tk.FLAT,
            justify="right",
            bg=self.colors["entry_bg"],
            fg=self.colors["entry_fg"],
            insertbackground=self.colors["entry_fg"],
        )
        self.entry.pack(fill="x", padx=14, pady=14, ipady=14)

        self.frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.frame.pack(fill="both", expand=True, padx=10, pady=(2, 10))

        buttons = [
            ("7", lambda: self.press("7"), "number"),
            ("8", lambda: self.press("8"), "number"),
            ("9", lambda: self.press("9"), "number"),
            ("/", lambda: self.press("/"), "operator"),
            ("sin", lambda: self.press("sin("), "function"),
            ("4", lambda: self.press("4"), "number"),
            ("5", lambda: self.press("5"), "number"),
            ("6", lambda: self.press("6"), "number"),
            ("*", lambda: self.press("*"), "operator"),
            ("cos", lambda: self.press("cos("), "function"),
            ("1", lambda: self.press("1"), "number"),
            ("2", lambda: self.press("2"), "number"),
            ("3", lambda: self.press("3"), "number"),
            ("-", lambda: self.press("-"), "operator"),
            ("tan", lambda: self.press("tan("), "function"),
            ("0", lambda: self.press("0"), "number"),
            (".", lambda: self.press("."), "number"),
            ("=", self.calculate, "equal"),
            ("+", lambda: self.press("+"), "operator"),
            ("√", lambda: self.press("sqrt("), "function"),
            ("(", lambda: self.press("("), "number"),
            (")", lambda: self.press(")"), "number"),
            ("log", lambda: self.press("log10("), "function"),
            ("ln", lambda: self.press("ln("), "function"),
            ("π", lambda: self.press("pi"), "function"),
            ("x²", lambda: self.press("**2"), "function"),
            ("⌫", self.backspace, "operator"),
            ("C", self.clear, "clear"),
        ]

        row = 0
        col = 0

        for text, command, kind in buttons:
            style = self._button_style(kind)
            btn = tk.Button(
                self.frame,
                text=text,
                command=command,
                font=("Segoe UI", 13, "bold"),
                bd=0,
                relief=tk.FLAT,
                activebackground=style["active_bg"],
                activeforeground=style["active_fg"],
                bg=style["bg"],
                fg=style["fg"],
                padx=8,
                pady=8,
                cursor="hand2",
            )
            btn.grid(row=row, column=col, padx=6, pady=6, sticky="nsew", ipadx=6, ipady=6)
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(6):
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.frame.grid_columnconfigure(i, weight=1)

    def _button_style(self, kind):
        if kind == "number":
            return {
                "bg": self.colors["number_bg"],
                "fg": self.colors["number_fg"],
                "active_bg": "#4B5563",
                "active_fg": self.colors["number_fg"],
            }
        if kind == "operator":
            return {
                "bg": self.colors["operator_bg"],
                "fg": self.colors["operator_fg"],
                "active_bg": "#FBBF24",
                "active_fg": self.colors["operator_fg"],
            }
        if kind == "clear":
            return {
                "bg": self.colors["clear_bg"],
                "fg": self.colors["clear_fg"],
                "active_bg": "#EF4444",
                "active_fg": self.colors["clear_fg"],
            }
        if kind == "equal":
            return {
                "bg": self.colors["equal_bg"],
                "fg": self.colors["equal_fg"],
                "active_bg": "#34D399",
                "active_fg": self.colors["equal_fg"],
            }
        return {
            "bg": self.colors["function_bg"],
            "fg": self.colors["function_fg"],
            "active_bg": "#3B82F6",
            "active_fg": self.colors["function_fg"],
        }

    def _bind_keyboard(self):
        allowed_chars = "0123456789.+-*/()"
        for char in allowed_chars:
            self.root.bind(char, lambda event, c=char: self.press(c))

        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<KP_Enter>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear())

    def _build_allowed_names(self):
        return {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log10": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "pow": pow,
        }

    def press(self, value):
        self.entry.insert(tk.END, value)

    def clear(self):
        self.entry_var.set("")

    def backspace(self):
        current = self.entry_var.get()
        self.entry_var.set(current[:-1])

    def format_result(self, result):
        if isinstance(result, float):
            if result.is_integer():
                return str(int(result))
            formatted = f"{result:.{self.max_decimal_places}f}".rstrip("0").rstrip(".")
            return formatted if formatted else "0"
        return str(result)

    def evaluate_expression(self, expr):
        safe_globals = {"__builtins__": {}}
        return eval(expr, safe_globals, self.allowed_names)

    def calculate(self):
        expr = self.entry_var.get().strip()
        if not expr:
            return

        try:
            result = self.evaluate_expression(expr)
            self.entry_var.set(self.format_result(result))
        except SyntaxError:
            self.entry_var.set("Syntax Error")
        except ZeroDivisionError:
            self.entry_var.set("Math Error: Division by zero")
        except ValueError:
            self.entry_var.set("Math Error: Invalid domain")
        except OverflowError:
            self.entry_var.set("Math Error: Overflow")
        except NameError:
            self.entry_var.set("Invalid Function")
        except TypeError:
            self.entry_var.set("Type Error")
        except Exception:
            self.entry_var.set("Error")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ScientificCalculator()
    app.run()