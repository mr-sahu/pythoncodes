#from dynamic coding
from tkinter import *
from tkinter import ttk,filedialog
win=Tk()
win.geometry("300x190")
win.title("Best Music Player")
#win.resizable(0,0)
win.config(bg="black")
# s=ttk.Style(win)
# s.theme_use('vista')
import os
from pygame import mixer
mixer.init()
###ask to select from location
def open_folder():
    path=filedialog.askdirectory()
    if(path):
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                play_list.insert(END,song)
######play 
def play_songs():
    mixer.music.load(play_list.get(ACTIVE))
    mixer.music.play()
########
#     set volume
def set_vol(val):
    mixer.music.set_volume(float(val)/100)

lab=ttk.Label(win,text="Best Music Player",font=("Arial Bold",10),background="blue",foreground="white").place(x=80,y=1)
ttk.Button(win,text="Play",width=10,command=play_songs).place(x=10,y=20)
ttk.Button(win,text="Stop",width=10,command=mixer.music.stop).place(x=10,y=50)
ttk.Button(win,text="Pause",width=10,command=mixer.music.pause).place(x=10,y=80)
ttk.Button(win,text="Resume",width=10,command=mixer.music.unpause).place(x=10,y=110)
ttk.Button(win,text="Open",width=10,command=open_folder).place(x=10,y=140)
###
music_frame=Frame(win,bd=2,relief=RIDGE)
music_frame.place(x=90,y=20,width=200,height=160)
scrollbar=ttk.Scrollbar(music_frame)
play_list=Listbox(music_frame,width=30,yscrollcommand=scrollbar.set)
play_list.pack(side=LEFT,fill=BOTH )
scrollbar.config(command=play_list.yview)
scrollbar.pack(side=RIGHT,fill=Y)
##VOL 
vol=ttk.Scale(win,from_=0,to=100,length=110,command=set_vol)
vol.set(50)
vol.place(x=100,y=130)





win.mainloop()