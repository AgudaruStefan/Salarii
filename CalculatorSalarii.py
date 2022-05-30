from tkinter import *
from tkinter import ttk


import tkinter as tk

def CAS(x):
    return x*25/100

def CASS(x):
    return x*10/100

def ImpozitPeVenit(x):
    return x*10/100


def deducerePersonala(x,y):
    if x <= 1950 and y == 0:
        return 510
    elif x <= 1950 and y == 1:
        return 670
    elif x <= 1950 and y == 2:
        return 830
    elif x <= 1950 and y == 3:
        return 990
    elif x <= 1950 and y >= 4:
        return 1.310

    elif 1951 <= x <= 2000 and y == 0:
        return 495
    elif 1951 <= x <= 2000 and y == 1:
        return 655
    elif 1951 <= x <= 2000 and y == 2:
        return 815
    elif 1951 <= x <= 2000 and y == 3:
        return 975
    elif 1951 <= x <= 2000 and y >= 4:
        return 1295

    elif 2001 <= x <= 2050 and y == 0:
        return 480
    elif 2001 <= x <= 2050 and y == 1:
        return 640
    elif 2001 <= x <= 2050 and y == 2:
        return 800
    elif 2001 <= x <= 2050 and y == 3:
        return 960
    elif 2001 <= x <= 2050 and y >= 4:
        return 1280

    elif 2051 <= x <= 2100 and y == 0:
        return 465
    elif 2051 <= x <= 2100 and y == 1:
        return 625
    elif 2051 <= x <= 2100 and y == 2:
        return 785
    elif 2051 <= x <= 2100 and y == 3:
        return 945
    elif 2051 <= x <= 2100 and y >= 4:
        return 1265

    elif 2101 <= x <= 2150 and y == 0:
        return 450
    elif 2101 <= x <= 2150 and y == 1:
        return 610
    elif 2101 <= x <= 2150 and y == 2:
        return 770
    elif 2101 <= x <= 2150 and y == 3:
        return 930
    elif 2101 <= x <= 2150 and y >= 4:
        return 1250

    elif 2151 <= x <= 2200 and y == 0:
        return 435
    elif 2151 <= x <= 2200 and y == 1:
        return 595
    elif 2151 <= x <= 2200 and y == 2:
        return 755
    elif 2151 <= x <= 2200 and y == 3:
        return 915
    elif 2151 <= x <= 2200 and y >= 4:
        return 1235

    elif 2151 <= x <= 2200 and y == 0:
        return 1235
    elif 2151 <= x <= 2200 and y == 1:
        return 1235
    elif 2151 <= x <= 2200 and y == 2:
        return 1235
    elif 2151 <= x <= 2200 and y == 3:
        return 1235
    elif 2151 <= x <= 2200 and y >= 4:
        return 1235

    elif 2201 <= x <= 2250 and y == 0:
        return 420
    elif 2201 <= x <= 2250 and y == 1:
        return 580
    elif 2201 <= x <= 2250 and y == 2:
        return 740
    elif 2201 <= x <= 2250 and y == 3:
        return 900
    elif 2201 <= x <= 2250 and y >= 4:
        return 1220

    elif 2251 <= x <= 2300 and y == 0:
        return 405
    elif 2251 <= x <= 2300 and y == 1:
        return 565
    elif 2251 <= x <= 2300 and y == 2:
        return 725
    elif 2251 <= x <= 2300 and y == 3:
        return 885
    elif 2251 <= x <= 2300 and y >= 4:
        return 1205

    elif 2301 <= x <= 2350 and y == 0:
        return 390
    elif 2301 <= x <= 2350 and y == 1:
        return 550
    elif 2301 <= x <= 2350 and y == 2:
        return 710
    elif 2301 <= x <= 2350 and y == 3:
        return 870
    elif 2301 <= x <= 2350 and y >= 4:
        return 1190

    elif 2351 <= x <= 2400 and y == 0:
        return 375
    elif 2351 <= x <= 2400 and y == 1:
        return 535
    elif 2351 <= x <= 2400 and y == 2:
        return 695
    elif 2351 <= x <= 2400 and y == 3:
        return 855
    elif 2351 <= x <= 2400 and y >= 4:
        return 1175

    elif 2401 <= x <= 2450 and y == 0:
        return 360
    elif 2401 <= x <= 2450 and y == 1:
        return 520
    elif 2401 <= x <= 2450 and y == 2:
        return 680
    elif 2401 <= x <= 2450 and y == 3:
        return 840
    elif 2401 <= x <= 2450 and y >= 4:
        return 1160

    elif 2451 <= x <= 2500 and y == 0:
        return 345
    elif 2451 <= x <= 2500 and y == 1:
        return 505
    elif 2451 <= x <= 2500 and y == 2:
        return 665
    elif 2451 <= x <= 2500 and y == 3:
        return 825
    elif 2451 <= x <= 2500 and y >= 4:
        return 1145

    elif 2501 <= x <= 2550 and y == 0:
        return 330
    elif 2501 <= x <= 2550 and y == 1:
        return 490
    elif 2501 <= x <= 2550 and y == 2:
        return 650
    elif 2501 <= x <= 2550 and y == 3:
        return 810
    elif 2501 <= x <= 2550 and y >= 4:
        return 1130

    elif 2551 <= x <= 2600 and y == 0:
        return 315
    elif 2551 <= x <= 2600 and y == 1:
        return 475
    elif 2551 <= x <= 2600 and y == 2:
        return 635
    elif 2551 <= x <= 2600 and y == 3:
        return 795
    elif 2551 <= x <= 2600 and y >= 4:
        return 1115

    elif 2601 <= x <= 2650 and y == 0:
        return 300
    elif 2601 <= x <= 2650 and y == 1:
        return 460
    elif 2601 <= x <= 2650 and y == 2:
        return 620
    elif 2601 <= x <= 2650 and y == 3:
        return 780
    elif 2601 <= x <= 2650 and y >= 4:
        return 1100

    elif 2651 <= x <= 2700 and y == 0:
        return 285
    elif 2651 <= x <= 2700 and y == 1:
        return 445
    elif 2651 <= x <= 2700 and y == 2:
        return 605
    elif 2651 <= x <= 2700 and y == 3:
        return 765
    elif 2651 <= x <= 2700 and y >= 4:
        return 1085

    elif 2701 <= x <= 2750 and y == 0:
        return 270
    elif 2701 <= x <= 2750 and y == 1:
        return 430
    elif 2701 <= x <= 2750 and y == 2:
        return 590
    elif 2701 <= x <= 2750 and y == 3:
        return 750
    elif 2701 <= x <= 2750 and y >= 4:
        return 1070

    elif 2751 <= x <= 2800 and y == 0:
        return 255
    elif 2751 <= x <= 2800 and y == 1:
        return 415
    elif 2751 <= x <= 2800 and y == 2:
        return 575
    elif 2751 <= x <= 2800 and y == 3:
        return 735
    elif 2751 <= x <= 2800 and y >= 4:
        return 1055

    elif 2801 <= x <= 2850 and y == 0:
        return 240
    elif 2801 <= x <= 2850 and y == 1:
        return 400
    elif 2801 <= x <= 2850 and y == 2:
        return 560
    elif 2801 <= x <= 2850 and y == 3:
        return 720
    elif 2801 <= x <= 2850 and y >= 4:
        return 1040

    elif 2851 <= x <= 2900 and y == 0:
        return 225
    elif 2801 <= x <= 2850 and y == 1:
        return 385
    elif 2801 <= x <= 2850 and y == 2:
        return 545
    elif 2801 <= x <= 2850 and y == 3:
        return 705
    elif 2801 <= x <= 2850 and y >= 4:
        return 1025

    elif 2901 <= x <= 2950 and y == 0:
        return 210
    elif 2901 <= x <= 2950 and y == 1:
        return 370
    elif 2901 <= x <= 2950 and y == 2:
        return 530
    elif 2901 <= x <= 2950 and y == 3:
        return 690
    elif 2901 <= x <= 2950 and y >= 4:
        return 1010

    elif 2951 <= x <= 3000 and y == 0:
        return 195
    elif 2951 <= x <= 3000 and y == 1:
        return 355
    elif 2951 <= x <= 3000 and y == 2:
        return 515
    elif 2951 <= x <= 3000 and y == 3:
        return 675
    elif 2951 <= x <= 3000 and y >= 4:
        return 995

    elif 3001 <= x <= 3050 and y == 0:
        return 180
    elif 2951 <= x <= 3000 and y == 1:
        return 340
    elif 2951 <= x <= 3000 and y == 2:
        return 500
    elif 2951 <= x <= 3000 and y == 3:
        return 660
    elif 2951 <= x <= 3000 and y >= 4:
        return 980

    elif 3051 <= x <= 3100 and y == 0:
        return 165
    elif 3051 <= x <= 3100 and y == 1:
        return 325
    elif 3051 <= x <= 3100 and y == 2:
        return 485
    elif 3051 <= x <= 3100 and y == 3:
        return 645
    elif 3051 <= x <= 3100 and y >= 4:
        return 965

    elif 3101 <= x <= 3150 and y == 0:
        return 150
    elif 3101 <= x <= 3150 and y == 1:
        return 310
    elif 3101 <= x <= 3150 and y == 2:
        return 470
    elif 3101 <= x <= 3150 and y == 3:
        return 630
    elif 3101 <= x <= 3150 and y >= 4:
        return 950

    elif 3151 <= x <= 3200 and y == 0:
        return 135
    elif 3151 <= x <= 3200 and y == 1:
        return 295
    elif 3151 <= x <= 3200 and y == 2:
        return 455
    elif 3151 <= x <= 3200 and y == 3:
        return 615
    elif 3151 <= x <= 3200 and y >= 4:
        return 935

    elif 3201 <= x <= 3250 and y == 0:
        return 120
    elif 3201 <= x <= 3250 and y == 1:
        return 280
    elif 3201 <= x <= 3250 and y == 2:
        return 440
    elif 3201 <= x <= 3250 and y == 3:
        return 600
    elif 3201 <= x <= 3250 and y >= 4:
        return 920

    elif 3251 <= x <= 3300 and y == 0:
        return 105
    elif 3251 <= x <= 3300 and y == 1:
        return 265
    elif 3251 <= x <= 3300 and y == 2:
        return 425
    elif 3251 <= x <= 3300 and y == 3:
        return 585
    elif 3251 <= x <= 3300 and y >= 4:
        return 905

    elif 3301 <= x <= 3350 and y == 0:
        return 90
    elif 3301 <= x <= 3350 and y == 1:
        return 250
    elif 3301 <= x <= 3350 and y == 2:
        return 410
    elif 3301 <= x <= 3350 and y == 3:
        return 570
    elif 3301 <= x <= 3350 and y >= 4:
        return 890

    elif 3351 <= x <= 3400 and y == 0:
        return 75
    elif 3351 <= x <= 3400 and y == 1:
        return 235
    elif 3351 <= x <= 3400 and y == 2:
        return 395
    elif 3351 <= x <= 3400 and y == 3:
        return 555
    elif 3351 <= x <= 3400 and y >= 4:
        return 875

    elif 3401 <= x <= 3450 and y == 0:
        return 60
    elif 3401 <= x <= 3450 and y == 1:
        return 220
    elif 3401 <= x <= 3450 and y == 2:
        return 380
    elif 3401 <= x <= 3450 and y == 3:
        return 540
    elif 3401 <= x <= 3450 and y >= 4:
        return 860

    elif 3451 <= x <= 3500 and y == 0:
        return 45
    elif 3451 <= x <= 3500 and y == 1:
        return 205
    elif 3451 <= x <= 3500 and y == 2:
        return 365
    elif 3451 <= x <= 3500 and y == 3:
        return 525
    elif 3451 <= x <= 3500 and y >= 4:
        return 845

    elif 3501 <= x <= 3550 and y == 0:
        return 30
    elif 3501 <= x <= 3550 and y == 1:
        return 190
    elif 3501 <= x <= 3550 and y == 2:
        return 350
    elif 3501 <= x <= 3550 and y == 3:
        return 510
    elif 3501 <= x <= 3550 and y >= 4:
        return 830

    elif 3551 <= x <= 3600 and y == 0:
        return 15
    elif 3551 <= x <= 3600 and y == 1:
        return 175
    elif 3551 <= x <= 3600 and y == 2:
        return 335
    elif 3551 <= x <= 3600 and y == 3:
        return 495
    elif 3551 <= x <= 3600 and y >= 4:
        return 815
    else:
        return 0

