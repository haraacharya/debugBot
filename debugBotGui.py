from tkinter import *
import time
from tkinter import messagebox as msgbox
import threading

saved_username = ["You"]

class ChatWindowInterface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.window_bg = "#FFFFFFFF"
        self.window_fg = "#00000000"
        self.font = "Verdana 12"
        menu = Menu(self.master)
        self.master.config(menu = menu, bd=2)
        
        #Add customized Menu bar
        file = Menu(menu, tearoff = 0)
        menu.add_cascade(label = "File", menu = file)
        file.add_command(label = "Clear off chat", command = self.clear_screen)
        file.add_command(label = "Exit", command = self.exit_chat)

        help = Menu(menu, tearoff = 0)
        menu.add_cascade(label = "Help", menu = help)
        help.add_command(label = "About DebugBot", command = self.about_msg)

        self.showchatboxframe = Frame(self.master, bd=4)
        self.showchatboxframe.pack(expand=True, fill=BOTH)

        self.showchatbox_scrollbar = Scrollbar(self.showchatboxframe, bd=0)
        self.showchatbox_scrollbar.pack(fill=Y, side=RIGHT)

        self.showchatbox = Text(self.showchatboxframe, yscrollcommand=self.showchatbox_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 12", relief=GROOVE,
                             width=10, height=1)
        self.showchatbox.pack(expand=True, fill=BOTH)
        self.showchatbox_scrollbar.config(command=self.showchatbox.yview)

        # user input frame
        self.user_input_frame = Frame(self.master, bd=1)
        self.user_input_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.user_input_box = Entry(self.user_input_frame, bd=2, justify=LEFT)
        self.user_input_box.pack(fill=X, padx=4, pady=4, ipady=8)
        
        # frame containing send msg button
        self.send_msg_button_frame = Frame(self.master, bd=0)
        self.send_msg_button_frame.pack(fill=BOTH)
        self.send_msg_button = Button(self.send_msg_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_input_message(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_msg_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_input_message)


    def clear_screen(self):
        self.showchatbox.config(state=NORMAL)
        self.last_sent_label(date="No new messages available.")
        self.showchatbox.delete(1.0, END)
        self.showchatbox.delete(1.0, END)
        self.showchatbox.config(state=DISABLED)

    def last_sent_label(self, date):
        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.user_input_box, font="Verdana 7", text=date, bg=self.window_bg, fg=self.window_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)



    def exit_chat(self):
        exit()

    def about_msg(self):
        msgbox.showinfo("DebugBot v1.0.0",'DebugBot is a chatbot to help debug chromeOS DUT issues. \nIt is based on retrival-based NLP.\nGUI is based on Tkinter.\nIt can answer questions regarding chromeOs build env issues.\nIt can find out issues in remote system based on system ip with asyncssh module.')

    def send_input_message(self, message):
        user_input = self.user_input_box.get()
        processed_user_input = "You : " + user_input + "\n"
        self.showchatbox.configure(state=NORMAL)
        self.showchatbox.insert(END, processed_user_input)
        self.showchatbox.configure(state=DISABLED)
        self.showchatbox.see(END)
        # bot_output=botchat(user_input)
        bot_output = "test"
        processed_bot_output = "DebugBot : " + bot_output + "\n"
        self.showchatbox.configure(state=NORMAL)
        self.showchatbox.insert(END, processed_bot_output)
        self.showchatbox.configure(state=DISABLED)
        self.showchatbox.see(END)
        self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.user_input_box.delete(0,END)
        time.sleep(0)
        t2 = threading.Thread(target=self.playResponce, args=(bot_output,))
        t2.start()
        #return bot_output


root=Tk()
a = ChatWindowInterface(root)

screen_width = str(int(root.winfo_screenwidth()/4))
screen_height = str(int(root.winfo_screenheight()/2))
window_size = screen_width + "x" + screen_height

root.geometry(window_size)
root.title("ChromeOSDebugBot")

root.mainloop()
