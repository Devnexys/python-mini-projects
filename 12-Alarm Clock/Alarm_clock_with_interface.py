import tkinter as tk
from tkinter import ttk
from playsound import playsound
import threading
import time

class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beautiful Alarm Clock")
        self.root.geometry("400x300")
        self.root.config(bg="lightblue")

        # Alarm setup
        self.minutes = tk.IntVar()
        self.seconds = tk.IntVar()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title = tk.Label(self.root, text="Set Your Alarm", font=("Arial", 18, "bold"), bg="lightblue")
        title.pack(pady=20)

        # Time Input Frame
        time_frame = tk.Frame(self.root, bg="lightblue")
        time_frame.pack(pady=10)

        tk.Label(time_frame, text="Minutes:", font=("Arial", 12), bg="lightblue").grid(row=0, column=0, padx=10)
        tk.Entry(time_frame, textvariable=self.minutes, font=("Arial", 12), width=5).grid(row=0, column=1)

        tk.Label(time_frame, text="Seconds:", font=("Arial", 12), bg="lightblue").grid(row=0, column=2, padx=10)
        tk.Entry(time_frame, textvariable=self.seconds, font=("Arial", 12), width=5).grid(row=0, column=3)

        # Start Button
        start_button = tk.Button(self.root, text="Start Alarm", font=("Arial", 14), bg="green", fg="white", command=self.start_alarm_thread)
        start_button.pack(pady=20)

        # Countdown Label
        self.countdown_label = tk.Label(self.root, text="", font=("Arial", 14), bg="lightblue")
        self.countdown_label.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

    def start_alarm_thread(self):
        # Start alarm in a separate thread to keep the GUI responsive
        threading.Thread(target=self.start_alarm).start()

    def start_alarm(self):
        total_seconds = self.minutes.get() * 60 + self.seconds.get()

        if total_seconds <= 0:
            self.countdown_label.config(text="Please enter a valid time!")
            return

        self.progress["maximum"] = total_seconds
        elapsed = 0

        while elapsed < total_seconds:
            time_left = total_seconds - elapsed
            minutes_left = time_left // 60
            seconds_left = time_left % 60

            # Update countdown label
            self.countdown_label.config(text=f"Time left: {minutes_left:02d}:{seconds_left:02d}")

            # Update progress bar
            self.progress["value"] = elapsed
            self.root.update()

            time.sleep(1)  # Pause for 1 second
            elapsed += 1

        # Alarm sound
        self.countdown_label.config(text="Time's up!")
        playsound("alarm.mp3")

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()
