"""Simple Calculator GUI using Tkinter.

Buttons: digits, +, -, *, /, ., =, Clear.
Evaluate uses a safe try/except around Python's `eval` for simplicity.
"""
import tkinter as tk


class CalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Calculator")
        root.geometry("320x380")

        self.expr = ""

        self.display = tk.Entry(root, font=("Segoe UI", 18), bd=6, relief="ridge", justify="right")
        self.display.pack(fill="both", padx=8, pady=10)

        btns = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both", padx=8, pady=6)

        for r, row in enumerate(btns):
            for c, char in enumerate(row):
                btn = tk.Button(frame, text=char, font=("Segoe UI", 16), command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)

        ctrl = tk.Frame(root)
        ctrl.pack(fill="x", padx=8, pady=(0, 8))
        tk.Button(ctrl, text="Clear", command=self.clear, font=("Segoe UI", 12)).pack(side="left")
        tk.Button(ctrl, text="Back", command=self.backspace, font=("Segoe UI", 12)).pack(side="right")

        root.bind('<Return>', lambda e: self.evaluate())
        root.bind('<BackSpace>', lambda e: self.backspace())

    def on_click(self, ch: str) -> None:
        if ch == "=":
            self.evaluate()
            return
        self.expr += ch
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expr)

    def clear(self) -> None:
        self.expr = ""
        self.display.delete(0, tk.END)

    def backspace(self) -> None:
        self.expr = self.expr[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expr)

    def evaluate(self) -> None:
        try:
            # NOTE: using eval for a simple calculator UI; input is limited
            # to button presses so risk is small in this context.
            result = eval(self.expr)
            self.expr = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expr)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expr = ""


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