def CAM(x):
    return x*2.25/100

def SALARIUNET(a,b,c,d):
    return a - b - c - d

def CalculatorPTSAlariuNET():
    e5.config(state='normal')
    e5.delete(0, tk.END)
    e5.config(state='disabled')
    a = int(e1.get())
    p = int(e2.get())
    b = round(CAS(a))
    c = round(CASS(a))
    e = (deducerePersonala(a, p))
    Dimp = a - b - c - e
    d = round(ImpozitPeVenit(Dimp))
    x = round(CAM(a))
    exe = SALARIUNET(a, b, c, d)
    e5.config(state='normal')
    e5.insert(0, exe)
    e5.config(state='disabled')

def CalculatorPTSAlariuBrut():
    e10.config(state='normal')
    e10.delete(0, tk.END)
    e10.config(state='disabled')
    q = int(e3.get())
    p = int(e4.get())
    a = round(q/0.585)
    b = round(CAS(a))
    c = round(CASS(a))
    e = (deducerePersonala(a, p))
    Dimp = a - b - c - e
    d = round(ImpozitPeVenit(Dimp))
    x = round(CAM(a))
    exe = SALARIUNET(a, b, c, d)
    e10.config(state='normal')
    e10.insert(0, a)
    e10.config(state='disabled')













