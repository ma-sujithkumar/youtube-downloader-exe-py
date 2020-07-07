#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pytube
from pytube import YouTube as YT


# In[2]:


window=Tk()
window.title("Youtube Video Downloader")
label=Label(window,text=" Youtube Video Downloader ",font=("Calibri",30,"bold")).grid(row=0,column=0,columnspan=3)


# In[3]:


def Directory():
    path=filedialog.askdirectory()
    link=url1.get()
    yt=YT(link)
    if variable.get()==optionList[0]:
        vid=yt.streams.get_by_itag("22")
        start()
        vid.download(path)
        end()
    elif variable.get()==optionList[1]:
        vid=yt.streams.get_by_itag("18")
        start()
        vid.download(path)
        end()
    else:
        vid=yt.streams.get_by_itag("135")
        start()
        vid.download(path)
        end()


# In[4]:


def start():
    messagebox.showinfo("Started","The download has been started! Please wait")
def end():
    messagebox.showinfo("Stop","The download has been completed succesfully")


# In[5]:


font=("Helvetica", 12, "bold italic")


# In[6]:


def getURL():
    link=url1.get()
    yt=YT(link)
    duration=str(yt.length/60)+" mins"
    vid1.insert(0,duration)
    author1.insert(0,yt.author)
    rating1.insert(0,yt.rating)
    view1.insert(0,yt.views)
    messagebox.showinfo("URL Parsed","The link has been parsed succesfully")


# In[7]:


url=Label(window,text="Paste the link here!",padx=20,pady=10,font=font).grid(row=1,column=0)
okay=Button(window,text="Okay",padx=20,pady=10,font=font,command=getURL).grid(row=2,sticky=E,columnspan=2)
vid=Label(window,text="Video Length: ",padx=20,pady=10,font=font).grid(row=3,column=0)
author=Label(window,text="Author Name: ",padx=20,pady=10,font=font).grid(row=4,column=0)
rating=Label(window,text="Video rating",padx=20,pady=10,font=font).grid(row=5,column=0)
view=Label(window,text="No. of views",padx=20,pady=10,font=font).grid(row=6,column=0)
res=Label(window,text="Set the resolution here!",padx=20,pady=10,font=font).grid(row=7,column=0)

url1=Entry(window,width=35)
vid1=Entry(window,width=40)
author1=Entry(window,width=40)
rating1=Entry(window,width=40)
view1=Entry(window,width=40)

url1.grid(row=1,column=1)
vid1.grid(row=3,column=1)
author1.grid(row=4,column=1)
rating1.grid(row=5,column=1)
view1.grid(row=6,column=1)


# In[8]:


optionList=["720p","360p (recommended)","480p"]
variable = StringVar(window)
variable.set(optionList[0])

opt = OptionMenu(window, variable, *optionList)
opt.config(font=font)
opt.grid(row=7,column=1)


# In[9]:


download=Button(window,text="Download",command=Directory).grid(row=8,column=0,columnspan=3)


# In[10]:


window.mainloop()


# In[11]:


print(variable)


# In[12]:


variable.get()


# In[ ]:




