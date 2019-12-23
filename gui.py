from tkinter import *
import time

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


    def clear_screen(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No new messages available.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def exit_chat(self):
        exit()




root=Tk()
a = ChatWindowInterface(root)

screen_width = str(root.winfo_screenwidth())
screen_height = str(root.winfo_screenheight())
window_size = screen_width + "x" + screen_height

root.geometry(window_size)
root.title("ChromeOSDebugBot")

root.mainloop()