from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pickle

global count, check, local_count, height, repere, cycles, number, lbl, txt, btn, lbl_new, plus, click_load, \
    save_cyc, save_height, l, save_repere

check = 0
cycles = []
l = 0


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def clicked_minus():
    global count, check, local_count, repere, cycles, number, lbl, txt, btn, lbl_new, plus
    plus = 0
    r = 0
    for i in txt.get():
        if i.isalpha():
            r += 1
    if txt.get() != "" and r == 0:
        lbl_new.configure(text="")
        if check == 0:
            count = int(txt.get())
            local_count = count
            lbl.configure(text="Введите количество реперов", padx=192)
            txt.delete(0, END)
            check = 2
        elif check == 2:
            repere = int(txt.get())
            lbl.configure(text="Введите данные о высотах цикла №1", padx=133)
            txt.delete(0, END)
            check = 3
            number = 1
        elif check == 3:
            a = txt.get()
            check_1 = 0
            check_2 = 0
            for i in a:
                if i == " ":
                    check_1 += 1
                elif i == "\r":
                    check_2 += 1
            if check_1 > 0:
                b = a.split(" ")
            elif check_2 > 0:
                b = a.split('\r\n')
            else:
                c = ""
                b = []
                check_minus = 0
                for i in range(len(a)):
                    c += a[i]
                    if i <= len(a) - 3:
                        if a[i + 1] == "-":
                            b.append(c)
                            c = ""
                            check_minus = 1
                        elif a[i + 2] == "." and check_minus != 0:
                            b.append(c)
                            c = ""
                        check_minus -= 1
                    elif i == len(a) - 1:
                        b.append(c)
            t = 0
            for i in b:
                for i1 in range(len(b[t])):
                    if b[t][i1] == ",":
                        c = b[t].split(",")
                        b[t] = c[0] + "." + c[1]
                t += 1
            t = 0
            for i in b:
                b[t] = float(i)
                t += 1
            cycles.append(b)
            txt.delete(0, END)
            number += 1
            local_count -= 1
            lbl.configure(text="Введите данные об изменениях цикла №" + str(number), padx=101)
            if local_count == 0:
                window.destroy()
    else:
        txt.delete(0, END)
        lbl_new.configure(text="Ошибка! Данные отсутствуют либо содержат буквы.")


def clicked_plus():
    global count, check, local_count, height, repere, cycles, number, lbl, txt, btn, lbl_new, plus
    plus = 1
    r = 0
    for i in txt.get():
        if i.isalpha():
            r += 1
    if txt.get() != "" and r == 0:
        lbl_new.configure(text="")
        if check == 0:
            count = int(txt.get())
            local_count = count
            lbl.configure(text="Введите количество реперов", padx=192)
            txt.delete(0, END)
            check = 1
        elif check == 1:
            repere = int(txt.get())
            lbl.configure(text="Введите первоначальную высоту", padx=159)
            txt.delete(0, END)
            check = 2
        elif check == 2:
            b = txt.get()
            for i in range(len(txt.get())):
                if txt.get()[i] == ",":
                    a = txt.get().split(",")
                    b = float(a[0] + "." + a[1])
            height = float(b)
            lbl.configure(text="Введите данные об изменениях цикла №1", padx=101)
            txt.delete(0, END)
            check = 3
            number = 1
        elif check == 3:
            a = txt.get()
            check_1 = 0
            check_2 = 0
            for i in a:
                if i == " ":
                    check_1 += 1
                elif i == "\r":
                    check_2 += 1
            if check_1 > 0:
                b = a.split(" ")
            elif check_2 > 0:
                b = a.split('\r\n')
            else:
                c = ""
                b = []
                check_minus = 0
                for i in range(len(a)):
                    c += a[i]
                    if i <= len(a) - 3:
                        if a[i + 1] == "-":
                            b.append(c)
                            c = ""
                            check_minus = 1
                        elif a[i + 2] == "." and check_minus != 0:
                            b.append(c)
                            c = ""
                        check_minus -= 1
                    elif i == len(a) - 1:
                        b.append(c)
            t = 0
            for i in b:
                for i1 in range(len(b[t])):
                    if b[t][i1] == ",":
                        c = b[t].split(",")
                        b[t] = c[0] + "." + c[1]
                t += 1
            t = 0
            for i in b:
                b[t] = float(i)
                t += 1
            cycles.append(b)
            txt.delete(0, END)
            number += 1
            local_count -= 1
            lbl.configure(text="Введите данные об изменениях цикла №" + str(number), padx=101)
            if local_count == 0:
                window.destroy()
    else:
        txt.delete(0, END)
        lbl_new.configure(text="Ошибка! Данные отсутствуют либо содержат буквы.")


