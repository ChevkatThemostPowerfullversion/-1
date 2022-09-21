from tkinter import *
import tk as tk
from PIL import ImageTk,Image

root=Tk()
root.geometry("720x480")
root.title('Интерфейс пользователя всех лампочек')
root.iconbitmap('icons8-anime-64.ico') #add "r" at the beginning of the path if there is an error
FILENAME = 'IMG_1513.jfif'
canvas = Canvas(root, width=720, height=480)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = FILENAME)
canvas.create_image(500, 360, image=tk_img)
CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()

#######################################bathroom####################################################
button_bathroom=Button(root,text="Ванная комната",padx=35,pady=40)
check_bathroom=Checkbutton(root,text="Ванная комната",variable=CheckVar1,onvalue=1,offvalue=0)
Scl=Scale(label="Яркость",from_=0,to=100,orient=HORIZONTAL,length=160,width=10)
Scl.place(x=0,y=140)
button_bathroom.place(x=0,y=20)
check_bathroom.place(x=20,y=10)

#######################################living room#################################################
button_livingroom=Button(root,text="Гостиная",padx=55,pady=40)
check_livingroom=Checkbutton(root,text="Гостиная",variable=CheckVar2,onvalue=1,offvalue=0)
Scl=Scale(label="Яркость",from_=0,to=100,orient=HORIZONTAL,length=160,width=10)
Scl.place(x=200,y=140)
button_livingroom.place(x=200,y=20)
check_livingroom.place(x=245,y=10)

#######################################bedroom#####################################################
button_bedroom=Button(root,text="Спальня",padx=55,pady=40)
check_bedroom=Checkbutton(root,text="Спальня",variable=CheckVar3,onvalue=1,offvalue=0)
Scl=Scale(label="Яркость",from_=0,to=100,orient=HORIZONTAL,length=160,width=10)
Scl.place(x=0,y=340)
button_bedroom.place(x=0,y=220)
check_bedroom.place(x=45,y=210)

##########################################kitchen##################################################
button_kitchen=Button(root,text=" Кухня",padx=62,pady=40)
check_kitchen=Checkbutton(root,text="Кухня",variable=CheckVar4,onvalue=1,offvalue=0)
Scl=Scale(label="Яркость",from_=0,to=100,orient=HORIZONTAL,length=160,width=10)
Scl.place(x=200,y=340)
button_kitchen.place(x=200,y=220)
check_kitchen.place(x=255,y=210)

#############################member######################################################################
#myImg = ImageTk.PhotoImage(Image.open("IMG_1513.jfif"))
#my_Label=Label(image=myImg)
#my_Label.place(x=0,y=0)
#Ванная комната,Гостиная, Спальня, Кухня






button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.place(x=640,y=455)







root.mainloop()
