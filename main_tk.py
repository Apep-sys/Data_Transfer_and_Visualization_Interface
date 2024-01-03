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


# from PIL import Image, ImageTk


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

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
        self.grid(row=0, column=0, padx=20, pady=50, sticky='nsew')
        self.lbl = ctk.CTkLabel(self, text='\n\n\nWelcome to my project!\nInstructions:\n1. Choose your theme\n'
                                           '2. Click the Start button and select the desired operation\n'
                                           '', font=('Roboto', 20),
                                text_color='green')
        self.btn = ctk.CTkButton(self, text='Start', width=70, height=50, border_width=2, border_color='green',
                                 corner_radius=32, font=('Roboto', 14), command=self.delete_frame)

        # TODO Add the function for changing the theme
        self.change_theme = ctk.CTkButton(self, text='Change the Theme', width=70, height=50, border_width=2,
                                          border_color='green', corner_radius=32, font=('Roboto', 14),
                                          )

        self.btn.pack(padx=5, pady=15)
        self.change_theme.pack(padx=5, pady=15)
        self.lbl.pack(padx=5, pady=20)

    def delete_frame(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.grid_remove()
        self.master.btns()


class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def add(self, tab_name):
        tab = super().add(tab_name)
        self.grid(column=0, row=5, padx=50)
        return tab

    def read_tab(self):
        self.add('Read Tab')
        self.btn_csv = ctk.CTkButton(self.tab('Read Tab'), text='Read CSV', corner_radius=32)
        self.btn_xlsx = ctk.CTkButton(self.tab('Read Tab'), text='Read XLSX', corner_radius=32)
        self.btn_csv.pack(padx=10, pady=20)
        self.btn_xlsx.pack(padx=10, pady=20)

    def parse_tab(self):
        self.add('Parse Tab')

    def graph_tab(self):
        self.add('Graph Tab')
        graph_names = ['Graph Humidity', 'Graph Temperature', 'Graph Speed', 'Graph Position']
        for i in range(4):
            self.btn = ctk.CTkButton(self.tab('Graph Tab'), text=graph_names[i], corner_radius=32)
            self.btn.pack(padx=10, pady=20)

    def tcp_tab(self):
        self.add('TCP Tab')

        # TODO To add the red colour for closing buttons
        self.open_tcp = ctk.CTkButton(self.tab('TCP Tab'), text='Open TCP Server', corner_radius=32)

        self.close_tcp = ctk.CTkButton(self.tab('TCP Tab'), text='Close TCP Server', corner_radius=32)
        self.open_tcp.pack(padx=10, pady=20)
        self.close_tcp.pack(padx=10, pady=20)

    def rs232_tab(self):
        self.add('RS232 Tab')
        self.rs_open = ctk.CTkButton(self.tab('RS232 Tab'), text='Start RS Communication', corner_radius=32)
        self.rs_close = ctk.CTkButton(self.tab('RS232 Tab'), text='Close RS Communication', corner_radius=32)
        self.rs_open.pack(padx=10, pady=20)
        self.rs_close.pack(padx=10, pady=20)

    def all_tab(self):
        self.add('All Tab')
        self.btn = ctk.CTkButton(self.tab('All Tab'), text='Execute Command', corner_radius=32)
        self.btn.pack(padx=10, pady=20)

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
        self.btn_frame = Frame(self, border_width=5, border_color='orange')
        self.btn_list = self.btn_frame.add_btns()
        self.btn_frame.grid(column=0, sticky='w')
        self.tabs()

    def tabs(self):
        self.tab_view = TabView(self, corner_radius=32, fg_color='silver')
        self.tab_view.add_command(self.btn_list)


app = App()
app.intro()

app.mainloop()
