import os
import tkinter
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import pygame
from mutagen.id3 import ID3
from tkinter import *
from pygame import mixer
import time
import tkinter.messagebox
import sqlite3
conn=sqlite3.connect('melody.db')
c=conn.cursor()

#c.execute('''CREATE TABLE music
              #(name text,
              #id text)''')

#c.execute('''CREATE TABLE fav
                   #(name text)
                   #''')






root = Tk()
root.minsize(300, 300)
playlist = []


listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root, textvariable=v, width=35)

index = 0

menubar = Menu(root)
root.config(menu=menubar)

def recently():
    listbox2 = Listbox(root)

def favourites():
    listbox3 = Listbox(root)



submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="Recent Plays", command=recently)
submenu.add_command(label="Favourites", command=favourites)
submenu.add_command(label="Exit", command=root.destroy)
'''
def file_selection(self):
    pygame.mixer.music.load(listbox.curselection)
    pygame.mixer.music.play()
    '''



recently()


def fillnamedb():
    listvalue = listbox.get(0, END)
    j = 0
    for value in listvalue:
        c.execute("INSERT INTO music VALUES(?,?);", (value, j))
        j += 1
    conn.commit()




def browse_file():    #browse the file mp3
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

    mixer.music.queue(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    listbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

'''
def addallsong():

    i=0
    for a in realnames:

        b=a
        c.execute("INSERT INTO music VALUES(?,?)",(b,i))
        i=i+1
    conn.commit()
'''

def directorychooser():   #browse the folder whch contains mp3
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            index=0
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            playlist.insert(index,realdir)
            index+=1
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    # pygame.mixer.music.play()
    #addallsong()



directorychooser()

listbox = Listbox(root)
listbox.pack()

addBtn = Button(root, text="+ Add", command=browse_file)
addBtn.pack(side=LEFT)



def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    # return songname


def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = FALSE
    else:
        try:

            time.sleep(1)
            selected_song = listbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()


        except:
            tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')

'''      
def nextsong(event):
    global index
    index += 1
                                         
    selected_song = listbox.curselection()
    selected_song = int(selected_song[0])
    play_it = playlist[selected_song]

    pygame.mixer.music.load(listbox[selected_song])
    pygame.mixer.music.play()
    updatelabel()
'''
def next(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()



def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    # return songname
paused = FALSE
def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()


def rewind_music():
    mixer.music.play()


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)  # takes from 0 to 1


muted = FALSE


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        volBtn.configure(image=volPhoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE


label = Label(root, text='Music Player')
label.pack()

listboxp = Listbox(root)
#listboxp.pack(fill=X)

# listofsongs.reverse()
#realnames.reverse()

# listbox.bind('<<ListboxSelect>>', file_selection)



for items in realnames:

    listbox.insert(0, items)



fillnamedb()






print(realnames)
#realnames.reverse()
# listofsongs.reverse()


nextbutton = Button(root, text='Play This song',command=play_music)
nextbutton.pack()
'''
previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

stopbutton = Button(root, text='Stop Music')
stopbutton.pack()

previousbutton.bind("<Button-1>", prevsong)
'''
middleframe = Frame(root)
middleframe.pack(pady=30, padx=30)

favphoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/fav.png')
favbutton = Button(root, image=favphoto,width=25,height=20 )
favbutton.pack()



PlayPhoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/play.png')
PlayBtn = Button(middleframe, image=PlayPhoto)
# PlayBtn.pack(side=LEFT,padx=10)
PlayBtn.bind("<Button-1>", next)
PlayBtn.grid(row=0, column=0, padx=10)

StopPhoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/stop.png')
StopBtn = Button(middleframe, image=StopPhoto)
# StopBtn.pack(side=LEFT,padx=10)
StopBtn.bind("<Button-1>", stopsong)
StopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/pause.png')
PauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
# PauseBtn.pack(side=LEFT,padx=10)
PauseBtn.grid(row=0, column=2, padx=10)


rewindPhoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/prewind.png')
rewindBtn = Button(root, image=rewindPhoto, command=rewind_music)
# PauseBtn.pack(side=LEFT,padx=10)
rewindBtn.pack()



mutePhoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/mute.png')
volPhoto = PhotoImage(file='C:/Users/INSPIRON/PycharmProjects/musicplayer/melodyimages/melody/pvol.png')
volBtn = Button(root, image=volPhoto, command=mute_music)
volBtn.pack()



scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=12)



statusbar = Label(root, text="Music Player", relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
