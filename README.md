# 🪨📄✂️ Rock-Paper-Scissors Game

A simple, graphical implementation of the classic game "Rock, Paper, Scissors" built using Python's `tkinter` library for the GUI and `Pillow` for image handling.

## ✨ Features

* **Interactive GUI:** Play directly in a modern window application.

* **Image Integration:** Uses custom images for Rock, Paper, and Scissors options.

* **Real-time Scoring:** Tracks and displays the scores for the Player and the Computer.

* **Instant Feedback:** Uses popup message boxes to show the result of each round (Win, Loss, or Tie).

## 🛠️ Prerequisites

To run this game, you need:

1. **Python 3.x**

2. The **Pillow (PIL)** library for handling and displaying images.

3. The necessary **image assets** (`.png` files) in the correct folder structure.

## 📦 Installation and Setup

### 1. Install Dependencies

The `tkinter` library usually comes pre-installed with Python. You only need to install `Pillow`:

pip install Pillow


### 2. File Structure

The script is configured to look for the image assets in a specific subdirectory. Ensure your project directory is structured as follows:

rock-paper-scissors-game/
├── app.py              # The main game script (where your code is saved)
├── face.ico            # Custom window icon file
└── Proj_images/
├── Rock.png        # Image for Rock button
├── Paper.png       # Image for Paper button
└── Scissors.png    # Image for Scissors button


**Note:** If you don't have the image files or the `face.ico` file, you must either create them and place them in the correct paths or modify the image loading lines in `app.py`:

Original lines requiring files:
photo_rock = ImageTk.PhotoImage(Image.open("Proj_images/Rock.png").resize((50, 50)))
root.iconbitmap('face.ico')


## ▶️ How to Run the Game

1. Navigate to the root directory of the project in your terminal:

cd rock-paper-scissors-game/


2. Run the Python script:

python app.py


The game window will open, and you can start playing!

## 🕹️ Gameplay

Simply click on one of the three buttons (**Rock**, **Paper**, or **Scissor**) to make your choice. A message box will pop up displaying the computer's choice and the winner, and the score tracker will update automatically.
