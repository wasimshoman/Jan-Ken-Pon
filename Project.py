# a game (Rock, papper and sciceros)
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
  

root = Tk()
root.title("Rock-paper-scissors Game!")
root.iconbitmap('face.ico')
root.geometry("400x400")
# To center the buttons, we configure the column to expand when the window is resized.
root.columnconfigure(0, weight=1)   

# locate the images 
photo_rock = ImageTk.PhotoImage(Image.open("Proj_images/Rock.png").resize((50, 50)))
photo_paper = ImageTk.PhotoImage(Image.open("Proj_images/Paper.png").resize((50, 50)))
photo_scissors = ImageTk.PhotoImage(Image.open("Proj_images/Scissors.png").resize((50, 50)))
# Initialize the score counters for both the paleyer and the counter
counterYou=0
counterComputer=0

def click(choice):
    # check the winner according to the game's rules and return a message with the winner 
    global counterYou
    global counterComputer

    mylist = ["Rock", "Paper", "Scissors"]
    computer_choice= random.choices(mylist)[0]
    winner = ""
    icon_type = ""

    if choice == computer_choice:
        winner = "It's a tie!"
        icon_type = "info" 
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        winner = "You win!"
        icon_type = "info"  
        counterYou +=1
    else:
        winner = "The computer wins!"
        icon_type = "warning"  
        counterComputer+=1
    
    # Display the result 
    messagebox.showinfo(
        title="Game Result",
        message=f"{winner}\n\nYou chose: {choice}\nComputer chose: {computer_choice}",
        icon=icon_type
    )
    label2.config(text=f'Score is \n you {counterYou}\n The computer {counterComputer}')

# styling the buttons for the images
button_style = {
    "font": ("Helvetica", 14, "bold"),
    "bg": "#f0f0f0",
    "fg": "black",
    "activebackground": "#dcdcdc",
    "activeforeground": "black",
    "bd": 2,
    "relief": "groove",
}
# a message for the palyer
label=Label(root, text= 'Choose Rock, Paper or Scissors!')
label.grid(row=0, column=0, pady=10)

# the buttons with the images for the options
but_Rock = Button(root, text="Rock", image=photo_rock, compound='left', **button_style, command=lambda: click("Rock"))
but_paper= Button(root, text="Paper", image=photo_paper, compound='left',  **button_style,command=lambda: click("Paper"))
but_Scissor = Button(root, text="Scissor", image=photo_scissors, compound='left', **button_style, command=lambda: click("Scissors"))

#exit button
but_exit= Button(root, text="Exit", compound='left', **button_style, command=root.quit)

#locations of the buttons
but_Rock.grid(row=1, column=0, pady=5)
but_paper.grid(row=2, column=0, pady=5)
but_Scissor.grid(row=3, column=0, pady=5)
but_exit.grid(row=4, column=0, pady=5)

# a label with counter for the winner
label2=Label(root, text= '')
label2.grid(row=5, column=0, pady=20, padx=10)



root.mainloop()
