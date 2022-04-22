import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("SecureWay")
        #setting window size
        width=700
        height=498
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_611=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_611["font"] = ft
        GLabel_611["fg"] = "#333333"
        GLabel_611["justify"] = "center"
        GLabel_611["text"] = "Enter Max Number of people"
        GLabel_611.place(x=20,y=60,width=174,height=30)

        GButton_866=tk.Button(root)
        GButton_866["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_866["font"] = ft
        GButton_866["fg"] = "#000000"
        GButton_866["justify"] = "center"
        GButton_866["text"] = "Done"
        GButton_866.place(x=450,y=60,width=69,height=30)
        GButton_866["command"] = self.GButton_866_command

        GLineEdit_89=tk.Entry(root)
        GLineEdit_89["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_89["font"] = ft
        GLineEdit_89["fg"] = "#333333"
        GLineEdit_89["justify"] = "center"
        GLineEdit_89["text"] = ""
        GLineEdit_89.place(x=240,y=60,width=159,height=30)

        GMessage_197=tk.Message(root)
        GMessage_197["bg"] = "#ff2424"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_197["font"] = ft
        GMessage_197["fg"] = "#333333"
        GMessage_197["justify"] = "center"
        GMessage_197["text"] = "Unsafe"
        GMessage_197.place(x=310,y=280,width=292,height=216)

        GMessage_574=tk.Message(root)
        GMessage_574["bg"] = "#33e715"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_574["font"] = ft
        GMessage_574["fg"] = "#333333"
        GMessage_574["justify"] = "center"
        GMessage_574["text"] = "Safe"
        GMessage_574.place(x=0,y=280,width=310,height=216)

        GButton_916=tk.Button(root)
        GButton_916["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_916["font"] = ft
        GButton_916["fg"] = "#000000"
        GButton_916["justify"] = "center"
        GButton_916["text"] = "Start Camera"
        GButton_916.place(x=150,y=200,width=95,height=57)
        GButton_916["command"] = self.GButton_916_command

        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#000000"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Button"
        GButton_365.place(x=310,y=200,width=95,height=57)
        GButton_365["command"] = self.GButton_365_command

    def GButton_866_command(self):
        print("command")


    def GButton_916_command(self):
        print("command")


    def GButton_365_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
