import tkinter
from tkinter import *
from pytube import YouTube
#Display Window
window = Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title("Maria's Youtube downloader")
Label(window,text = " Maria'sYoutube Video Downloader", font ='arial 20 bold').pack()

#the fieled for the link
link = StringVar()
Label(window, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(window, width = 70,textvariable = link).place(x = 32, y = 90)

#to download
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
window.mainloop()