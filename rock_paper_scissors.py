"""Simple Rock-Paper-Scissors with a Tkinter GUI.

This replaces the text-based prompt with a small GUI providing
three buttons (Rock, Paper, Scissors), a score display and reset.
"""
import random
import tkinter as tk

OPTIONS = ["Rock", "Paper", "Scissors"]
WIN_MAP = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}


class RPSApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Rock Paper Scissors")
        root.geometry("420x220")

        self.player_score = 0
        self.comp_score = 0

        header = tk.Label(root, text="Rock · Paper · Scissors", font=("Segoe UI", 14))
        header.pack(pady=(12, 6))

        self.result_label = tk.Label(root, text="Make your move", font=("Segoe UI", 11))
        self.result_label.pack(pady=6)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=8)
        for opt in OPTIONS:
            b = tk.Button(btn_frame, text=opt, width=10, command=lambda o=opt: self.play(o))
            b.pack(side="left", padx=8)

        self.score_label = tk.Label(root, text=self._score_text(), font=("Segoe UI", 10))
        self.score_label.pack(pady=8)

        ctrl = tk.Frame(root)
        ctrl.pack(pady=6)
        tk.Button(ctrl, text="Reset", command=self.reset, width=10).pack()

    def _score_text(self) -> str:
        return f"You: {self.player_score}    Computer: {self.comp_score}"

    def play(self, player_choice: str) -> None:
        comp_choice = random.choice(OPTIONS)
        if player_choice == comp_choice:
            result = "Tie"
        elif WIN_MAP[player_choice] == comp_choice:
            result = "You win"
            self.player_score += 1
        else:
            result = "You lose"
            self.comp_score += 1

        self.result_label.config(text=f"You: {player_choice}  ·  Computer: {comp_choice}  →  {result}")
        self.score_label.config(text=self._score_text())

    def reset(self) -> None:
        self.player_score = 0
        self.comp_score = 0
        self.score_label.config(text=self._score_text())
        self.result_label.config(text="Make your move")


def main() -> None:
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
