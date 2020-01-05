import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from pygame import mixer  #this module includes classes for loading sound objs and controlling playbacks
#net i tried
import pygame
from mutagen import *
from mutagen.id3 import ID3           #bring out metadata from mp3 file


root = Tk()
root.minsize(300,300)   #sets the min size of the window
listofsongs =[]
realname=[]
index=0


v = StringVar()
songlabel = Label(root,textvariable=v,width=35)


#to import music from the dir chosen
def directorychooser():

    directory=askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):                         #to filter only mp3



            realdir=os.path.realpath(files)                # getthe fll path of a file...c//folder/song.mp3
            audio=ID3(realdir)                           #puts all the metadata in audio
            realname.append(audio['TIT2'].text[0])       #tag is used toretrieve diff type of data




            listofsongs.append((files))


                                                             #this will play the first song from the dire
    pygame.mixer.init()
    pygame.mixer.music.load((listofsongs[0]))
  #  pygame.mixer.music.play()


directorychooser()                                           #call the function




label=Label(root,text='Song LIST')   #label to display above listbox
label.pack()

listbox=Listbox(root)
listbox.pack()

realname.reverse()   #if u remove this line the songs will be listed reverse order

for items in realname:
    listbox.insert(0,items)


realname.reverse()



nextbutton =Button(root,text='Next Song')
nextbutton.pack()


previousbutton=Button(root,text='Previous Button')
previousbutton.pack()


stopbutton=Button(root,text='Stop')
stopbutton.pack()
















#create menu

menubar=Menu(root)
root.config(menu=menubar)
#submwnu

def browse_file():
     global filename
     filename=filedialog.askopenfilename()
     print(filename)


submenu =Menu(menubar, tearoff=0)
menubar.add_cascade(label="file",menu="submenu")



root.mainloop()
