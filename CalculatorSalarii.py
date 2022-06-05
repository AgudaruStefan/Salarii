from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk1
import tkinter as tk
import requests
import datetime

date = datetime.datetime.now()

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=RON&base=EUR"

payload = {}
headers= {
  "apikey": "iuGyKo2kbkA02aHdzQF3pIJLKruKpW5A"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
exchange_rate = result['rates']["RON"]

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
    e21.config(state='normal')
    e21.delete(0, tk.END)
    e21.config(state='disabled')
    e22.config(state='normal')
    e22.delete(0, tk.END)
    e22.config(state='disabled')
    e23.config(state='normal')
    e23.delete(0, tk.END)
    e23.config(state='disabled')
    e24.config(state='normal')
    e24.delete(0, tk.END)
    e24.config(state='disabled')
    e26.config(state='normal')
    e26.delete(0, tk.END)
    e26.config(state='disabled')
    ee21.config(state='normal')
    ee21.delete(0, tk.END)
    ee21.config(state='disabled')
    ee22.config(state='normal')
    ee22.delete(0, tk.END)
    ee22.config(state='disabled')
    ee23.config(state='normal')
    ee23.delete(0, tk.END)
    ee23.config(state='disabled')
    ee24.config(state='normal')
    ee24.delete(0, tk.END)
    ee24.config(state='disabled')
    ee26.config(state='normal')
    ee26.delete(0, tk.END)
    ee26.config(state='disabled')
    eNET2.config(state='normal')
    eNET2.delete(0, tk.END)
    eNET2.config(state='disabled')
    eNET.config(state='normal')
    eNET.delete(0, tk.END)
    eNET.config(state='disabled')
    a = int(e1.get())
    p = int(e2.get())
    b = round(CAS(a))
    c = round(CASS(a))
    e = (deducerePersonala(a, p))
    Dimp = a - b - c - e
    d = round(ImpozitPeVenit(Dimp))
    x = round(CAM(a))
    exe = SALARIUNET(a, b, c, d)
    netEntry = round(a/exchange_rate)
    exeEUR = round(exe/exchange_rate)
    bEUR = round(b/exchange_rate)
    cEUR = round(c/exchange_rate)
    eEUR = round(e/exchange_rate)
    dEUR = round(d/exchange_rate)
    xEUR = round(x/exchange_rate)
    e5.config(state='normal')
    e5.insert(0, exe)
    e5.config(state='disabled')
    e21.config(state='normal')
    e21.insert(0, b)
    e21.config(state='disabled')
    e22.config(state='normal')
    e22.insert(0, c)
    e22.config(state='disabled')
    e23.config(state='normal')
    e23.insert(0, e)
    e23.config(state='disabled')
    e24.config(state='normal')
    e24.insert(0, d)
    e24.config(state='disabled')
    e26.config(state='normal')
    e26.insert(0, x)
    e26.config(state='disabled')
    ee21.config(state='normal')
    ee21.insert(0, bEUR)
    ee21.config(state='disabled')
    ee22.config(state='normal')
    ee22.insert(0, cEUR)
    ee22.config(state='disabled')
    ee23.config(state='normal')
    ee23.insert(0, eEUR)
    ee23.config(state='disabled')
    ee24.config(state='normal')
    ee24.insert(0, dEUR)
    ee24.config(state='disabled')
    ee26.config(state='normal')
    ee26.insert(0, xEUR)
    ee26.config(state='disabled')
    eNET2.config(state='normal')
    eNET2.insert(0, exeEUR)
    eNET2.config(state='disabled')
    eNET.config(state='normal')
    eNET.insert(0, netEntry)
    eNET.config(state='disabled')

def CalculatorPTSAlariuBrut():
    e10.config(state='normal')
    e10.delete(0, tk.END)
    e10.config(state='disabled')
    e21K.config(state='normal')
    e21K.delete(0, tk.END)
    e21K.config(state='disabled')
    e22K.config(state='normal')
    e22K.delete(0, tk.END)
    e22K.config(state='disabled')
    e23K.config(state='normal')
    e23K.delete(0, tk.END)
    e23K.config(state='disabled')
    e24K.config(state='normal')
    e24K.delete(0, tk.END)
    e24K.config(state='disabled')
    e26K.config(state='normal')
    e26K.delete(0, tk.END)
    e26K.config(state='disabled')
    ee21K.config(state='normal')
    ee21K.delete(0, tk.END)
    ee21K.config(state='disabled')
    ee22K.config(state='normal')
    ee22K.delete(0, tk.END)
    ee22K.config(state='disabled')
    ee23K.config(state='normal')
    ee23K.delete(0, tk.END)
    ee23K.config(state='disabled')
    ee24K.config(state='normal')
    ee24K.delete(0, tk.END)
    ee24K.config(state='disabled')
    ee26K.config(state='normal')
    ee26K.delete(0, tk.END)
    ee26K.config(state='disabled')
    eNET2K.config(state='normal')
    eNET2K.delete(0, tk.END)
    eNET2K.config(state='disabled')
    eNETK.config(state='normal')
    eNETK.delete(0, tk.END)
    eNETK.config(state='disabled')
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
    netEntry = round(exe / exchange_rate)
    exeEUR = round(a / exchange_rate)
    bEUR = round(b / exchange_rate)
    cEUR = round(c / exchange_rate)
    eEUR = round(e / exchange_rate)
    dEUR = round(d / exchange_rate)
    xEUR = round(x / exchange_rate)
    e10.config(state='normal')
    e10.insert(0, a)
    e10.config(state='disabled')
    e21K.config(state='normal')
    e21K.insert(0, b)
    e21K.config(state='disabled')
    e22K.config(state='normal')
    e22K.insert(0, c)
    e22K.config(state='disabled')
    e23K.config(state='normal')
    e23K.insert(0, e)
    e23K.config(state='disabled')
    e24K.config(state='normal')
    e24K.insert(0, d)
    e24K.config(state='disabled')
    e26K.config(state='normal')
    e26K.insert(0, x)
    e26K.config(state='disabled')
    ee21K.config(state='normal')
    ee21K.insert(0, bEUR)
    ee21K.config(state='disabled')
    ee22K.config(state='normal')
    ee22K.insert(0, cEUR)
    ee22K.config(state='disabled')
    ee23K.config(state='normal')
    ee23K.insert(0, eEUR)
    ee23K.config(state='disabled')
    ee24K.config(state='normal')
    ee24K.insert(0, dEUR)
    ee24K.config(state='disabled')
    ee26K.config(state='normal')
    ee26K.insert(0, xEUR)
    ee26K.config(state='disabled')
    eNET2K.config(state='normal')
    eNET2K.insert(0, exeEUR)
    eNET2K.config(state='disabled')
    eNETK.config(state='normal')
    eNETK.insert(0, netEntry)
    eNETK.config(state='disabled')




root = tk1.ThemedTk()
root.get_themes()
root.set_theme("plastik")
root.geometry("1100x500")
root.config(bg="white")
root.resizable(width=False, height=False)
root.title('Calculator Salarii')

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

my_frame1 = Frame(my_notebook, width=1200, height=600, bg='#89CFF0')
my_frame2 = Frame(my_notebook, width=1200, height=600, bg='#89CFF0')

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

v21 = StringVar()
v22 = StringVar()
v23 = StringVar()
v24 = StringVar()
v25 = StringVar()

v21E = StringVar()
v22E = StringVar()
v23E = StringVar()
v24E = StringVar()
v25E = StringVar()

euronet = StringVar()
euronet2 = StringVar()

v21k = StringVar()
v22k = StringVar()
v23k = StringVar()
v24k = StringVar()
v25k = StringVar()

v21Ek = StringVar()
v22Ek = StringVar()
v23Ek = StringVar()
v24Ek = StringVar()
v25Ek = StringVar()

euronetk = StringVar()
euronet2k = StringVar()


l2 = Label(my_frame1, text="Salariu brut*:", font=("Arial Bold", 10), fg="Red", bg='#89CFF0')
e1 = Entry(my_frame1, font=("Arial", 11), textvariable=v1, borderwidth=3)

l3 = Label(my_frame1, text="Persoane in intretinere*:", font=("Arial Bold", 10), fg="Red", bg='#89CFF0')
e2 = Entry(my_frame1, font=("Arial", 11), textvariable=v2, borderwidth=3)
# Calculnet_btn = PhotoImage(file='desktop/calculate-buton-md.png')
b1 = ttk.Button(my_frame1, text="Calcul salariu net",  command=CalculatorPTSAlariuNET)

l6 = Label(my_frame1, text="Salariu NET:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
e5 = Entry(my_frame1, font=("Arial", 11), state='disabled', textvariable=v5, borderwidth=3)


l4 = Label(my_frame2, text="Salariu net*:", font=("Arial Bold", 10), fg="Red", bg='#89CFF0')
e3 = Entry(my_frame2, font=("Arial", 11), textvariable=v3, borderwidth=3)

l5 = Label(my_frame2, text="Persoane in intretinere*:", font=("Arial Bold", 10), fg="Red", bg='#89CFF0')
e4 = Entry(my_frame2, font=("Arial", 11), textvariable=v4, borderwidth=3)

b2 = ttk.Button(my_frame2, text="Calcul salariu brut",  command=CalculatorPTSAlariuBrut)

l10 = Label(my_frame2, text="Salariu BRUT:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
e10 = Entry(my_frame2, font=("Arial", 11), state='disabled', textvariable=v10, borderwidth=3)



#contributii frame 1
euroL = Label(my_frame1, text="EURO", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
leiL = Label(my_frame1, text="LEI", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l20 = Label(my_frame1, text="Contributii angajat:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')

l21 = Label(my_frame1, text="CAS:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l22 = Label(my_frame1, text="CASS:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l23 = Label(my_frame1, text="Deducere personala:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l24 = Label(my_frame1, text="Impozit pe venit:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')

l25 = Label(my_frame1, text="Contributii angajator:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l26 = Label(my_frame1, text="CAM:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')

# entry variable

e21 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v21, borderwidth=3)
ee21 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v21E, borderwidth=3)

e22 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v22, borderwidth=3)
ee22 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v22E, borderwidth=3)

e23 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v23, borderwidth=3)
ee23 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v23E, borderwidth=3)

e24 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v24, borderwidth=3)
ee24 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v24E, borderwidth=3)

e26 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v25, borderwidth=3)
ee26 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=v25E, borderwidth=3)

