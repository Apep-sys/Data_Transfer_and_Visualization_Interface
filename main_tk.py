import threading

import customtkinter as ctk
import parse_file as ps
import graphs_file as gr
import tcp_file as tcp
import queue
import sys

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

    def add_btns(self):
        btn_names = ['Read CSV/XLSX', 'Graph the Data', 'Send to TCP', 'RS232 Communication',
                     'All of the Above', 'Close Application']
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
        self.theme_btn = ctk.CTkButton(self, text='Change the Theme', width=70, height=50, border_width=2,
                                       border_color='green', corner_radius=32, font=('Roboto', 14),
                                       command=self.change_theme)

        self.btn.pack(padx=5, pady=15)
        self.theme_btn.pack(padx=5, pady=15)
        self.lbl.pack(padx=5, pady=20)

    def delete_frame(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.grid_remove()
        self.master.btns()

    def change_theme(self):
        if ctk.get_appearance_mode() == 'Dark':
            ctk.set_appearance_mode('light')
        elif ctk.get_appearance_mode() == 'Light':
            ctk.set_appearance_mode('dark')

class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.path = ''
        self.toplevel_opened = False

    def add(self, tab_name):
        tab = super().add(tab_name)
        self.grid(column=0, row=5, padx=50)
        return tab

    def read_tab(self):
        self.add('Read Tab')
        self.entry = ctk.CTkEntry(self.tab('Read Tab'), placeholder_text='Name and Path of the File',
                                  width=200)
        self.entry.pack(padx=20, pady=10)
        self.entry.bind('<Return>', self.entry_event)

    def entry_event(self, event):
        self.entry.pack_forget()
        if self.entry.get():
            self.path = self.entry.get()
            if self.path[-3:] == 'csv':
                self.btn_csv = ctk.CTkButton(self.tab('Read Tab'), text='Read CSV', corner_radius=32,
                                             command=lambda: self.press_csv(self.path))
                self.btn_csv.pack(padx=10, pady=40)
            elif self.path[-3:] == 'lsx':
                self.btn_xlsx = ctk.CTkButton(self.tab('Read Tab'), text='Read XLSX', corner_radius=32,
                                              command=lambda: self.press_xlsx(self.path))
                self.btn_xlsx.pack(padx=10, pady=40)

    def press_csv(self, path):
        self.csv_csv = ctk.CTkButton(self.tab('Read Tab'), text='Download CSV as CSV',
                                          corner_radius=32, font=('Roboto', 14),
                                          command=lambda: ps.process_csv('CSV', path, 'CSV'))
        self.csv_xlsx = ctk.CTkButton(self.tab('Read Tab'), text='Download CSV as XLSX',
                                          corner_radius=32, font=('Roboto', 14),
                                          command=lambda: ps.process_csv('CSV', path, 'XLSX'))
        self.csv_csv.pack(padx=3, pady=10)
        self.csv_xlsx.pack(padx=3, pady=10)

        self.btn_csv.pack_forget()

    def press_xlsx(self, path):
        self.xlsx_csv = ctk.CTkButton(self.tab('Read Tab'), text='Download XLSX as CSV',
                                          corner_radius=32, font=('Roboto', 14),
                                          command=lambda: ps.process_csv('XLSX', path, 'CSV'))
        self.xlsx_xlsx = ctk.CTkButton(self.tab('Read Tab'), text='Download XLSX as XLSX',
                                           corner_radius=32, font=('Roboto', 14),
                                           command=lambda: ps.process_csv('XLSX', path, 'XLSX'))

        self.btn_xlsx.pack_forget()
        self.xlsx_csv.pack(padx=3, pady=10)
        self.xlsx_xlsx.pack(padx=3, pady=10)

    def graph_tab(self):
        self.add('Graph Tab')
        self.btn_temp = ctk.CTkButton(self.tab('Graph Tab'), text='Graph Temperature', corner_radius=32,
                                      font=('Roboto', 14),
                                      command=lambda: gr.show_graphs('Temp'))
        self.btn_humid = ctk.CTkButton(self.tab('Graph Tab'), text='Graph Humidity', corner_radius=32,
                                      font=('Roboto', 14),
                                      command=lambda: gr.show_graphs('Humid'))
        self.btn_speed = ctk.CTkButton(self.tab('Graph Tab'), text='Graph Speed', corner_radius=32,
                                      font=('Roboto', 14),
                                      command=lambda: gr.show_graphs('Speed'))
        self.btn_presence = ctk.CTkButton(self.tab('Graph Tab'), text='Graph Presence', corner_radius=32,
                                      font=('Roboto', 14),
                                      command=lambda: gr.show_graphs('Presence'))

        self.btn_temp.pack(padx=3, pady=15)
        self.btn_humid.pack(padx=3, pady=15)
        self.btn_speed.pack(padx=3, pady=15)
        self.btn_presence.pack(padx=3, pady=15)

    def tcp_tab(self):
        self.add('TCP Tab')

        # TODO To add the red colour for closing buttons
        self.open_tcp = ctk.CTkButton(self.tab('TCP Tab'), text='Open TCP Server', corner_radius=32,
                                      command=lambda: self.master.threads(thread='tcp'))

        self.close_tcp = ctk.CTkButton(self.tab('TCP Tab'), text='Close TCP Server', corner_radius=32,
                                       command=lambda: self.master.threads(stop='stop'))
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

    def close_tab(self):
        self.add('Close Tab')

    def add_command(self, btn_list):
        for btn in btn_list:
            if 'Read' in btn.cget('text'):
                btn.configure(command=self.read_tab)

            elif 'Close' in btn.cget('text'):
                btn.configure(command=self.close_tab)

            elif 'Graph' in btn.cget('text'):
                btn.configure(command=self.graph_tab)

            elif 'TCP' in btn.cget('text'):
                btn.configure(command=self.tcp_tab)

            elif 'RS232' in btn.cget('text'):
                btn.configure(command=self.rs232_tab)

            elif 'All' in btn.cget('text'):
                btn.configure(command=self.all_tab)

class App(ctk.CTk):

    def __init__(self, root):
        super().__init__()
        self.root = root

        self.geometry('800x500')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.grid_columnconfigure(0, weight=1, minsize=50)

        self.q = queue.Queue()
        self.p = queue.Queue()
        self.thread_list = []

        self.setup()

    def setup(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.root.destroy()
        sys.exit()

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

    def threads(self, thread=None, stop=None):

        if stop == 'stop':
            self.thread_list = []
            print('Emptied.')

        if thread == 'tcp':
            tcp_thread = threading.Thread(target=tcp.serverTCP, name='TCP Thread')
            self.thread_list.append(tcp_thread)
        elif thread == 'arduino':
            #TODO To be added in a future arduino file
            arduino_thread = threading.Thread()
            self.thread_list.append(arduino_thread)
        elif thread == 'all':
            pass
            # all of the above
        for thread in self.thread_list:
            thread.start()

        for thread in self.thread_list:
            thread.join()
        print('Thread finished')


if __name__ == '__main__':
    root = ctk.CTk()
    app = App(root)
    app.intro()
    app.mainloop()
