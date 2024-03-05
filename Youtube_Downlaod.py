


from tkinter import ttk
from tkinter.messagebox import showerror
from PIL import Image
import customtkinter 
import tkinter
from pytube import YouTube
from customtkinter import CTk, CTkImage, CTkSwitch, filedialog    ##import package


def startDownlaod():             ## for click for downlaod
 try :
  ytlink = link.get()
  resolution = resolution_var.get()
  ytobject = YouTube(ytlink,on_progress_callback=on_progress)
  Video = ytobject.streams.filter(res=resolution).first()
  title.configure(text=ytobject.title, text_color="Green")
  Finish_Download.configure(text="")
  Foldername = filedialog.askdirectory()
  Video.download(Foldername)
  Finish_Download.configure(text="Downloaded Completed",text_color = "Green")
 except Exception :
   Finish_Download.configure(Exception,text = "Downlaod Error !", text_color="red")
   showerror("Error","Please try Again")




def on_progress(stream , chunk , bytes_remaining) :      ## progress fro click for Downlaod
 total_size = stream.filesize
 bytes_download = total_size - bytes_remaining
 ppercentage_of_compeletion = bytes_download / total_size * 100
 #print(ppercentage_of_compeletion)
 per = str(int(ppercentage_of_compeletion))
 ppercentage.configure(text=per + '%')
 ppercentage.update()
 progressBar.set(float(ppercentage_of_compeletion))
 
# system settings

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
def ChangeMoode() :
 val=switch.get()
 if val :
   customtkinter.set_appearance_mode("dark")
 else :
   customtkinter.set_appearance_mode("light")
   





   



   
   
#our App frame

App = customtkinter.CTk()
App.geometry("800x900")
App.title("Youtube_Downlaod_ezioo111")


##Add UI Elements
title = customtkinter.CTkLabel(App,text=" Inssert a Youtube  Link")
title.pack(padx=10,pady=10)

#LINK INPUT 
Url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(App , width=350 , height=50 ,textvariable=Url_var)
link.pack()


#finish Downlaoding

Finish_Download = customtkinter.CTkLabel(App ,text="")
Finish_Download.pack()

# progress percentage

ppercentage = customtkinter.CTkLabel(App, text="0%")
ppercentage.pack()

progressBar = customtkinter.CTkProgressBar(App , width=400)
progressBar.set(0)
progressBar.pack(padx = 10 ,pady=10)


img = Image.open("image_2024-03-04_232011971.ico")

 # Downlaod Buuton

download = customtkinter.CTkButton(App,text="Download", command=startDownlaod,corner_radius=32,fg_color="#C850C0",hover_color="4158D0",image=CTkImage(dark_image=img,light_image=img))
download.pack(padx= 10, pady = 10)

switch = CTkSwitch(App,text="Dark Mode",onvalue=1,offvalue=0,command=ChangeMoode)
switch.pack(padx=10)
print(switch.get())

resolutions =["720p","480p","360p","240","144"]
resolution_var = customtkinter.StringVar()
resolution_Combox = ttk.Combobox(App,values=resolutions,textvariable=resolution_var)
resolution_Combox.pack(padx=20)
resolution_Combox.set("720p")

copyright = customtkinter.CTkLabel(App,text="@ CopyRight : Amir wael")
copyright.pack(padx = 160 , pady = 160)

# Run App

App.mainloop()


