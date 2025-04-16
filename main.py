import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Game variables
youDict = {"r": 1, "p": 2, "s": 3}
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissors"}
choices = ["r", "p", "s"]
computer = random.choice([1, 2, 3])
your_choice = None

# Adjust element sizes based on screen dimensions
button_width = int(root.winfo_screenwidth() * 0.1)
button_height = int(root.winfo_screenheight() * 0.05)
image_size = int(root.winfo_screenwidth() * 0.15)

# Load images
try:
    rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((image_size, image_size)))
    paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((image_size, image_size)))
    scissors_img = ImageTk.PhotoImage(Image.open("sissor.png").resize((image_size, image_size)))
except FileNotFoundError as e:
    messagebox.showerror("Error", f"Image not found: {e}")
    root.destroy()

images = {1: rock_img, 2: paper_img, 3: scissors_img}

# Functions
def play(choice):
    global your_choice, computer
    your_choice = youDict[choice]
    computer = random.choice([1, 2, 3])
    determine_result()

def determine_result():
    global your_choice, computer
    if computer == your_choice:
        result = "It's a Draw!"
    elif (computer == 1 and your_choice == 2) or \
         (computer == 2 and your_choice == 3) or \
         (computer == 3 and your_choice == 1):
        result = "You win!"
    else:
        result = "You lose!"
    display_result(result)

def display_result(result):
    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a sub-frame for centering elements
    sub_frame = tk.Frame(frame, bg="#ffcccb")
    sub_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Display choices
    tk.Label(sub_frame, text="Your Choice:", font=("Comic Sans MS", 14), bg="#ffcccb", fg="#00008b").grid(row=0, column=0, padx=10)
    tk.Label(sub_frame, image=images[your_choice], bg="#ffcccb").grid(row=1, column=0, padx=10)
    tk.Label(sub_frame, text="Computer's Choice:", font=("Comic Sans MS", 14), bg="#ffcccb", fg="#00008b").grid(row=0, column=1, padx=10)
    tk.Label(sub_frame, image=images[computer], bg="#ffcccb").grid(row=1, column=1, padx=10)

    # Display result
    tk.Label(sub_frame, text=result, font=("Comic Sans MS", 16), fg="green" if "win" in result else "red", bg="#ffcccb").grid(row=2, column=0, columnspan=2, pady=10)

    # Play again and back to main menu buttons
    tk.Button(sub_frame, text="Play Again", command=reset_game, font=("Comic Sans MS", 12), bg="#ffb6c1").grid(row=3, column=0, pady=10, padx=10)
    tk.Button(sub_frame, text="Back to Main Menu", command=display_start_page, font=("Comic Sans MS", 12), bg="#ffb6c1").grid(row=3, column=1, pady=10, padx=10)

def reset_game():
    global your_choice, computer
    your_choice = None
    computer = random.choice([1, 2, 3])
    display_menu()

def display_menu():
    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a sub-frame for centering elements
    sub_frame = tk.Frame(frame, bg="#ffcccb", highlightthickness=0)
    sub_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Display instructions
    tk.Label(sub_frame, text="Choose Rock, Paper, or Scissors", font=("Comic Sans MS", int(root.winfo_screenwidth() * 0.02)), bg="#ffcccb", fg="#00008b").pack(pady=20)

    # Buttons for choices
    tk.Button(sub_frame, text="Rock", image=rock_img, compound="top", command=lambda: play("r"), bg="#ffb6c1", font=("Comic Sans MS", int(root.winfo_screenwidth() * 0.01))).pack(side="left", padx=20)
    tk.Button(sub_frame, text="Paper", image=paper_img, compound="top", command=lambda: play("p"), bg="#ffb6c1", font=("Comic Sans MS", int(root.winfo_screenwidth() * 0.01))).pack(side="left", padx=20)
    tk.Button(sub_frame, text="Scissors", image=scissors_img, compound="top", command=lambda: play("s"), bg="#ffb6c1", font=("Comic Sans MS", int(root.winfo_screenwidth() * 0.01))).pack(side="left", padx=20)

def start_game():
    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()
    # Display the game menu
    display_menu()

def display_start_page():
    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a sub-frame for centering elements
    sub_frame = tk.Frame(frame, bg="#ffcccb", highlightthickness=0)
    sub_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Display welcome message
    tk.Label(sub_frame, text="Welcome to Rock Paper Scissors!", font=("Comic Sans MS", int(root.winfo_screenwidth() * 0.025)), bg="#ffcccb", fg="#00008b").pack(pady=20)

    # Play button
    tk.Button(sub_frame, text="Play", command=start_game, font=("Comic Sans MS", int(root.winfo_screenwidth() * 0.02)), bg="#ffb6c1", width=button_width).pack(pady=20)

# Main frame with a vibrant background color
frame = tk.Frame(root, bg="#ffcccb")  # Light pink background
frame.pack(expand=True, fill="both")

# Display start page
display_start_page()

# Run the application
root.mainloop()