# ===========================================================#
# Catapult simulator Program
# Last update : 28/6/2564
# By owl_hor | Mei | X2, FRAB7
# This program is final project of
# FRA142_Programming2 x  FRA163_Robotics Studio1:Science in motion
# Institute of FIeld roBOtics, KMUTT
# ------------------------------------
# Using Tkinter(main) and pygame(renderer)
# input  : Distance,High,Angle,Kspring
# output : velocity,time,spring-pull length
# features : - Tkinter UI : show parameters
#            - Projectile Graphic Render
# ===========================================================#

from tkinter import *
from tkinter import ttk, messagebox
from Calculation import XDisToSpringDis
import pygrender2 as pgr
import math

mainfrm = Tk()
mainfrm.geometry("480x490")
mainfrm.title("FRA163 x FRA142 Catapult Simulator V1.1")
mainfrm.configure(bg="skyblue1")
mainfrm.iconbitmap('./image/object_2.ico')

def dcc(x):  # config decimal for answer
    dcc = spb_1.get()
    aaa = str(int(dcc))
    dm = "{:." + aaa + "f}"
    ff = float(dm.format(x))
    return str(ff)

def prender():
    try:
        dista =  int(ent_distance.get())
        high = int(ent_high.get())
        anglr = int(ent_angle.get())
        kspr = int(ent_kspr.get())
    except:
        messagebox.showerror("Parameter error", 'Something went wrong about your parameter.\nPlease check again.')

    xdist = XDisToSpringDis(2, 0, anglr, kspr)
    xdist.XStimecal()
    veloc = xdist.XSvelocitycal()
    veloc2 = dcc(xdist.XSvelocitycal())
    sppull = dcc(xdist.XSpullingcal())
    timec = dcc(xdist.XStimecal())
    prender = pgr.rendder(anglr,veloc,veloc2,timec,dista,high,sppull,kspr)

def calculate():
    ent_time.delete(0, END)
    ent_velocy.delete(0, END)
    ent_sppull.delete(0, END)
    try:
        dista = int(ent_distance.get())
        high = int(ent_high.get())
        anglr = int(ent_angle.get())
        kspr = int(ent_kspr.get())
    except:
        messagebox.showerror("Parameter error", 'Something went wrong about your parameter.\nPlease check again.')

    if anglr > 90 or anglr < 0:
        messagebox.showerror("Angle error", 'Please insert  " 0-90 " for angle.')
    elif 4 * math.tan(math.radians(anglr)) < high :
        messagebox.showerror("Distance-high error", 'Too much high.\nToo low Angle.')
    elif dista <= high:
        messagebox.showerror("Distance-high error", 'Please check your high,distance again.')
    elif anglr == None:
        messagebox.showerror("No Data error", 'Please key data.')
    else:
        xdist = XDisToSpringDis(dista, high, anglr, kspr)
        ent_time.insert("", dcc(xdist.XStimecal()))
        ent_velocy.insert("", dcc(xdist.XSvelocitycal()))
        ent_sppull.insert("", dcc(xdist.XSpullingcal()))

def clearEntry():
    ent_time.delete(0, END)
    ent_velocy.delete(0, END)
    ent_sppull.delete(0, END)

def clearEntryAll():
    ent_distance.delete(0, END)
    ent_high.delete(0, END)
    ent_angle.delete(0, END)
    ent_kspr.delete(0, END)
    ent_time.delete(0, END)
    ent_velocy.delete(0, END)
    ent_sppull.delete(0, END)

def askfile():
    import time
    from tkinter import filedialog
    tmme = time.strftime("SRec_%Y%m%d")  # %H%M%S
    fname = "/" + tmme + ".txt"
    fd = filedialog.askdirectory()
    fdf = fd + fname
    ent_fpth.delete(0, END)
    ent_fpth.insert("", fdf)

def askfile_name():
    #import time
    from tkinter import filedialog
    #tmme = time.strftime("SRec_%Y%m%d")  # %H%M%S
    #fname = "/" + tmme + ".txt"
    fd = filedialog.askopenfilename()
    #fdf = fd + fname
    ent_fpth.delete(0, END)
    ent_fpth.insert("", fd)

def fileWriteCMD_2():  # file name, your text
    import time
    from tkinter import filedialog
    tmme_f = time.strftime("%c")

    try:
        fname = str(ent_fpth.get())
        f = open(fname, "a")
    except:
        messagebox.showerror("File path error", 'Please choose where to save file.')
    try:
        dista = int(ent_distance.get())
        high = int(ent_high.get())
        anglr = int(ent_angle.get())
        kspr = int(ent_kspr.get())
    except:
        messagebox.showerror("Parameter error", 'Something went wrong about your parameter.\nPlease check again.')

    xdist = XDisToSpringDis(dista, high, anglr, kspr)
    top_info = "\ndistance: " + str(dista) + "  high: " + str(high) \
               + "\nangle: " + str(anglr) + "  Kspring: " + str(kspr) + "\n"
    sf_time = "      time : " + dcc(xdist.XStimecal()) + "\n"
    sf_velo = "  velocity : " + dcc(xdist.XSvelocitycal()) + "\n"
    sf_pull = "pull range : " + dcc(xdist.XSpullingcal()) + "\n"
    endline = "----------------------------------\n"
    f.writelines(tmme_f)
    f.writelines(top_info)
    f.writelines(sf_time)
    f.writelines(sf_velo)
    f.writelines(sf_pull)
    f.writelines(endline)
    f.close()
    messagebox.showinfo("Data Rec", "File Saved")

