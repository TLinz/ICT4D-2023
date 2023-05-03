#Author Leo

import tkinter as tk
from tkinter import ttk, messagebox

# Define global variables to store poll results. A simple application interface that does not yet read telephone polling data.
yes_votes = 0
no_votes = 0
poll_data = []

# Defining the interface
root = tk.Tk()
root.title("EasyVote")
root.geometry("800x600")

main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_login():
    clear_frame()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username == 'leo' and password == '1234':
            show_manage_polls()
        else:
            error_label.config(text="Invalid username or password")
            error_label.grid(column=1, row=3)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)

    username_label = ttk.Label(main_frame, text="Username:")
    username_label.grid(column=0, row=0)

    username_entry = ttk.Entry(main_frame)
    username_entry.grid(column=1, row=0)

    password_label = ttk.Label(main_frame, text="Password:")
    password_label.grid(column=0, row=1)

    password_entry = ttk.Entry(main_frame, show="*")
    password_entry.grid(column=1, row=1)

    login_button = ttk.Button(main_frame, text="Login", command=login)
    login_button.grid(column=1, row=2)

    error_label = ttk.Label(main_frame, text="")
    error_label.grid(column=1, row=3)

def show_manage_polls():
    clear_frame()

    # Function to show poll creation form
    def show_create_poll():
        clear_frame()

        def create_poll():
            global poll_data
            start_date = start_date_entry.get()
            end_date = end_date_entry.get()
            phone_number = phone_number_entry.get()

            poll_data.append({'start_date': start_date, 'end_date': end_date, 'phone_number': phone_number})

            # Show a message box to indicate success
            messagebox.showinfo("Success", "Poll created successfully")
            show_manage_polls()

        def go_back():
            show_manage_polls()

        # Create form elements
        start_date_label = ttk.Label(main_frame, text="Start Date:")
        start_date_label.grid(column=0, row=0)
        start_date_entry = ttk.Entry(main_frame)
        start_date_entry.grid(column=1, row=0)

        end_date_label = ttk.Label(main_frame, text="End Date:")
        end_date_label.grid(column=0, row=1)
        end_date_entry = ttk.Entry(main_frame)
        end_date_entry.grid(column=1, row=1)

        phone_number_label = ttk.Label(main_frame, text="Phone Number:")
        phone_number_label.grid(column=0, row=2)
        phone_number_entry = ttk.Entry(main_frame)
        phone_number_entry.grid(column=1, row=2)

        create_button = ttk.Button(main_frame, text="Create", command=create_poll)
        create_button.grid(column=1, row=3)

        back_button = ttk.Button(main_frame, text="Back", command=go_back)
        back_button.grid(column=0, row=3)

    # Function to show poll results
    def show_poll_results():
        clear_frame()

        yes_label = ttk.Label(main_frame, text="Yes:")
        yes_label.grid(column=0, row=0)
        yes_votes_label = ttk.Label(main_frame, text=str(yes_votes))
        yes_votes_label.grid(column=1, row=0)

        no_label = ttk.Label(main_frame, text="No:")
        no_label.grid(column=0, row=1)
        no_votes_label = ttk.Label(main_frame, text=str(no_votes))
        no_votes_label.grid(column=1, row=1)

        back_button = ttk.Button(main_frame, text="Back", command=show_manage_polls)
        back_button.grid(column=1, row=2)

    create_poll_button = ttk.Button(main_frame, text="Create Poll", command=show_create_poll)
    create_poll_button.grid(column=0, row=0)

    view_results_button = ttk.Button(main_frame, text="View Results", command=show_poll_results)
    view_results_button.grid(column=1, row=0)

    logout_button = ttk.Button(main_frame, text="Logout", command=show_login)
    logout_button.grid(column=2, row=0)

    for i, poll in enumerate(poll_data):
        poll_label = ttk.Label(main_frame, text=f"Poll {i+1}: {poll['start_date']} - {poll['end_date']} ({poll['phone_number']})")
        poll_label.grid(column=0, row=i+1, columnspan=3)

show_login()
root.mainloop()

