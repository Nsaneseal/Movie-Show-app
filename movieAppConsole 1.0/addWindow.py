# not currently being used!!

import tkinter as tk
import customtkinter
from tkinter import messagebox
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SHEET_ID = "1Gd9u1vd8zEpqJtLKmM5knBoQMbvz3T6qpOeffGN2oaI"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SERVICE_ACCOUNT_FILE = "credentials.json"

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build("sheets", "v4", credentials=credentials)

sheet = service.spreadsheets()

range = "Sheet1!$A:$Z"

class addingWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # create size of window
        self.geometry("400x600")
        # name the window
        self.title("Adding Screen")


        # add welcome lable to top of screen
        self.welcome_label = customtkinter.CTkLabel(self, text="Welcome! What would you like to add?")
        self.welcome_label.pack(padx=10, pady=10)
        # name label 
        self.name_label = customtkinter.CTkLabel(self, text="Name of Movie/Show:")
        self.name_label.pack(padx=5, pady=5)
        # name entry box
        self.name_entryBox = customtkinter.CTkEntry(self, placeholder_text="Name")
        self.name_entryBox.pack()
        # optionMenu label 
        self.option_label = customtkinter.CTkLabel(self, text="Where can I watch:")
        self.option_label.pack(padx=5, pady=5)
        # optionMenu box
        self.options = ["Amazon Prime", "Flixtor", "HBO", "Netflix", "Peacock"]
        self.optionmenu_var = tk.StringVar(value="Netflix")
        self.optionmenu = customtkinter.CTkOptionMenu(self,values=self.options, variable=self.optionmenu_var)
        self.optionmenu.pack()
        # watched label 
        self.watched_label = customtkinter.CTkLabel(self, text="Have I watched it?")
        self.watched_label.pack(padx=5, pady=5)
        # watched radio button
        self.watch_radio_var = tk.StringVar(value="Yes")
        self.watch_radiobutton_yes = customtkinter.CTkRadioButton(self, text="Yes", variable= self.watch_radio_var, value="Yes")
        self.watch_radiobutton_yes.pack(pady=5)
        self.watch_radiobutton_no = customtkinter.CTkRadioButton(self, text="No", variable= self.watch_radio_var, value="No")
        self.watch_radiobutton_no.pack(pady=5)
        # recommend label 
        self.recommend_label = customtkinter.CTkLabel(self, text="Do I recommend it?")
        self.recommend_label.pack(padx=5, pady=5)
        # recommend radio button
        self.recommend_radio_var = tk.StringVar(value="Yes")
        self.recommend_radiobutton_yes = customtkinter.CTkRadioButton(self, text="Yes", variable= self.recommend_radio_var, value="Yes")
        self.recommend_radiobutton_yes.pack(pady=5)
        self.recommend_radiobutton_no = customtkinter.CTkRadioButton(self, text="No", variable= self.recommend_radio_var, value="No")
        self.recommend_radiobutton_no.pack(pady=5)
        self.recommend_radiobutton_no = customtkinter.CTkRadioButton(self, text="N/A", variable= self.recommend_radio_var, value="N/A")
        self.recommend_radiobutton_no.pack(pady=5)
        # button to add to sheet
        self.add_button = customtkinter.CTkButton(self, text="Add to Google Sheet", command=self.addToSheet)
        self.add_button.pack(pady=5)


    def addToSheet(self):
        # create variables and assign all user choices to it
        name = self.name_entryBox.get().title()
        location = self.optionmenu_var.get()
        watched = self.watch_radio_var.get()
        recommend = self.recommend_radio_var.get()
        # create list of the variables
        movies = [[name, location, watched, recommend]]
        # read the current google sheet
        sheet_read = sheet.values().get(spreadsheetId = SHEET_ID, range=range).execute()
        # add the values to a variable
        values = sheet_read.get("values", [])
        # loop through the new list and check if the movie already exist
        def isStringInList(name, values):
            for sublist in values:
                if name in sublist:
                    return True
            return False
        # if the movie does exist give message
        if isStringInList(name, values):
            messagebox.showinfo("Uh Oh", f"The movie {name} already exists")
        # if movie doesnt exist add it to the sheet
        else:
            request = sheet.values().append(spreadsheetId=SHEET_ID, range=range, valueInputOption='RAW', body={'values': movies}).execute()
