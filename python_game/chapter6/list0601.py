import tkinter


def click_btn():
    button["text"] = (i,"回クリックしました")
    
root = tkinter.Tk()
root.title("初めてのbutton")
root.geometry("800x600")
i = 0
button = tkinter.Button(root, text="クリックしてください",
                      font=("System",24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()
