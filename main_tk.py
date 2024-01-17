import threading
import customtkinter as ctk
import parse_file as ps
import graphs_file as gr
import tcp_file as tcp
import arduino_file as ardu
import live_graph as live
import queue
from PIL import Image, ImageTk
import video_file as video

# Importam toate bibliotecile si fisierele necesare rularii aplicatiei

class Frame(ctk.CTkFrame):
    '''
    Clasa Frame mosteneste clasa CTkFrame din modulul customtkinter.
    Continele toate metodele referitoare la crearea widget-urilor precum butoane, label-uri si frame-uri.
    Constructorul clasei este initializat cu obiectul app, numit master.

    Metode:
    ------
    add_btns - adauga butoanele operatiunilor
    add_lbl - adauga labelul care contine textul ferestrei de instructiuni si butoanele acesteia
    reveal_text - contine mesajele pentru textul ferestrei de instructiuni si apelurile functiei animate_text
    animate_text - adauga mesajul primit ca text in fereastra de instructiuni litera cu litera
    delete_frame - sterge frame-ul si butoanele din fereastra de instructiuni si apeleaza functia pentru crearea
                   butanelor meniului principal
    change_theme - schimba tema de culoare a aplicatiei
    '''
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

    def add_btns(self):
        btn_names = ['Read CSV/XLSX', 'Graph the Data', 'RS232 Communication', 'Send to TCP',
                     'Real-Time Reading', 'Close Application']
        btn_list = []
        image_list = ['csv_icon.png', 'graph_icon.png', 'rs_icon.png', 'tcp_icon.png', 'sensor_icon.png', 'close_icon.png']

        for i in range(6):
            self.grid(row=i, column=0, pady=5)
            self.btn = ctk.CTkButton(self, text=btn_names[i], width=70, height=50, corner_radius=32,
                                     border_width=2, fg_color= '#006400', border_color='#32CD32',
                                     font=('Roboto', 14),
                                     image=ctk.CTkImage(light_image=Image.open(image_list[i]),
                                                        size=(30, 30)))
            self.btn.pack(padx=5, pady=15)
            btn_list.append(self.btn)
        return btn_list

    def add_lbl(self):
        self.grid(row=0, column=0, padx=60, pady=10, sticky='e')
        self.lbl = ctk.CTkLabel(self, text=''
                                           '', font=('Roboto', 20), text_color='green')
        self.lbl_instruct = ctk.CTkLabel(self,
                                text=''
                                     '', font=('Roboto', 20), text_color='green')
        self.btn = ctk.CTkButton(self, text='Start', text_color='black', width=70, height=50, border_width=2, border_color='red',
                                 fg_color='red',
                                 corner_radius=32, font=('Roboto', 14), command=self.delete_frame)
        self.theme_btn = ctk.CTkButton(self, text='Change the Theme', text_color='black', width=70, height=50, border_width=2, fg_color='red',
                                       border_color='red', corner_radius=32, font=('Roboto', 14),
                                       command=self.change_theme)

        self.lbl.pack(padx=5, pady=5)
        self.btn.pack(padx=5, pady=5)
        self.theme_btn.pack(padx=5, pady=5)
        self.lbl_instruct.pack(padx=5, pady=5)

        self.reveal_text()

    def reveal_text(self):
        original_text = "➜ Welcome to my project!\n➜ This is a data transfer and visualization interface.\n" \
                        "➜ Its purpose is to facilitate processes such as reading CSV,\n➜ showing graphics and" \
                        " transferring data \n➜ from a microcontroller to a CSV."
        self.animate_text(self.lbl, original_text)

        instructions_text = "\n➜ Instructions:\n➜ Choose your theme\n" \
                            "➜ Click the Start button and select the desired operation"
        self.animate_text(self.lbl_instruct, instructions_text)

    def animate_text(self, label, text, delay=50, index=0):
        if index < len(text):
            label.configure(text=label.cget('text') + text[index])
            self.after(delay, lambda: self.animate_text(label, text, delay, index + 1))

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
    '''
    Clasa TabView
    '''
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.path = ''
        self.toplevel_opened = False

    def add(self, tab_name):
        tab = super().add(tab_name)
        self.grid(row=0, column=1, sticky='w', padx=20, pady=10)

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

        self.open_tcp = ctk.CTkButton(self.tab('TCP Tab'), text='Open TCP Server', corner_radius=32,
                                      command=lambda: app.threads(thread='tcp', q=app.q,
                                                                          stop_event=app.stop_event_tcp))

        self.close_tcp = ctk.CTkButton(self.tab('TCP Tab'), text='Close TCP Server', corner_radius=32, fg_color='red',
                                       hover_color='red',
                                       command=lambda: app.stop_threads(thread='tcp',
                                                                                stop_event=app.stop_event_tcp))
        self.open_tcp.pack(padx=10, pady=20)
        self.close_tcp.pack(padx=10, pady=20)

    def rs232_tab(self):
        self.add('RS232 Tab')
        self.rs_open = ctk.CTkButton(self.tab('RS232 Tab'), text='Start RS Communication', corner_radius=32,
                                     command=lambda: app.threads(thread='arduino', q=app.q,
                                                                         p=app.p,
                                                                         stop_event=app.stop_event_arduino))
        self.rs_close = ctk.CTkButton(self.tab('RS232 Tab'), text='Close RS Communication', corner_radius=32,
                                      fg_color='red', hover_color='red',
                                     command=lambda: app.stop_threads(thread='arduino',
                                                                         stop_event=app.stop_event_arduino))
        self.rs_open.pack(padx=10, pady=20)
        self.rs_close.pack(padx=10, pady=20)

    def all_tab(self):
        self.add('Live Graph')

        self.arduino_btn = ctk.CTkButton(self.tab('Live Graph'), text='Get Data from Microcontroller', corner_radius=32,
                                 command=lambda: app.threads(thread='arduino', q=app.q, p=app.p,
                                                                     stop_event=app.stop_event_arduino))
        self.arduino_btn.pack(padx=10, pady=20)

        self.csv_btn = ctk.CTkButton(self.tab('Live Graph'), text='Save Data in CSV', corner_radius=32,
                                 command=lambda: app.threads(thread='csv', p=app.p))
        self.csv_btn.pack(padx=10, pady=20)

        self.live_graph_btn = ctk.CTkButton(self.tab('Live Graph'), text='Live Graph', corner_radius=32,
                                 command=lambda: app.threads(thread='live'))
        self.live_graph_btn.pack(padx=10, pady=20)

    def close_tab(self):
        app.destroy()

    def add_command(self, btn_list):
        for btn in btn_list:
            if 'Read CSV' in btn.cget('text'):
                btn.configure(command=self.read_tab)

            elif 'Close' in btn.cget('text'):
                btn.configure(command=self.close_tab)

            elif 'Graph' in btn.cget('text'):
                btn.configure(command=self.graph_tab)

            elif 'TCP' in btn.cget('text'):
                btn.configure(command=self.tcp_tab)

            elif 'RS232' in btn.cget('text'):
                btn.configure(command=self.rs232_tab)

            elif 'Real-Time' in btn.cget('text'):
                btn.configure(command=self.all_tab)

