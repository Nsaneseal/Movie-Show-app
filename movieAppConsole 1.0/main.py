import tkinter as tk
from tkinter import *
import customtkinter
import randMovie, randShow

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the size of the window
        self.geometry("500x400")
        # set the title of the window
        self.title("Random Movie/Show Generator")

        # create a label
        self.watchLabel = customtkinter.CTkLabel(self, text="Watch this: ")
        self.watchLabel.pack(side="top", padx=10, pady=10)

        # create a randomize show button
        self.rec_movie_button = customtkinter.CTkButton(self, text="Recommended Movie", command=self.open_movieWindow)
        self.rec_movie_button.pack(side="top", padx=10, pady=10)

        # create a randomize show button
        self.rec_show_button = customtkinter.CTkButton(self, text="Recommended Show", command=self.open_showWindow)
        self.rec_show_button.pack(side="top", padx=10, pady=10)

        self.toplevel_window = None

    def open_movieWindow(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = randMovie.randMovieWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_showWindow(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = randShow.randShowWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


    

# call the application
app = App()

# keep the window open until the user closes
app.mainloop()


