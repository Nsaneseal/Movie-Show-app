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

range = "Shows!$A:$Z"

class randShowWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # create size of window
        self.geometry("400x600")
        # name the window
        self.title("Random Show Screen")

        # add welcome lable to top of screen
        self.welcome_label = customtkinter.CTkLabel(self, text="Welcome! I am going to help you find a Show to watch!")
        self.welcome_label.pack(padx=10, pady=10)

        # add welcome lable to top of screen
        self.w_and_r_label = customtkinter.CTkLabel(self, text="This section is for a random Show I have watched and recommend!")
        self.w_and_r_label.pack(padx=10, pady=10)

        # Create a StringVar to hold the label text
        self.w_and_r_text = customtkinter.StringVar(value="")

        # Create the label, associating it with the StringVar
        self.w_r_label = customtkinter.CTkLabel(self, textvariable=self.w_and_r_text)
        self.w_r_label.pack(pady=20)

        # create a randomize show button
        self.w_and_r_button = customtkinter.CTkButton(self, text="Recommended Shows", command=self.getRandRecShow)
        self.w_and_r_button.pack(side="top", padx=10, pady=10)

        # add welcome lable to top of screen
        self.rand_label = customtkinter.CTkLabel(self, text="This section is for a random Show I have not watched!")
        self.rand_label.pack(padx=10, pady=10)

        # Create a StringVar to hold the label text
        self.rand_text = customtkinter.StringVar(value="")

        # Create the label, associating it with the StringVar
        self.r_label = customtkinter.CTkLabel(self, textvariable=self.rand_text)
        self.r_label.pack(pady=20)

        # create a randomize show button
        self.rand_button = customtkinter.CTkButton(self, text="Unseen Shows", command=self.getRandShow)
        self.rand_button.pack(side="top", padx=10, pady=10)





    def getRandRecShow(self):
        sheet_read = sheet.values().get(spreadsheetId = SHEET_ID, range=range).execute()
        values = sheet_read.get("values", [])

        Show_list = []

        for x in values:
            if x[2] == "Yes" and x[3] == "Yes":
                Show_list.append(x)
        
        rand_index = random.randrange(len(Show_list))
        rand_Show = Show_list[rand_index]

        self.w_and_r_text.set(f"You should watch {rand_Show[0]} on {rand_Show[1]}")


    def getRandShow(self):
        sheet_read = sheet.values().get(spreadsheetId = SHEET_ID, range=range).execute()
        values = sheet_read.get("values", [])

        Show_list = []

        for x in values:
            if x[2] == "No" and x[3] == "N/A":
                Show_list.append(x)
        
        rand_index = random.randrange(len(Show_list))
        rand_Show = Show_list[rand_index]

        self.rand_text.set(f"You should watch {rand_Show[0]} on {rand_Show[1]}")
