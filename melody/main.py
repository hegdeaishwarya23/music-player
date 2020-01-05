import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
#lipi fullorig
from pygame import mixer
from tkinter.filedialog import askdirectory
import pygame
root = Tk()

# creating the menu

menubar = Menu(root)
root.config(menu=menubar)


# creating sub menu

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('musickit', 'This is the place to hear music')


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us", command=about_us)

mixer.init()  # initialize the mixer

root.title("MusicKit")
root.iconbitmap(r'melody.ico')

text = Label(root, text='lets make some noise')
text.pack(pady=10)


# labelphoto = Label(root, image = photo)
# labelphoto.pack()

def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = FALSE
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "playing music" + ' ' + os.path.basename(filename)
        except:
            tkinter.messagebox.showerror('error', 'file not found')


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "stop music"


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "pause music"


def rewind_music():
    mixer.music.play()
    statusbar['text'] = "rewind music"


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


middleframe = Frame(root)
middleframe.pack(pady=30, padx=30)

PlayPhoto = PhotoImage(file='play.png')
PlayBtn = Button(middleframe, image=PlayPhoto, command=play_music)
# PlayBtn.pack(side=LEFT,padx=10)
PlayBtn.grid(row=0, column=0, padx=10)

StopPhoto = PhotoImage(file='stop.png')
StopBtn = Button(middleframe, image=StopPhoto, command=stop_music)
# StopBtn.pack(side=LEFT,padx=10)
StopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='pause.png')
PauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
# PauseBtn.pack(side=LEFT,padx=10)
PauseBtn.grid(row=0, column=2, padx=10)

rewindPhoto = PhotoImage(file='prewind.png')
rewindBtn = Button(root, image=rewindPhoto, command=rewind_music)
# PauseBtn.pack(side=LEFT,padx=10)
rewindBtn.pack()

mutePhoto = PhotoImage(file='mute.png')
volPhoto = PhotoImage(file='pvol.png')
volBtn = Button(root, image=volPhoto, command=mute_music)

volBtn.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=12)

statusbar = Label(root, text="welcome to music kit", relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
