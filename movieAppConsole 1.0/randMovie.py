import tkinter as tk
import customtkinter, random
from tkinter import messagebox
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SHEET_ID = "1Gd9u1vd8zEpqJtLKmM5knBoQMbvz3T6qpOeffGN2oaI"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SERVICE_ACCOUNT_FILE = "credentials.py"

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build("sheets", "v4", credentials=credentials)

sheet = service.spreadsheets()

range = "Movies!$A:$Z"

class randMovieWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # create size of window
        self.geometry("400x600")
        # name the window
        self.title("Random Movie Screen")

        # add welcome lable to top of screen
        self.welcome_label = customtkinter.CTkLabel(self, text="Welcome! I am going to help you find a movie to watch!")
        self.welcome_label.pack(padx=10, pady=10)

        # add watch and recommend lable to top of screen
        self.w_and_r_label = customtkinter.CTkLabel(self, text="This section is for a random movie I have watched and recommend!")
        self.w_and_r_label.pack(padx=10, pady=10)

        # Create a StringVar to hold the watch text
        self.w_and_r_text = customtkinter.StringVar(value="")

        # Create the watch and recommend text
        self.w_r_label = customtkinter.CTkLabel(self, textvariable=self.w_and_r_text)
        self.w_r_label.pack(pady=20)

        # create a randomize recommend button
        self.w_and_r_button = customtkinter.CTkButton(self, text="Recommended Movies", command=self.getRandRecMovie)
        self.w_and_r_button.pack(side="top", padx=10, pady=10)

        # add random lable to top of screen
        self.rand_label = customtkinter.CTkLabel(self, text="This section is for a random movie I have not watched!")
        self.rand_label.pack(padx=10, pady=10)

        # Create a StringVar to hold the random text
        self.rand_text = customtkinter.StringVar(value="")

        # Create the label, associating it with the StringVar
        self.r_label = customtkinter.CTkLabel(self, textvariable=self.rand_text)
        self.r_label.pack(pady=20)

        # create a randomize movie button
        self.rand_button = customtkinter.CTkButton(self, text="Unseen Movies", command=self.getRandMovie)
        self.rand_button.pack(side="top", padx=10, pady=10)




    def getRandRecMovie(self):
        # read the current sheet and save it to the vulues list
        sheet_read = sheet.values().get(spreadsheetId = SHEET_ID, range=range).execute()
        values = sheet_read.get("values", [])
        # create a new empty list 
        movie_list = []
        # loop through list and if recommended and watched add to new list
        for x in values:
            if x[2] == "Yes" and x[3] == "Yes":
                movie_list.append(x)
        # get a random movie from the new list
        rand_index = random.randrange(len(movie_list))
        rand_movie = movie_list[rand_index]
        # set the random movie to the lable
        self.w_and_r_text.set(f"You should watch {rand_movie[0]} on {rand_movie[1]}")


    def getRandMovie(self):
        # read the current sheet and save it to the vulues list
        sheet_read = sheet.values().get(spreadsheetId = SHEET_ID, range=range).execute()
        values = sheet_read.get("values", [])
        # create a new empty list 
        movie_list = []
        # loop through list and if not watched add to new list
        for x in values:
            if x[2] == "No" and x[3] == "N/A":
                movie_list.append(x)
        # get a random movie from the new list
        rand_index = random.randrange(len(movie_list))
        rand_movie = movie_list[rand_index]
        # set the random movie to the lable
        self.rand_text.set(f"You should watch {rand_movie[0]} on {rand_movie[1]}")
