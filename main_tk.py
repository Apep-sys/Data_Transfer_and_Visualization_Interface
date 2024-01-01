'''import tkinter as tk

def tk_interface():
    pass

window = tk.Tk()

btn_names = ['Read CSV/XLSX', 'Parse CSV', 'Graph the Data', 'Send to TCP', 'RS232 Communication',
             'All of the Above']
for i in range(6):
    window.rowconfigure(i, weight=1, minsize=75)
    window.columnconfigure(0, weight=1, minsize=50)
    frame = tk.Frame(window, relief=tk.RAISED, bg='turquoise', borderwidth=1)
    frame.grid(row=i, column=0, padx=5, pady=5, sticky='nsew')
    btn = tk.Button(frame, text=btn_names[i], fg='gold', bg='indianred')
    btn.pack(padx=5, pady=5)

window.mainloop()
'''
import customtkinter
import customtkinter as ctk
#from PIL import Image, ImageTk


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def add_btns(self):
        btn_names = ['Read CSV/XLSX', 'Parse CSV/XLSX', 'Graph the Data', 'Send to TCP', 'RS232 Communication',
                     'All of the Above']
        btn_list = []

        for i in range(6):
            self.grid(row=i, column=0, pady=5)
            self.btn = ctk.CTkButton(self, text=btn_names[i], width=70, height=50,
                                border_width=2, border_color='green', corner_radius=32,
                                font=('Roboto', 14))
            self.btn.pack(padx=5, pady=15)
            btn_list.append(self.btn)
        return btn_list

    def add_lbl(self):
        self.grid(row=5, column=5, padx=20, pady=5)
        self.lbl = ctk.CTkLabel(self, text='\n\n\nWelcome to my project!\nInstructions:\n1. Choose your theme\n'
                                      '2. Click the Start button and select the desired operation\n'
                                      '', font=('Roboto', 20),
                                      text_color='green')
        self.btn = ctk.CTkButton(self, text='Start', width=70, height=50,border_width=2, border_color='green',
                                corner_radius=32, font=('Roboto', 14), command=self.delete_frame)
        self.btn.pack(padx=5, pady=15)
        self.lbl.pack(padx=5, pady=10)
        #TODO Look for the solution to passing value from the command function using StringVar in the saved link
        '''if stringvar:
            btns.btns()'''

    def delete_frame(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.grid_remove()


class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def read_tab(self):
        self.add('Read Tab')

    def parse_tab(self):
        self.add('Parse Tab')

    def graph_tab(self):
        self.add('Graph Tab')

    def tcp_tab(self):
        self.add('TCP Tab')

    def rs232_tab(self):
        self.add('RS232 Tab')

    def all_tab(self):
        self.add('All Tab')

    def add_command(self, btn_list):
        for btn in btn_list:
            if 'Read' in btn.cget('text'):
                btn.configure(command=self.read_tab)

            elif 'Parse' in btn.cget('text'):
                btn.configure(command=self.parse_tab)

            elif 'Graph' in btn.cget('text'):
                btn.configure(command=self.graph_tab)

            elif 'TCP' in btn.cget('text'):
                btn.configure(command=self.tcp_tab)

            elif 'RS232' in btn.cget('text'):
                btn.configure(command=self.rs232_tab)

            elif 'All' in btn.cget('text'):
                btn.configure(command=self.all_tab)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.grid_columnconfigure(0, weight=1, minsize=50)

    def intro(self):
        self.lbl_frame = Frame(self, border_width=2, border_color='red')
        self.lbl_frame.add_lbl()

    def btns(self):
        self.btn_frame = Frame(self, border_width=2, border_color='orange')
        self.btn_list = self.btn_frame.add_btns()
        self.btn_frame.grid(column=0, sticky='w')

    def tabs(self):
        self.tab_view = TabView(self)
        if self.tab_view.add_command(self.btn_list):
            self.tab_view.grid(row=3, column=3)
            self.lbl_frame.grid_forget()


'''window = ctk.CTk()
window.geometry('800x600')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

btn_names = ['Read CSV/XLSX', 'Parse CSV/XLSX', 'Graph the Data', 'Send to TCP', 'RS232 Communication',
             'All of the Above']

def btn_open(btn):
    btn._fg_color = 'red'
    btn._hover_color = 'gold'

for i in range(6):
    window.rowconfigure(i, weight=1, minsize=75)
    window.columnconfigure(0, weight=1, minsize=50)
    frame = ctk.CTkFrame(window)
    frame.grid(row=i, column=0, padx=2, pady=2)
    btn = ctk.CTkButton(frame, text=btn_names[i], corner_radius=32)
    btn.command = btn_open(btn)
    btn.pack(padx=2, pady=2)'''

app = App()
app.intro()

app.mainloop()