def click_plus():
    global lbl, btn, lbl_new, click_load
    lbl.destroy()
    lbl_new.destroy()
    btn.destroy()
    click_load.destroy()
    lbl5.grid(column=0, row=2)
    lbl = Label(window, text="Введите количество циклов", font=("Arial Bold", 28), padx=200, pady=80, bg="#CCC")
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=10)
    txt.grid(column=0, row=1)
    txt.focus()
    btn = Button(window, text="Ввести", font=("Arial Bold", 18), pady=10, command=clicked_plus)
    btn.grid(column=0, row=3)
    lbl_new = Label(window, text="", font=("Times New Roman", 20,), fg='Red', pady=20, bg="#CCC")
    lbl_new.grid(column=0, row=4)


def click_minus():
    global lbl, btn, lbl_new, click_load, txt
    click_load.destroy()
    lbl.destroy()
    lbl_new.destroy()
    btn.destroy()
    lbl5.grid(column=0, row=2)
    lbl = Label(window, text="Введите количество циклов", font=("Arial Bold", 28), padx=200, pady=80, bg="#CCC")
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=10)
    txt.grid(column=0, row=1)
    txt.focus()
    btn = Button(window, text="Ввести", font=("Arial Bold", 18), pady=10, command=clicked_minus)
    btn.grid(column=0, row=3)
    lbl_new = Label(window, text="", font=("Times New Roman", 20,), fg='Red', pady=20, bg="#CCC")
    lbl_new.grid(column=0, row=4)


def ll():
    global l
    l += 2
    load()

def load():
    global lbl, btn, lbl_new, click_load, l, plus, save_cyc, save_height, cycles, local_count, txt, repere, \
        save_repere, number
    l += 1
    click_load.destroy()
    btn.destroy()
    lbl_new.destroy()
    lbl.configure(text="")
    btn = Button(window, text="С расчётом", font=("Arial Bold", 18), pady=10, bg="#CCC", command=ll)
    btn.grid(column=0, row=1)
    lbl_new = Button(window, text="Без расчёта", font=("Arial Bold", 18), pady=10, bg="#CCC", command=load)
    lbl_new.grid(column=0, row=2)
    if l == 2:
        r = 0
        plus = 0
        cycles = pickle.loads(save_cyc)
        lbl.configure(text="Введите количество новых циклов")
        lbl_new.destroy()
        btn.destroy()
        txt = Entry(window, width=10)
        txt.grid(column=0, row=1)
        txt.focus()
        l = 20
        btn = Button(window, text="Ввести", font=("Arial Bold", 18), pady=10, bg="#CCC", command=load)
        btn.grid(column=0, row=2)
    if l != 1:
        for i in txt.get():
            if i.isalpha():
                r += 1
        if txt.get() != "" and r == 0:
            if l == 20:
                local_count = int(lbl_new.get())
                repere = pickle.loads(save_repere)
                lbl.configure(text="Введите данные о высотах нового цикла №1", padx=133)
                txt.delete(0, END)
                number = 1
                l = 40
            elif l == 40:
                a = txt.get()
                check_1 = 0
                check_2 = 0
                for i in a:
                    if i == " ":
                        check_1 += 1
                    elif i == "\r":
                        check_2 += 1
                if check_1 > 0:
                    b = a.split(" ")
                elif check_2 > 0:
                    b = a.split('\r\n')
                else:
                    c = ""
                    b = []
                    check_minus = 0
                    for i in range(len(a)):
                        c += a[i]
                        if i <= len(a) - 3:
                            if a[i + 1] == "-":
                                b.append(c)
                                c = ""
                                check_minus = 1
                            elif a[i + 2] == "." and check_minus != 0:
                                b.append(c)
                                c = ""
                            check_minus -= 1
                        elif i == len(a) - 1:
                            b.append(c)
                t = 0
                for i in b:
                    for i1 in range(len(b[t])):
                        if b[t][i1] == ",":
                            c = b[t].split(",")
                            b[t] = c[0] + "." + c[1]
                    t += 1
                t = 0
                for i in b:
                    b[t] = float(i)
                    t += 1
                cycles.append(b)
                txt.delete(0, END)
                number += 1
                local_count -= 1
                lbl.configure(text="Введите данные об изменениях цикла №" + str(number), padx=101)
                if local_count == 0:
                    window.destroy()





