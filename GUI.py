import tkinter
import tkinter.ttk as ttk


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


main_window = tkinter.Tk()

combo = TextScrollCombo(main_window)
combo.pack(fill="both", expand=True)
combo.config(width=600, height=600)

combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
combo.txt.config(borderwidth=3, relief="sunken")

style = ttk.Style()
style.theme_use('clam')

main_window.mainloop()
