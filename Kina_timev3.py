from Tkinter import *
import time
import webbrowser
import random
#Creates button screen
class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Kina Time!")
        self.label = Label (self.root, text= "Enter your Kina break time (in secs)")
        self.label.pack()

        #User inputs file path 
        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Run")
        Button(self.root, textvariable=self.buttontext, command=self.run_program).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()
            #Function to call from button
    def run_program(self):
    #websites to pull from
      song_play = ["https://www.youtube.com/watch?v=-nYsM9sTqxo", "https://www.youtube.com/watch?v=4_o95IyLL_U", "https://www.youtube.com/watch?v=SDGOXRr-yco", "https://www.youtube.com/watch?v=BjfjxTxQ02w","https://www.youtube.com/watch?v=iW4jp8UlBt4","https://www.youtube.com/watch?v=9ptD3kSvc24"]
    #Tells user when the program started
      print("This program started on"+time.ctime())
    #On start up, play random song
      song = random.choice(song_play)
      webbrowser.open(song)
      num = self.entrytext.get()
      num1 = int(num)
    #Loop through set of videos every 20 minutes
      for i in range (1,11):                    
        time.sleep(num1)
    #randomly choice one page to use
        song = random.choice(song_play)
        webbrowser.open(song)
        


App()
