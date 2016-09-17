from Tkinter import *
import time
import webbrowser
import random
#Creates button screen
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.slogan = Button(frame,
                         text="Kina Time!",
                         command=self.run_program)
    self.slogan.pack(side=LEFT)
#Function to call from button
  def run_program(self):
    #websites to pull from
    song_play = ["https://www.youtube.com/watch?v=-nYsM9sTqxo", "https://www.youtube.com/watch?v=4_o95IyLL_U", "https://www.youtube.com/watch?v=SDGOXRr-yco", "https://www.youtube.com/watch?v=BjfjxTxQ02w","https://www.youtube.com/watch?v=iW4jp8UlBt4","https://www.youtube.com/watch?v=9ptD3kSvc24"]
    #Tells user when the program started
    print("This program started on"+time.ctime())
    #On start up, play random song
    song = random.choice(song_play)
    webbrowser.open(song)
    #Loop through set of videos every 20 minutes
    for i in range (1,11):                    
        time.sleep(1200)
    #randomly choice one page to use
        song = random.choice(song_play)
        webbrowser.open(song)
        


root = Tk()
app = App(root)
root.mainloop()
