from tkinter import*

class MyGuiPractice():
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        # rock paper scissor buttons
        self.rock_button = Button(master, text="Rock", width=10)
        self.rock_button.grid(row=4, column=0)
        self.paper_button = Button(master, text="Paper", width=10)
        self.paper_button.grid(row=4, column=1)
        self.scissor_button = Button(master, text="Scissors", width=10)
        self.scissor_button.grid(row=4, column=2)
        # win count labels
        self.comp_win_label = Label(master, text="Computer Wins:")
        self.comp_win_label.grid(row=0, column=0, sticky=E)
        self.user_win_label = Label(master, text="User Wins:")
        self.user_win_label.grid(row=1, column=0, sticky=E)
        self.draw_label = Label(master, text="Draws:")
        self.draw_label.grid(row=2, column=0, sticky=E)
        # win percent labels
        self.comp_win_perc_label = Label(master, text="Win %:")
        self.comp_win_perc_label.grid(row=0, column=2, sticky=W)
        self.user_win_perc_label = Label(master, text="Win %:")
        self.user_win_perc_label.grid(row=1, column=2, sticky=W)
        self.draw_perc_label = Label(master, text="Draw %:")
        self.draw_perc_label.grid(row=2, column=2, sticky=W)
        # Choice labels
        self.comp_choice_label = Label(master, text="Computers Move is:")
        self.comp_choice_label.grid(row=3, column=0, sticky=E)


root = Tk()
this_gui = MyGuiPractice(root)
root.mainloop()

