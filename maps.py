from tkinter import *
import webbrowser
 
 
class GoogleMap(Tk):
 
    def __init__(self):
        Tk.__init__(self)
        Tk.title(self, 'Google Map in Python')
 
        container = Frame(self)
        container.grid()
 
        self.frames = {}
 
        for page in (StartPage, MapPage, DirectionPage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky=N+S+E+W)
 
        self.raise_frame(StartPage)
 
    def raise_frame(self, frame_title):
        frame = self.frames[frame_title]
        frame.tkraise()
 
 
class StartPage(Frame):
 
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
 
        Map_Button = Button(self, text='Go to Map',
                            command=lambda: controller.raise_frame(MapPage))
        Map_Button.grid(row=0, column=0)
 
        Direction_Button = Button(self, text='Go to Direction',
                                  command=lambda: controller.raise_frame(DirectionPage))
        Direction_Button.grid(row=0, column=1)
 
        Quit_Button = Button(self, text='Quit', command=quit)
        Quit_Button.grid(row=0, column=2)
 
 
class MapPage(Frame):
 
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
 
        Address_Label = Label(self, text='Street address:')
        Address_Label.grid(row=0, column=0)
 
        String_Entry = Entry(self)
        String_Entry.grid(row=0, column=1)
 
        def search():
            url = 'https://www.google.com/maps/place/' + String_Entry.get()
            webbrowser.open(url)
           
        Search_Button = Button(self, text='Search', command=search)
        Search_Button.grid(row=0, column=2)
 
        Back_Button = Button(self, text='Go back',
                             command=lambda: controller.raise_frame(StartPage))        
        Back_Button.grid(row=1, columnspan=3)
 
 
class DirectionPage(Frame):
   
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
 
        Start_Label = Label(self, text='Start address:')
        Start_Label.grid(row=0, column=0)
 
        Start_Entry = Entry(self)
        Start_Entry.grid(row=0, column=1)
       
        Finish_Label = Label(self, text='Finish address:')
        Finish_Label.grid(row=1, column=0)
 
        Finish_Entry = Entry(self)
        Finish_Entry.grid(row=1, column=1)
 
        Back_Button = Button(self, text='Go back',
                             command=lambda: controller.raise_frame(StartPage))        
        Back_Button.grid(row=0, column=2)
 
        def search():
            url = ('https://www.google.com/maps/dir/' + Start_Entry.get() +
                   '/' + Finish_Entry.get())
            webbrowser.open(url)
 
        Search_Button = Button(self, text='Search', command=search)
        Search_Button.grid(row=1, column=2)        
 
 
GoogleMap()
 
mainloop()