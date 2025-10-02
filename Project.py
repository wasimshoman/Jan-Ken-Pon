# a game (Rock, papper and sciceros)
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
  
#configuring the GUI
root = Tk()
root.title("Rock-Paper-Scissors Game!")
root.iconbitmap('face.ico')
root.geometry("400x400")
root.columnconfigure(0, weight=1)   

# locate the images 
try:
    photo_rock = ImageTk.PhotoImage(Image.open("Proj_images/Rock.png").resize((50, 50)))
    photo_paper = ImageTk.PhotoImage(Image.open("Proj_images/Paper.png").resize((50, 50)))
    photo_scissors = ImageTk.PhotoImage(Image.open("Proj_images/Scissors.png").resize((50, 50)))
except:
    photo_rock, photo_paper, photo_scissors = None, None, None

class choice_click():
    def __init__(self):
        # Initialize the score counters for both the paleyer and the counter
        self.counterYou = 0
        self.counterComputer = 0
        self.continue_game= False
        # Initialize the score label text
        label2.config(text=f'Score:\nYou: {self.counterYou}\nComputer: {self.counterComputer}')
    def click(self, choice):
        # check the winner according to the game's rules and return a message with the winner 
        self.choice= choice
        mylist = ["Rock", "Paper", "Scissors"]
        computer_choice= random.choice(mylist)
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
            self.counterYou +=1
        else:
            winner = "The computer wins!"
            icon_type = "warning"  
            self.counterComputer+=1
        
        # Display the result 
        messagebox.showinfo(
            title="Game Result",
            message=f"{winner}\n\nYou chose: {self.choice}\nComputer chose: {computer_choice}",
            icon=icon_type
        )
        label2.config(text=f'Score is: \n You {self.counterYou}\n The computer {self.counterComputer}')
        # check if the player wants to continoue after his first win/lost
        if self.counterComputer + self.counterYou >= 1 and self.continue_game == False:
            play_again = messagebox.askyesno(title='Continoue?', message="Do you want to play another round?")
            
            if not play_again:
                # If the player clicks 'No' then quit the application otherwise continoue 
                root.quit()
            else:
                self.continue_game= True

# styling the buttons for the images
button_style = {
    "font": ("Helvetica", 14, "bold"),
    "bg": "#f0f0f0",
    "fg": "black",
    "activebackground": "#dcdcdc",
    "activeforeground": "black",
    "bd": 2,
    "relief": "groove","width": 150 
}
# a message for the palyer
label=Label(root, text= 'Choose Rock, Paper or Scissors!')
label.grid(row=0, column=0, pady=10)
# a label with counter for the winner
label2=Label(root, text= '', font=("Helvetica", 12))
label2.grid(row=5, column=0, pady=20, padx=10)

game = choice_click()
# the buttons with the images for the options
but_Rock = Button(root, text="Rock", image=photo_rock, compound='left', **button_style, command=lambda: game.click("Rock"))
but_paper= Button(root, text="Paper", image=photo_paper, compound='left',  **button_style,command=lambda: game.click("Paper"))
but_Scissor = Button(root, text="Scissor", image=photo_scissors, compound='left', **button_style, command=lambda: game.click("Scissors"))

#exit button
but_exit= Button(root, text="Exit Game!",  **button_style, command=root.quit)
#locations of the buttons
but_Rock.grid(row=1, column=0, pady=5)
but_paper.grid(row=2, column=0, pady=5)
but_Scissor.grid(row=3, column=0, pady=5)
but_exit.grid(row=4, column=0, pady=5)

root.mainloop()
