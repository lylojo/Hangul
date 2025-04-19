from tkinter import *
from importer import flattened_list
import random
from time import sleep
import threading

root = Tk()
root.geometry('940x800+200+10')
root.resizable()
root.overrideredirect(True)

#Functionality
totaltime=60
time=0
wrongwords = 0
elapsedtimeinminutes =0

def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state = NORMAL)
    textarea.focus()

    for time in range(1,61):
        elapsed_time_label.config(text= time)
        remaining_time = totaltime - time
        remaining_time_label.config(text= remaining_time)
        sleep(1)
        root.update()

    textarea.config(state = DISABLED)
    resetButton.config(state = NORMAL)

def count():
    global wrongwords
    while time != totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        total_words = len(entered_paragraph)

    totalwords_count_label.config(text= total_words)

    para_word_list = label_paragraph['text'].split()

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0] != pair[1]:
            wrongwords += 1

    wrongwords_count_label.config(text= wrongwords)

    elapsedtimeinminutes = time/60
    wpm = (total_words-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text= wpm)

    gross_wpm = total_words / elapsedtimeinminutes
    accuracy = wpm/gross_wpm *100
    accuracy = round(accuracy)
    accuracy_percent_label.config(text= str(accuracy) + '%')

def start():
    t1 = threading.Thread(target = start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()

def reset():
    global time, elapsedtimeinminutes
    time=0
    elapsedtimeinminutes = 0

    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    elapsed_time_label.config(text= '0')
    remaining_time_label.config(text= '0')
    wpm_count_label.config(text= '0')
    accuracy_percent_label(text = '0')
    totalwords_count_label.config(text= '0')
    wrongwords_count_label.config(text= '0')

#GUI

mainframe = Frame(root,bd=10)
mainframe.grid()

titleframe = Frame(mainframe,bg='OliveDrab4')
titleframe.grid()

titleLabel = Label(titleframe, text='Hangul Typing!!', font=('Baskerville Old Face', 29), bg='DarkOliveGreen2',fg='OliveDrab4', width=41, bd = 10)
titleLabel.grid(pady=3)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0)

#paragraph_list = random.sample(flattened_list,20)

label_paragraph=Label(paragraph_frame, text = random.sample(flattened_list,20), wraplength=912, justify=CENTER, font=('BatangChe', 23, 'bold'),fg='OliveDrab4')
label_paragraph.grid(row=0, column=0, pady=20)

#typing area

textarea_frame=Frame(mainframe, bg='OliveDrab4')
textarea_frame.grid(row=2, column=0)

textarea=Text(textarea_frame, font=('BatangChe', 20, 'bold'),fg='OliveDrab4', width=50, height = 7, bd=4, relief= FLAT, wrap=WORD, state=DISABLED)
textarea.grid(row=0, column=0)

#labels

frame_output = Frame(mainframe)
frame_output.grid(row=3, column=0)

elapsed_time_label = Label(frame_output, text = 'Elapsed Time', font = ('Baskerville Old Face', 12, 'bold'), fg='OliveDrab4')
elapsed_time_label.grid(row=0, column=0, padx=5, pady=5)

elapsed_time_label = Label(frame_output, text = '0', font = ('Baskerville Old Face', 12), fg='OliveDrab4')
elapsed_time_label.grid(row=0, column=1, padx=5, pady=5)

remaining_time_label = Label(frame_output, text = 'Remaining Time', font = ('Baskerville Old Face', 12, 'bold'), fg='OliveDrab4')
remaining_time_label.grid(row=0, column=2, padx=5, pady=5)

remaining_time_label = Label(frame_output, text = '60', font = ('Baskerville Old Face', 12), fg='OliveDrab4')
remaining_time_label.grid(row=0, column=3, padx=5, pady=5)

wpm_label = Label(frame_output, text = 'WPM', font = ('Baskerville Old Face', 12, 'bold'), fg='OliveDrab4')
wpm_label.grid(row=0, column=4, padx=5, pady=5)

wpm_count_label = Label(frame_output, text = '0', font = ('Baskerville Old Face', 12), fg='OliveDrab4')
wpm_count_label.grid(row=0, column=5, padx=5, pady=5)

totalwords_label = Label(frame_output, text = 'Total Words', font = ('Baskerville Old Face', 12, 'bold'), fg='OliveDrab4')
totalwords_label.grid(row=0, column=6, padx=5, pady=5)

totalwords_count_label = Label(frame_output, text = '0', font = ('Baskerville Old Face', 12), fg='OliveDrab4')
totalwords_count_label.grid(row=0, column=7, padx=5, pady=5)

