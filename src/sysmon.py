from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
import socket
import os 
import platform

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI() 
    
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
        # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
             
    def initUI(self):
      
        self.master.title("APMW System Info")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="System Info")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        area.insert(END, "Hostname: "+socket.gethostname())
        area.insert(END, "\nUsername: "+os.getlogin())
        area.insert(END, "\nWindows Version: "+platform.version())
        area.insert(END, "\nIP Address: "+self.get_ip())
        area.config(state=DISABLED)
        
        abtn = Button(self, text="Refresh Info")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close", command=self.quit)
        cbtn.grid(row=5, column=0, pady=5)
        
        hbtn = Button(self, text="Help")
        hbtn.grid(row=2, column=3, padx=4)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3) 

def main():
  
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()  
    

if __name__ == '__main__':
    main()  