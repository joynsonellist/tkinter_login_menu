import tkinter

login_window = tkinter.Tk()
login_window.title("Login")
# ======================================== #
usernames = ["Username"] "EDIT"
passwords = ["Password"] "EDIT"
# ======================================== #


def confirm_login():
    global login_window
    username = login_window_entry_username.get()
    password = login_window_entry_password.get()
    login_window_pass_rate = 0

    if username in usernames:
        login_window_pass_rate += 1
    else:
        login_window_outcome = tkinter.Label(login_window, text="Failure: Username is incorrect")
        login_window_outcome.grid(column=1, row=2)

    if login_window_pass_rate == 1:
        if password in passwords:
            login_window_pass_rate += 1
        else:
            login_window_outcome = tkinter.Label(login_window, text="Failure: Password is incorrect")
            login_window_outcome.grid(column=1, row=2)

    if login_window_pass_rate == 2:
        login_window_outcome = tkinter.Label(login_window, text="=======Success!=======")
        login_window_outcome.grid(column=1, row=2)
    else:
        pass


# ======================================== #
login_window_label_username = tkinter.Label(login_window, text="Username:")
login_window_entry_username = tkinter.Entry(login_window)
# ======================================== #
login_window_label_password = tkinter.Label(login_window, text="Password:")
login_window_entry_password = tkinter.Entry(login_window, show="*")
# ======================================== #
login_window_button_confirm = tkinter.Button(login_window, text="Confirm", command=confirm_login)
# ======================================== #
login_window_label_username.grid(column=0, row=0)
login_window_entry_username.grid(column=1, row=0)
login_window_label_password.grid(column=0, row=1)
login_window_entry_password.grid(column=1, row=1)
login_window_button_confirm.grid(column=0, row=2)

tkinter.mainloop()
