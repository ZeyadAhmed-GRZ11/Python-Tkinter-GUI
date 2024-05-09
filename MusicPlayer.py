from tkinter import *
from tkinter import filedialog
from pygame import mixer


def addSongs():
    songsSelection = filedialog.askopenfilenames(initialdir="Music/", title="choose songs", filetypes=(("mp3 files", "*.mp3"),))
    for s in songsSelection:
        # s = s.replace("C:/Users/Teba/Music/", "")
        s = s.replace('file name', "")
        listSongs.insert(END, s)
        
def playSong():
    song = listSongs.get(ACTIVE)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()

def stopSong():
    mixer.music.stop()
    listSongs.selection_clear(ACTIVE)
    
def pauseSong():
    mixer.music.pause()

def resumeSong():
    mixer.music.unpause()
    
def nextSong():
    nextOne = listSongs.curselection() 
    nextOne = nextOne[0]+ 1
    song = listSongs.get(nextOne)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()
    listSongs.selection_clear(0, END)
    listSongs.activate(nextOne)
    listSongs.selection_set(nextOne)
    
def backSong():
    backOne = listSongs.curselection() 
    backOne = backOne[0]-1
    song = listSongs.get(backOne)
    song = f'{song}'
    listSongs.selection_clear(0, END)
    listSongs.activate(backOne)
    listSongs.selection_set(backOne)
    mixer.music.load(song)
    mixer.music.play()
    
def deleteSong():
    currSong = listSongs.curselection()
    listSongs.delete(currSong[0])   
    
    
window = Tk()
window.title("Music Player")

mixer.init()


# playlist = Label(window, text='Your PlayList')
# playlist.pack(side=TOP)

myMenu = Menu(window)
window.config(menu=myMenu)
controlSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Menu", menu= controlSongMenu)
controlSongMenu.add_command(label="Add songs" ,command=addSongs)
controlSongMenu.add_command(label="Delete song", command=deleteSong)
controlSongMenu.add_command(label="Your PlayList", command=addSongs)

#47 12
listSongs = Listbox(window, bg="black", fg="white",width=47,height=12 , font = ("arial"), selectmode=SINGLE, selectbackground="gray", selectforeground="black")
listSongs.grid(columnspan=9)

playBtn = Button(window, text="Play", font=("arial",15), width=7, command=playSong)
playBtn.grid(row=1, column=0)

pauseBtn = Button(window, text="Pause", font=("arial",15), width=7 ,command=pauseSong)
pauseBtn.grid(row=1, column=1)

stopBtn = Button(window, text="Stop", font=("arial",15), width=7, command= stopSong)
stopBtn.grid(row=1, column=2)

resumeBtn = Button(window, text="Resume", font=("arial",15), width=7 ,command=resumeSong)
resumeBtn.grid(row=1, column=3)

prevBtn = Button(window, text="Prev", font=("arial",15), width=7, command=backSong)
prevBtn.grid(row=1, column=4)

nextBtn = Button(window, text="Next", font=("arial",15), width=7, command= nextSong)
nextBtn.grid(row=1, column=5)

window.geometry("520x332")
window.mainloop()