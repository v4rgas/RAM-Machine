import tkinter
import os
import tkinter.ttk as ttk
from datetime import datetime

from ram import run_program, input_to_program, get_log


class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tkinter.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

    def get_input(self):
        input = self.txt.get('1.0', 'end')
        return input


def my_click():
    input = combo.get_input()
    mem = memoria.get()
    program = input_to_program(input, mem)
    output = run_program(program)

    my_label.configure(text='OUTPUT: ' + str(output))


# function to open a new window
# on a button click
def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    newWindow = tkinter.Toplevel(main_window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("LOG")

    # sets the geometry of toplevel
    newWindow.geometry("500x500")

    # A Label widget to show in toplevel
    tkinter.Label(newWindow,
                  text="LOG del programa").pack()

    scrollBar = tkinter.Scrollbar(newWindow)
    text = tkinter.Text(newWindow, height=10, width=50)
    scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    text.pack(side=tkinter.LEFT, fill=tkinter.Y)
    quote = get_log()
    text.insert(tkinter.END, quote)


def save_code():
    input = combo.get_input()
    now = (str(datetime.now())[
           0: len(str(datetime.now())) - 7]).replace(':', '_')

    path = os.path.join(f'{now}.txt')
    with open(path, 'w') as f:
        f.write(input)


main_window = tkinter.Tk()


combo = TextScrollCombo(main_window)
# combo.pack(fill="both", expand=True)
combo.grid(padx=0, row=0, column=1, columnspan=3)
combo.config(width=600, height=600)

combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
combo.txt.config(borderwidth=3, relief="sunken")

style = ttk.Style()
style.theme_use('clam')

memoria = tkinter.StringVar()
nameEntered = tkinter.Entry(main_window, textvariable=memoria, width=50)
nameEntered.grid(padx=0, pady=5, row=1, column=1, columnspan=5)

button = tkinter.Button(main_window, text='START',
                        command=my_click, width=10)
button.grid(padx=0, pady=5, row=2, column=1)

save_button = tkinter.Button(
    main_window, text='SAVE', command=save_code, width=10)
save_button.grid(padx=0, pady=5, row=2, column=2)

btn = tkinter.Button(main_window,
                     text="LOGS",
                     command=openNewWindow,
                     width=10)
btn.grid(padx=0, pady=5, row=2, column=3)


my_label = tkinter.Label(main_window, text='Aqui estara tu output')
my_label.grid(padx=10, pady=10, row=3, column=1, columnspan=3)

main_window.title('RAM')
main_window.mainloop()