root = Tk()
root.geometry("1000x600")
root.config(bg="white")
root.resizable(width=False, height=False)
root.title('Calculator Salarii')

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

my_frame1 = Frame(my_notebook, width=1000, height=600, bg='#0099FF')
my_frame2 = Frame(my_notebook, width=1000, height=600, bg='#0099FF')

my_frame1.pack(fill='both', expand=1)
my_frame2.pack(fill='both', expand=1)


my_notebook.add(my_frame1, text="Salariu NET")
my_notebook.add(my_frame2, text="Salariu BRUT")

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v10 = StringVar()






l2 = Label(my_frame1, text="Salariu brut:", font=("Arial", 10), fg="Black", bg='#0099FF')
e1 = Entry(my_frame1, font=("Arial", 11), textvariable=v1, borderwidth=5)

l3 = Label(my_frame1, text="Persoane in intretinere:", font=("Arial", 10), fg="Black", bg='#0099FF')
e2 = Entry(my_frame1, font=("Arial", 11), textvariable=v2, borderwidth=5)

b1 = Button(my_frame1, text="Calcul salariu net", font=("Arial", 15), command=CalculatorPTSAlariuNET, bg='#0099FF')

l6 = Label(my_frame1, text="Salariu NET", font=("Arial", 10), fg="Black", bg='#0099FF')
e5 = Entry(my_frame1, font=("Arial", 11), state='disabled', textvariable=v5, borderwidth=5)