def click_choose():
    global lbl, btn, lbl_new, click_load
    lbl1.destroy()
    lbl2.destroy()
    lbl3.destroy()
    lbl4.destroy()
    btn1.destroy()
    lbl = Label(window,
                text="Выберите формат работы:\n\n1. С расчётом - использовать сырые данные\n\n2. "
                     "Без расчёта - использовать готовые данные",
                font=("Arial Bold", 20), padx=160, pady=40, bg="#CCC")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="С расчётом", font=("Arial Bold", 18), pady=10, bg="#CCC", command=click_plus)
    btn.grid(column=0, row=1)
    lbl5.grid(column=0, row=2)
    lbl_new = Button(window, text="Без расчёта", font=("Arial Bold", 18), pady=10, bg="#CCC", command=click_minus)
    lbl_new.grid(column=0, row=3)
    click_load = Button(window, text="Загрузить", font=("Arial Bold", 18), pady=10, bg="#CCC", command=load)
    click_load.grid(column=0, row=4)


window = Tk()
window.title("TiGraph")
window.geometry('800x400')
window["bg"] = "#CCC"
lbl1 = Label(window, text="Здравствуйте, это приложение Tigraph!", font=("Arial Bold", 25), bg="#CCC", padx=150,
             pady=10)
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Правила пользования:", font=("Times New Roman", 20), pady=50, bg="#CCC")
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Вы можете ввести значения, скопировав таблицу Excel либо", font=("Times New Roman", 20),
             bg="#CCC")
lbl3.grid(column=0, row=2)
lbl4 = Label(window, text="введя их самостоятельно слитно или через пробел.", font=("Times New Roman", 20), bg="#CCC")
lbl4.grid(column=0, row=3)
lbl5 = Label(window, text="", font=("Times New Roman", 20), bg="#CCC")
lbl5.grid(column=0, row=4)
btn1 = Button(window, text="Продолжить", font=("Arial Bold", 18), pady=10, command=click_choose)
btn1.grid(column=0, row=5)

window.mainloop()

if plus == 1:
    for i in range(count):
        difference = 0
        for j in range(repere + 1):
            difference += cycles[i][j]
        if difference > 0:
            for j1 in range(repere + 1):
                cycles[i][j1] -= (difference / repere)
        else:
            for j1 in range(repere + 1):
                cycles[i][j1] += (difference / repere)
        for m in range(repere):
            if m == 0:
                cycles[i][m] += height
            else:
                cycles[i][m] += cycles[i][m - 1]
    save_height = pickle.dumps(height)


save_cyc = pickle.dumps(cycles)
save_repere = pickle.dumps(repere)

graph = []
total = 0
num = 1
n1 = 'Циклы'
n2 = 'Высота'
f = []
for i in range(repere):
    x = np.arange(1, count + 1, 1)
    for j in range(count):
        graph.append(cycles[j][total])
    y = graph
    fig, ax = plt.subplots()
    ax.set_title('Репер №' + str(num))
    ax.plot(x, y)
    ax.set_xticks(x)
    for i in x:
        f.append(str(i))
    ax.set_xticklabels(f)
    f = []
    ax.set_yticks(y)
    for i in graph:
        f.append(str(toFixed(i, 4)))
    ax.set_yticklabels(f)
    ax.grid()
    plt.xlabel(n1)
    plt.ylabel(n2)
    fig.set_figwidth(10)
    fig.set_figheight(6)
    graph = []
    total += 1
    num += 1
    f = []
    plt.show()
