from tkinter import *
from data import Data

BACKGROUND_COLOR = "#B1DDC6"


class Interface:

    def __init__(self):
        # Interface
        self.windows = Tk()
        self.canvas = Canvas()
        # Images
        self.check_mark_image = PhotoImage(file="images/right.png")
        self.wrong_image = PhotoImage(file="images/wrong.png")
        self.card_frond_image = PhotoImage(file="images/card_front.png")
        self.card_back = PhotoImage(file="images/card_back.png")
        # Buttons
        self.wrong_button = self.create_button(self.wrong_image, 0, 1)
        self.right_button = self.create_button(self.check_mark_image, 1, 1)
        # Data
        self.data = Data()
        # Wait time
        self.wait_time = self.windows.after(3000, self.new_card_text, True)
        self.timer_count = self.windows

    def set_up_windows(self):
        self.windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.windows.resizable(False, False)
        self.windows.title("Flashy")

    def set_up_canvas(self):
        self.canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.create_image(400, 263, image=self.card_frond_image, tags="card")
        # Create Text
        self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), tags="card_title")
        self.canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), tags="word")

        self.canvas.grid(column=0, row=0, columnspan=2)

    def timer(self, count):
        self.canvas.create_text(400, 400, text="", font=("Ariel", 40, "bold"), tags="timer")
        self.canvas.itemconfig("timer", text=f"{count}")
        if count > 0:
            self.timer_count = self.windows.after(1000, self.timer, count - 1)

    def new_card_text(self, remove=False):
        self.windows.after_cancel(self.wait_time)
        self.windows.after_cancel(self.timer_count)
        self.canvas.delete("reset")
        self.canvas.itemconfig("card", image=self.card_frond_image)
        self.canvas.itemconfig("card_title", text="English", fill="black")
        # Start Timer
        self.timer(count=3)

        # Get random pick word
        word = self.data.random_pick()
        # Reset data if there is not more words
        if word == 0:
            self.canvas.itemconfig("word", text="Congratulations You Learned All Words", fill="black",
                                   font=("Ariel", 25, "bold"))
            self.canvas.create_text(400, 350, text="Press ✅ To Reset words and continue", font=("Ariel", 25, "bold"),
                                    tags="reset")
            self.data.reset_words()
        # Print in screen word
        else:
            self.canvas.itemconfig("word", text=word["English"], fill="black", font=("Ariel", 60, "bold"))
            # Create words to learn
            if remove:
                self.data.words_to_learn(word)

        # Wait 3 seconds to flip the card and show answer
        self.wait_time = self.windows.after(3300, self.flip_card, word)

    def flip_card(self, word):
        self.canvas.delete("timer")
        self.canvas.itemconfig("card", image=self.card_back)
        self.canvas.itemconfig("card_title", fill="white", text="Spanish")
        self.canvas.itemconfig("word", fill="white", text=word["Spanish"])
        self.canvas.itemconfig("word", fill="white")

    @staticmethod
    def create_button(image, column, row):
        button = Button(image=image, highlightthickness=0, borderwidth=0)
        button.grid(column=column, row=row)
        return button
