from tkinter import *
from chat import get_response, bot_name
import login

BG_GRAY = "#3d5a80"
BG_COLOR = "#e0fbfc"
TEXT_COLOR = "#EAECEE"
TEXT_BLACK = "#293241"

FONT = "Helvetica 13 italic"
FONT_BOLD = "Helvetica 14 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Interachat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, font=('Helvetica', 15, 'bold'), bg=BG_GRAY, fg=TEXT_COLOR,
                           text="Welcome",  pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_BLACK,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=0.99, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.979)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # logout button
        logout_button = Button(head_label, border=0, text="Logout", font=('Helvetica', 13), fg=TEXT_COLOR, width=20, bg=BG_GRAY,
                               command=lambda: self.logout_func())
        logout_button.place(relx=0.84, rely=0.03,
                            relheight=0.999, relwidth=0.18)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_COLOR,
                               fg=TEXT_BLACK, font=FONT)
        self.msg_entry.place(relwidth=0.73, relheight=0.05,
                             rely=0.015, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, fg='white',  bg="#659aba",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.78, rely=0.02, relheight=0.04, relwidth=0.21)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    def logout_func(self):
        f = open('isLog.txt', "w")
        to_write = 'Logged Off,'
        self.window.destroy()
        f.write(to_write)
        f.close()

        login.login()


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