desc = ttk.Label(mainfrm, text="Group 8 Catapult simulator.", font=("", "10"),anchor="nw",
                 foreground="black", background="skyblue1")
desc.pack(padx=0, pady=3)

label_f1 = ttk.LabelFrame(mainfrm, text="Catapult Calculator", labelanchor="n")
label_f1.pack(padx=10, pady=10, anchor="n")
#label_f1.place(x=55, y=30)
label_n1 = ttk.Label(label_f1, text="Distance (m)  :").grid(column=0, row=0, padx=25,pady=1, sticky="e")
label_n2 = ttk.Label(label_f1, text="High (m)  :").grid(column=0, row=1, padx=25,pady=1, sticky="e")
label_n3 = ttk.Label(label_f1, text="Angle (deg)  :").grid(column=0, row=2, padx=25,pady=1, sticky="e")
label_n4 = ttk.Label(label_f1, text="K spring (N/m)  :").grid(column=0, row=3, padx=25,pady=1, sticky="e")

#----------inbox--------------------------inbox-----------f1-----------#
f1_pady = 3
ent_distance = ttk.Entry(label_f1)
ent_distance.grid(column=1, row=0, padx=5,pady=f1_pady)
ent_high = ttk.Entry(label_f1)
ent_high.grid(column=1, row=1, padx=5, pady=f1_pady)
ent_angle = ttk.Entry(label_f1)
ent_angle.grid(column=1, row=2, padx=5, pady=f1_pady)
ent_kspr = ttk.Entry(label_f1)
ent_kspr.grid(column=1, row=3, padx=5,pady=f1_pady)
#----------inbox--------------------------inbox-----------f1-----------#

f3_pady = 1
label_f3 = ttk.LabelFrame(mainfrm, text="Results                                Decimal config", labelanchor="ne")
label_f3.pack(padx=10, pady=10, anchor="n")
#label_f3.place(x=55, y=190)
label_r1 = ttk.Label(label_f3, text="Time (sec) :").grid(column=0, row=0, padx=5,pady=f3_pady, sticky="e")
label_r2 = ttk.Label(label_f3, text="Velocity (m/s)  :").grid(column=0, row=1, padx=5,pady=f3_pady, sticky="e")
label_r3 = ttk.Label(label_f3, text="SpringPull (m)  :").grid(column=0, row=2, padx=5,pady=f3_pady, sticky="e")
#label_s1 = ttk.Label(label_f3, text="Decimal config")#.grid(column=2, row=1, padx=5, sticky="w")

spb_1 = Spinbox(label_f3, from_=1, to=10, width=7, format="%10.0f")
spb_1.grid(column=2, row=0, padx=5)

#----------inbox--------------------------inbox-----------f3-----------#
ent_time = ttk.Entry(label_f3)
ent_time.grid(column=1, row=0, padx=25, pady=f3_pady)
ent_velocy = ttk.Entry(label_f3)
ent_velocy.grid(column=1, row=1, padx=25, pady=f3_pady)
ent_sppull = ttk.Entry(label_f3)
ent_sppull.grid(column=1, row=2, padx=25, pady=f3_pady)
#----------inbox--------------------------inbox-----------f3-----------#

btn_Enter = ttk.Button(label_f1, text="Calculate"
                       , command=calculate).grid(column=1, row=4, padx=20, pady=5)
#btn_Enter.place(x=130, y=95)
btn_Clear = ttk.Button(label_f1, text="Clear all"
                       , command=clearEntryAll).grid(column=0, row=4, padx=5, pady=10)
btn_Clear_r = ttk.Button(label_f3, text="Clear"
                       , command=clearEntry).grid(column=2, row=1, padx=5, pady=3)
btn_render = ttk.Button(label_f3, text="Render"
                        , command=prender).grid(column=2, row=2, padx=5, pady=0)

##################### save label-----------------------------------------------
label_f2 = ttk.LabelFrame(mainfrm, text="Save to file", labelanchor="n")
label_f2.pack(padx=10, pady=5, anchor="n")
label_r4 = ttk.Label(label_f2, text="Save at  :").grid(column=0, row=0, padx=5, pady=f3_pady, sticky="e")
btn_Save = ttk.Button(label_f2, text="SAVE"
                      , command=fileWriteCMD_2).grid(column=2, row=0, padx=2, pady=0)
btn_asksav = ttk.Button(label_f2, text="Open location"
                        , command=askfile).grid(column=1, row=1, padx=25, pady=0)
btn_asksfle = ttk.Button(label_f2, text="Choose file"
                        , command=askfile_name)#.grid(column=0, row=1, padx=100, pady=0)
btn_asksfle.place(x=270, y=25)
ent_fpth = ttk.Entry(label_f2)
ent_fpth.grid(column=1, row=0, padx=5, pady=f3_pady, ipadx=90,sticky="e")

def _quit():
    mainfrm.quit()  # stops mainloop
    mainfrm.destroy()  # this is necessary on Windows to prevent

button_quit = ttk.Button(mainfrm, text="Quit", command=_quit)
#button_quit.pack(padx=0, pady=10, anchor="s")
button_quit.place(x=370, y=450)

label_under= Label(text="FRA163 x FRA142 Catapult Simulator Program. \nPowered by owl_hor | Mei | X2 Group_8"
                        "\n Institute of FIeld roBOtics, KMUTT. June 2021",
                   font=('courier new', 8), fg='#1d1e1f',bg="skyblue1")
label_under.place(x=10, y=435)


mainfrm.mainloop()