wrongwords_label = Label(frame_output, text = 'Wrong Words', font = ('Baskerville Old Face', 12, 'bold'), fg='OliveDrab4')
wrongwords_label.grid(row=0, column=8, padx=5, pady=5)

wrongwords_count_label = Label(frame_output, text = '0', font = ('Baskerville Old Face', 12), fg='OliveDrab4')
wrongwords_count_label.grid(row=0, column=9, padx=5, pady=5)

accuracy_label = Label(frame_output, text = 'Accuracy', font = ('Baskerville Old Face', 12, 'bold'), fg='OliveDrab4')
accuracy_label.grid(row=0, column=10, padx=5, pady=5)

accuracy_percent_label = Label(frame_output, text = '0', font = ('Baskerville Old Face', 12), fg='OliveDrab4')
accuracy_percent_label.grid(row=0, column=11, padx=5, pady=5)

#buttons

buttons_frame = Frame(mainframe)
buttons_frame.grid(row=4, column=0)

startButton=Button(buttons_frame,text='Start', command=start, font = ('Baskerville Old Face', 12, 'bold'), bg='DarkOliveGreen2', fg='OliveDrab4', width=10, bd=4, highlightthickness=4, highlightbackground='OliveDrab4', highlightcolor='OliveDrab4',relief=RIDGE)
startButton.grid(row=0, column=0, padx=10, pady=15)

resetButton=Button(buttons_frame,text='Reset', state=DISABLED, command=reset, font = ('Baskerville Old Face', 12, 'bold'), bg='DarkOliveGreen2', fg='OliveDrab4', width=10, bd=4, highlightthickness=4, highlightbackground='OliveDrab4', highlightcolor='OliveDrab4', relief = RIDGE)
resetButton.grid(row=0, column=1, padx=10, pady=15)

exitButton=Button(buttons_frame,text='Exit', command=root.destroy, font = ('Baskerville Old Face', 12, 'bold'), bg='DarkOliveGreen2', fg='OliveDrab4', width=10, bd=4, highlightthickness=4, highlightbackground='OliveDrab4', highlightcolor='OliveDrab4', relief = RIDGE)
exitButton.grid(row=0, column=2, padx=10, pady=15)

#keyboard

keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5, column=0)

frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0, column=0)
label1=Label(frame1to0, text='1', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label1.grid(row=0, column=0, padx=5, pady=5)
label2=Label(frame1to0, text='2', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label2.grid(row=0, column=1, padx=5, pady=5)
label3=Label(frame1to0, text='3', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label3.grid(row=0, column=2, padx=5, pady=5)
label4=Label(frame1to0, text='4', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label4.grid(row=0, column=3, padx=5, pady=5)
label5=Label(frame1to0, text='5', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label5.grid(row=0, column=4, padx=5, pady=5)
label6=Label(frame1to0, text='6', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label6.grid(row=0, column=5, padx=5, pady=5)
label7=Label(frame1to0, text='7', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label7.grid(row=0, column=6, padx=5, pady=5)
label8=Label(frame1to0, text='8', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label8.grid(row=0, column=7, padx=5, pady=5)
label9=Label(frame1to0, text='9', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label9.grid(row=0, column=8, padx=5, pady=5)
label0=Label(frame1to0, text='0', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
label0.grid(row=0, column=9, padx=5, pady=5)

frameqtop=Frame(keyboard_frame)
frameqtop.grid(row=1, column=0)
labelq=Label(frameqtop, text='ㅂ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelq.grid(row=0, column=0, padx=5, pady=5)
labelw=Label(frameqtop, text='ㅈ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelw.grid(row=0, column=1, padx=5, pady=5)
labele=Label(frameqtop, text='ㄷ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labele.grid(row=0, column=2, padx=5, pady=5)
labelr=Label(frameqtop, text='ㄱ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelr.grid(row=0, column=3, padx=5, pady=5)
labelt=Label(frameqtop, text='ㅅ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelt.grid(row=0, column=4, padx=5, pady=5)
labely=Label(frameqtop, text='ㅛ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labely.grid(row=0, column=5, padx=5, pady=5)
labelu=Label(frameqtop, text='ㅕ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelu.grid(row=0, column=6, padx=5, pady=5)
labeli=Label(frameqtop, text='ㅑ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labeli.grid(row=0, column=7, padx=5, pady=5)
labelo=Label(frameqtop, text='ㅐ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelo.grid(row=0, column=8, padx=5, pady=5)
labelp=Label(frameqtop, text='ㅔ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelp.grid(row=0, column=9, padx=5, pady=5)

frameatol = Frame(keyboard_frame)
frameatol.grid(row=2, column=0)
labela=Label(frameatol, text='ㅁ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labela.grid(row=0, column=0, padx=5, pady=5)
labels=Label(frameatol, text='ㄴ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labels.grid(row=0, column=1, padx=5, pady=5)
labeld=Label(frameatol, text='ㅇ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labeld.grid(row=0, column=2, padx=5, pady=5)
labelf=Label(frameatol, text='ㄹ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelf.grid(row=0, column=3, padx=5, pady=5)
labelg=Label(frameatol, text='ㅎ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelg.grid(row=0, column=4, padx=5, pady=5)
labelh=Label(frameatol, text='ㅗ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelh.grid(row=0, column=5, padx=5, pady=5)
labelj=Label(frameatol, text='ㅓ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelj.grid(row=0, column=6, padx=5, pady=5)
labelk=Label(frameatol, text='ㅏ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelk.grid(row=0, column=7, padx=5, pady=5)
labell=Label(frameatol, text='ㅣ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labell.grid(row=0, column=8, padx=5, pady=5)

frameztom = Frame(keyboard_frame)
frameztom.grid(row=3,column=0)
labelz=Label(frameztom, text='ㅋ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelz.grid(row=0, column=0, padx=5, pady=5)
labelx=Label(frameztom, text='ㅌ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelx.grid(row=0, column=1, padx=5, pady=5)
labelc=Label(frameztom, text='ㅊ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelc.grid(row=0, column=2, padx=5, pady=5)
labelv=Label(frameztom, text='ㅍ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelv.grid(row=0, column=3, padx=5, pady=5)
labelb=Label(frameztom, text='ㅠ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelb.grid(row=0, column=4, padx=5, pady=5)
labeln=Label(frameztom, text='ㅜ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labeln.grid(row=0, column=5, padx=5, pady=5)
labelm=Label(frameztom, text='ㅡ', font=('BatangChe', 12, 'bold'), width=4, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelm.grid(row=0, column=6, padx=5, pady=5)

spaceframe=Frame(keyboard_frame)
spaceframe.grid(row=4,column=0)
labelSpace=Label(spaceframe, font=('BatangChe', 12, 'bold'), width=40, height = 2, bg='OliveDrab4', fg='DarkOliveGreen2', highlightthickness=1, highlightbackground='DarkOliveGreen2', highlightcolor='DarkOliveGreen2', relief=GROOVE)
labelSpace.grid(row=0, column=0, padx=5, pady=5)

#keyboard highlight
korean_uppercase = ['ㅃ','ㅉ','ㄸ','ㄲ','ㅆ','ㅒ','ㅖ']
korean_lowercase = ['ㅂ','ㅈ','ㄷ','ㄱ','ㅅ','ㅐ','ㅔ']

def changeBG(widget):
    widget.config(bg='DarkOliveGreen2', fg='OliveDrab4')
    widget.after(200, lambda :widget.config(bg='OliveDrab4', fg='DarkOliveGreen2'))

def changeText(widget):
    widget.config(bg='DarkOliveGreen2', fg='OliveDrab4', text= korean_uppercase[widget.indexOf(widget)])
    widget.after(200, lambda: widget.config(bg='OliveDrab4', fg='DarkOliveGreen2', text=korean_lowercase[widget.indexOf(widget)]))

label_numbers=[label1, label2, label3, label4, label5, label6, label7, label8, label9, label0]
label_capital_alphabet=[labelq, labelw, labele, labelr, labelt, labelo, labelp]
label_small_alphabet=[labela, labelb, labelc, labeld, labele, labelf, labelg, labelh, labeli, labelj, labelk, labell, labelm, labeln,labelo,labelp, labelq, labelr, labels, labelt,labelu, labelv, labelw, labelx, labely, labelz]
space_label = [labelSpace]

binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
binding_capital_alphabet = ['Q','W','E','R','T','O','P']
binding_small_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers], lambda event, label=label_numbers[numbers]:changeBG(label))

for capital_alphabet in range(len(binding_capital_alphabet)):
    root.bind(binding_capital_alphabet[capital_alphabet], lambda event, label=label_capital_alphabet[capital_alphabet]:changeBG(label))

for small_alphabet in range(len(binding_small_alphabet)):
    root.bind(binding_small_alphabet[small_alphabet], lambda event, label=label_small_alphabet[small_alphabet]:changeBG(label))

root.bind('<space>',lambda event: changeBG(labelSpace))

root.mainloop()