# first entry ------------------------
lEURONET = Label(my_frame1, text="LEI", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
lEURONET2 = Label(my_frame1, text="EURO", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
eNET = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=euronet, borderwidth=3)
eNET2 = Entry(my_frame1,font=("Arial", 11), state='disabled', textvariable=euronet2, borderwidth=3)



eurolabel1 = Label(my_frame1, text=f"1 Euro = {exchange_rate}", font=("Arial Bold", 10), fg="Black", bg='white')
eurolabel2 = Label(my_frame2, text=f"1 Euro = {exchange_rate}", font=("Arial Bold", 10), fg="Black", bg='white')
eurolabel1.place(x= 70, y= 350)
eurolabel2.place(x= 70, y= 350)
# contributii place
l20.place(x=500, y=70)
l21.place(x=500, y=100)
l22.place(x=500, y=130)
l23.place(x=500, y=160)
l24.place(x=500, y=190)
l25.place(x=500, y=250)
l26.place(x=500, y=280)

e21.place(x=700, y=100)
e22.place(x=700, y=130)
e23.place(x=700, y=160)
e24.place(x=700, y=190)
e26.place(x=700, y=280)

ee21.place(x=850, y=100)
ee22.place(x=850, y=130)
ee23.place(x=850, y=160)
ee24.place(x=850, y=190)
ee26.place(x=850, y=280)

leiL.place(x=700, y=70)
euroL.place(x=980, y=70)

# ---------------


lEURONET2.place(x=300, y=40)
eNET.place(x=300, y=70)
eNET2.place(x=300, y=260)
lEURONET.place(x=170, y=40)




#contributii frame 2

euroLK = Label(my_frame2, text="EURO", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
leiLK = Label(my_frame2, text="LEI", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l20K = Label(my_frame2, text="Contributii angajat:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')

l21K = Label(my_frame2, text="CAS:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l22K = Label(my_frame2, text="CASS:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l23K = Label(my_frame2, text="Deducere personala:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l24K = Label(my_frame2, text="Impozit pe venit :", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')

l25K = Label(my_frame2, text="Contributii angajator:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')
l26K = Label(my_frame2, text="CAM:", font=("Arial Bold", 10), fg="Black", bg='#89CFF0')

# entry variable

e21K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v21k, borderwidth=3)
ee21K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v21Ek, borderwidth=3)

e22K= Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v22k, borderwidth=3)
ee22K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v22Ek, borderwidth=3)

e23K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v23k, borderwidth=3)
ee23K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v23Ek, borderwidth=3)

e24K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v24k, borderwidth=3)
ee24K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v24Ek, borderwidth=3)