l4 = Label(my_frame2, text="Salariu net:", font=("Arial", 10), fg="Black", bg='#0099FF')
e3 = Entry(my_frame2, font=("Arial", 11), textvariable=v3, borderwidth=5)

l5 = Label(my_frame2, text="Persoane in intretinere:", font=("Arial", 10), fg="Black", bg='#0099FF')
e4 = Entry(my_frame2, font=("Arial", 11), textvariable=v4, borderwidth=5)

b2 = Button(my_frame2, text="Calcul salariu brut", font=("Arial", 15), command=CalculatorPTSAlariuBrut, bg='#0099FF')

l10 = Label(my_frame2, text="Salariu Brut", font=("Arial", 10), fg="Black", bg='#0099FF')
e10 = Entry(my_frame2, font=("Arial", 11), state='disabled', textvariable=v10, borderwidth=5)








# l1.place(x=512, y=123)
l2.place(x=20, y=70)
e1.place(x=170, y=70)
l3.place(x=20, y=100)
e2.place(x=170, y=100)
l4.place(x=20, y=70)
e3.place(x=170, y=70)
l5.place(x=20, y=100)
e4.place(x=170, y=100)
b1.place(x=60, y=200)
l6.place(x=20, y=260)
e5.place(x=170, y=260)
l10.place(x=20, y=260)
e10.place(x=170, y=260)
b2.place(x=60, y=200)
# b3.place(x=60, y=350)




root.mainloop()