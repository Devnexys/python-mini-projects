import tkinter as tk
from tkinter import messagebox
import random


class PigGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Pig Game 🎮")
        self.root.geometry("600x400")
        self.root.configure(bg="#282a36")  # Dark background for a gaming vibe

        self.players = []
        self.current_player = 0
        self.current_score = 0
        self.max_score = 50

        self.setup_game()

    def setup_game(self):
        self.frame = tk.Frame(self.root, bg="#282a36")
        self.frame.pack(pady=20)

        title = tk.Label(
            self.frame,
            text="Welcome to the Pig Game!",
            font=("Comic Sans MS", 24, "bold"),
            fg="#ff79c6",
            bg="#282a36",
        )
        title.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(
            self.frame,
            text="Enter number of players (2-4):",
            font=("Comic Sans MS", 14),
            fg="#f8f8f2",
            bg="#282a36",
        ).grid(row=1, column=0, padx=10, pady=5)

        self.players_entry = tk.Entry(self.frame, font=("Comic Sans MS", 14))
        self.players_entry.grid(row=1, column=1, padx=10, pady=5)

        start_button = tk.Button(
            self.frame,
            text="Start Game",
            font=("Comic Sans MS", 14, "bold"),
            fg="#282a36",
            bg="#50fa7b",
            activebackground="#69ff94",
            command=self.start_game,
        )
        start_button.grid(row=2, column=0, columnspan=2, pady=10)

    def start_game(self):
        try:
            players = int(self.players_entry.get())
            if 2 <= players <= 4:
                self.players = [0 for _ in range(players)]
                self.frame.destroy()
                self.game_screen()
            else:
                messagebox.showerror("Error", "Number of players must be between 2 and 4.")
        except ValueError:
            messagebox.showerror("Error", "Invalid number of players.")

    def roll_dice(self):
        value = random.randint(1, 6)
        if value == 1:
            self.current_score = 0
            self.switch_player()
            messagebox.showinfo("Rolled a 1!", "You rolled a 1! Turn over.")
        else:
            self.current_score += value
            self.score_label.config(
                text=f"🎲 Rolled: {value}  |  Current Score: {self.current_score}"
            )

    def hold(self):
        self.players[self.current_player] += self.current_score
        if self.players[self.current_player] >= self.max_score:
            messagebox.showinfo(
                "Game Over",
                f"🎉 Player {self.current_player + 1} wins with {self.players[self.current_player]} points!",
            )
            self.root.quit()
        else:
            self.switch_player()

    def switch_player(self):
        self.current_score = 0
        self.current_player = (self.current_player + 1) % len(self.players)
        self.update_status()

    def update_status(self):
        self.status_label.config(
            text=f"🎮 Player {self.current_player + 1}'s Turn\n🎯 Total Score: {self.players[self.current_player]}"
        )
        self.score_label.config(text="🎲 Current Roll: -  |  Current Score: 0")

    def game_screen(self):
        self.frame = tk.Frame(self.root, bg="#282a36")
        self.frame.pack(pady=20)

        self.status_label = tk.Label(
            self.frame,
            text=f"🎮 Player 1's Turn\n🎯 Total Score: 0",
            font=("Comic Sans MS", 16),
            fg="#ffb86c",
            bg="#282a36",
        )
        self.status_label.pack(pady=10)

        self.score_label = tk.Label(
            self.frame,
            text="🎲 Current Roll: -  |  Current Score: 0",
            font=("Comic Sans MS", 14),
            fg="#f1fa8c",
            bg="#282a36",
        )
        self.score_label.pack(pady=10)

        button_frame = tk.Frame(self.frame, bg="#282a36")
        button_frame.pack(pady=20)

        roll_button = tk.Button(
            button_frame,
            text="🎲 Roll",
            font=("Comic Sans MS", 14, "bold"),
            fg="#282a36",
            bg="#ff5555",
            activebackground="#ff6e6e",
            command=self.roll_dice,
        )
        roll_button.grid(row=0, column=0, padx=20)

        hold_button = tk.Button(
            button_frame,
            text="🏁 Hold",
            font=("Comic Sans MS", 14, "bold"),
            fg="#282a36",
            bg="#8be9fd",
            activebackground="#69d9ff",
            command=self.hold,
        )
        hold_button.grid(row=0, column=1, padx=20)


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = PigGame(root)
    root.mainloop()