e26K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v25k, borderwidth=3)
ee26K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=v25Ek, borderwidth=3)

# first entry ------------------------
lEURONETK = Label(my_frame2, text="LEI", font=("Arial bold", 10), fg="Black", bg='#89CFF0')
lEURONET2K = Label(my_frame2, text="EURO", font=("Arial bold", 10), fg="Black", bg='#89CFF0')
eNETK = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=euronetk, borderwidth=3)
eNET2K = Entry(my_frame2,font=("Arial", 11), state='disabled', textvariable=euronet2k, borderwidth=3)
dataora = Label(my_frame1, text=f"{date:%A, %B %d, %Y}", font=("Arial bold", 10))
dataora1 = Label(my_frame2, text=f"{date:%A, %B %d, %Y}", font=("Arial bold", 10))
dataora.place(x= 800, y= 350)
dataora1.place(x= 800, y= 350)
avertisment1 = Label(my_frame1, text="(EX:0,1,2..)", font=("Arial bold", 10), fg="Black", bg='#89CFF0')
avertisment2 = Label(my_frame2, text="(EX:0,1,2..)", font=("Arial bold", 10), fg="Black", bg='#89CFF0')
avertisment1.place(x=350, y=105)
avertisment2.place(x=350, y=105)
# contributii place
l20K.place(x=500, y=70)
l21K.place(x=500, y=100)
l22K.place(x=500, y=130)
l23K.place(x=500, y=160)
l24K.place(x=500, y=190)
l25K.place(x=500, y=250)
l26K.place(x=500, y=280)

e21K.place(x=700, y=100)
e22K.place(x=700, y=130)
e23K.place(x=700, y=160)
e24K.place(x=700, y=190)
e26K.place(x=700, y=280)

ee21K.place(x=850, y=100)
ee22K.place(x=850, y=130)
ee23K.place(x=850, y=160)
ee24K.place(x=850, y=190)
ee26K.place(x=850, y=280)

leiLK.place(x=700, y=70)
euroLK.place(x=980, y=70)

# ---------------


lEURONET2K.place(x=300, y=40)
eNETK.place(x=300, y=70)
eNET2K.place(x=300, y=260)
lEURONETK.place(x=170, y=40)












# l1.place(x=512, y=123)
l2.place(x=20, y=70)
e1.place(x=170, y=70)
l3.place(x=20, y=100)
e2.place(x=180, y=100)
l4.place(x=20, y=70)
e3.place(x=170, y=70)
l5.place(x=20, y=100)
e4.place(x=180, y=100)
b1.place(x=60, y=200)
l6.place(x=20, y=260)
e5.place(x=170, y=260)
l10.place(x=20, y=260)
e10.place(x=170, y=260)
b2.place(x=60, y=200)
# b3.place(x=60, y=350)




root.mainloop()