class App(ctk.CTk):
    '''
    Clasa App mosteneste clasa CTk din modulul customtkinter.
    Aceasta reprezinta fereastra principala, urmand sa fie mostenita de obiectul app.
    In constructorul clasei App se configureaza marimea ferestrei principale, atribute precum thread-uri,
    listele tip Queue si alti parametri ai ferestrei.

    Metode:
    ------
    cyber_intro - metoda care se ocupa de incarcarea videoclipului si crearea atributului canvas
    update_video - metoda care se ocupa de actualizarea frame-urilor videoclipurilor
    intro - metoda care deschide fereastra de instructiuni, imediat dupa videoclip
    btns - metoda care apeleaza obiecte ale clasei Frame, pentru a crea obiecte
    tabs - metoda care apeleaza obiecte ale clasei TabView, pentru a crea tab-uri separate
    threads - metoda care se ocupa de firele de executie diverse ale aplicatiei
    '''
    def __init__(self):
        super().__init__()

        self.geometry('800x500')
        self.rowconfigure(0, weight=1)  # randul 0 ocupa spatiul vertical valabil
        self.columnconfigure(0, weight=1)  # coloana 0 ocupa spatiul orizontal valabil
        self.columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=50)

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        self.video_source = 0
        self.vid = None

        self.app_state = False
        self.arduino_thread = None
        self.tcp_thread = None
        self.csv_thread = None
        self.live_graph_thread = None

        self.stop_event_arduino = threading.Event()
        self.stop_event_tcp = threading.Event()

        self.q = queue.Queue()
        self.p = queue.Queue()

    def cyber_intro(self, canvas_check=None, video_source=None):

        if video_source is not None:
            self.video_source = video_source

        if self.vid is not None:
            self.vid.release()

        # open video source (by default this will try to open the computer webcam)
        self.vid = video.MyVideoCapture(self.video_source)

        if canvas_check is None:
        # Create a canvas that can fit the above video source size
            self.canvas = ctk.CTkCanvas(self, width=self.vid.width, height=self.vid.height)
            self.canvas.configure(highlightthickness=0)
            self.canvas.pack()
        elif canvas_check is True:
            self.canvas.configure(width=self.vid.width, height=self.vid.height, highlightthickness=0)
        # Button that lets the user take a snapshot

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 5

    def update_video(self, check=0):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=ctk.NW)
            app.after(self.delay, self.update_video)
        else:
            self.canvas.destroy()
            self.app_state = True
            self.intro()

    def intro(self):
        self.lbl_frame = Frame(self, border_width=2, border_color='red')
        self.lbl_frame.add_lbl()

    def btns(self):
        self.btn_frame = Frame(self, border_width=3, border_color='#006400')
        self.btn_list = self.btn_frame.add_btns()
        self.btn_frame.grid(row=0, column=0, sticky='w', pady=10)
        self.tabs()

    def tabs(self):

        self.tab_view = TabView(self, corner_radius=32, fg_color='transparent')
        self.tab_view.add_command(self.btn_list)

    def threads(self, stop_event=None, thread=None, q=None, p=None):

        if thread == 'arduino':
            self.arduino_thread = threading.Thread(target=ardu.arduino, args=(stop_event, q, p),
                                                   name='Arduino Thread')
            self.arduino_thread.daemon = True
            self.arduino_thread.start()

        elif thread == 'tcp':
            self.tcp_thread = threading.Thread(target=tcp.serverTCP, args=(stop_event, q), name='TCP Thread')
            self.tcp_thread.daemon = True
            self.tcp_thread.start()

        elif thread == 'csv':
            self.csv_thread = threading.Thread(target=ps.create_csv, args=(p,), name='CSV Thread')
            self.csv_thread.daemon = True
            self.csv_thread.start()

        elif thread == 'live':
            self.live_graph_thread = threading.Thread(target=live.start_animation, name='Live Graph')
            self.live_graph_thread.daemon = True
            self.live_graph_thread.start()

    def stop_threads(self, stop_event, thread):
        if thread == 'arduino':
            stop_event.set()
            self.arduino_thread.join()
        elif thread == 'tcp':
            stop_event.set()
            self.tcp_thread.join()

# Daca codul este deschis in fereastra principala, codul acesteia se va executa
# Codul ferestrei principale nu se va executa daca este important in alte fisiere
if __name__ == '__main__':

    # Se creeaza obiectul clasei App, care va servi ca fereastra principala a aplicatiei
    app = App()
    app.title('Data Transfer and Visualization Interface')
    if app.app_state is False:
        app.cyber_intro()
        app.after(app.delay, app.update_video)

    # Functia de loop a aplicatiei
try:
    app.mainloop()
except Exception:
    pass