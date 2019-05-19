#tkinter 练习
#%%
import tkinter
import tkinter.messagebox


class Messageapp:
    def __init__(self, parent):
        self.flag = True
        parent.title('game')
        parent.geometry('240x160')
        self.label = tkinter.Label(parent,
                                   text='Hello, world',
                                   font="arial-32",
                                   fg='red')
        self.label.pack(expand=1)
        #* container for buttons
        panel = tkinter.Frame(parent)
        button1 = tkinter.Button(panel,
                                 text='modify',
                                 command=self.change_label_text)
        button1.pack(side='left')
        button2 = tkinter.Button(panel,
                                 text='quit',
                                 command=lambda: self.confirm_to_quit(parent))
                                 #* if want to pass arguments in comman,
                                 #* lambda function is a good choice
        button2.pack(side='right')
        panel.pack(side='bottom')

    def change_label_text(self):
        color, msg = ('red',
                      'Hello world!') if self.flag else ('blue',
                                                         'Goodbye, world')
        self.label.config(text=msg, fg=color)

    def confirm_to_quit(self, parent):
        if tkinter.messagebox.askokcancel('Notice', 'Are you sure to quit?'):
            parent.quit()


def main():
    root = tkinter.Tk()
    myapp = Messageapp(root)
    root.mainloop()


if __name__ == '__main__':
    main()

#%%
