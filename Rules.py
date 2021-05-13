import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from tkinter import messagebox
global error
error=''

def openNewWindow():
      

    newWindow = tk.Tk()
  

    newWindow.title("Easter Egg")

    newWindow.geometry("200x200")
  
    # A Label widget to show in toplevel
    tk.Label(newWindow, 
          text ="Made by Gareth Riley!\n You can download the source code from https://github.com/Gareth-Riley/Ticket_Rules").pack()


def make_Rules(groups,excel,event):
    w=groups.split('\n')
    if len(w)==0:
        messagebox.showerror('No groups listed')
        return
    s=excel.split('\n')
    if len(s)==0:
        messagebox.showerror('No excel input')
        return
    count=len(s)
    
    f= open("RULES.CTL", "w")
    import re
    unprocessed=0
    PreviousXSection=0
    PreviousGate=0
    MIN=1
    MAX=0   
    ClauseCounter=0
    GATE=0
    ReplaceGate='Blah'
    Match=False
    LastMatch=False
    eventCode=event
    if eventCode=='':
        messagebox.showerror("Error",'No eventcode')
        return
    f.write("0,16383,0,1,0,9999,0,9999,0,86399,33,31647\nALL\n")
    counter=0
    while counter<count:

     
        unprocessed=s[counter]
        if unprocessed=="Easter Egg":
            openNewWindow()

        for Gate in w:
            Gate=Gate.replace('\n','')
            if unprocessed.find(Gate)!=-1 and Match!=True:
                ReplaceGate=Gate
                Match=True
        if counter==count-1:
            LastMatch=True
            MAX=PreviousXSection+1
            f.write("1,16383,0,1,"+str(MIN)+","+str(MAX)+","+str(MIN)+","+str(MAX)+",0,86399,0,0\n"+str(CurrentGate)+"\n")   
            
        if Match==True:
            try:
                processed=int(unprocessed.replace(ReplaceGate,''))
            except:
                messagebox.showerror("Error",'Conflict with gate name')
                return
            #print(processed)
            CurrentXSection=processed
            CurrentGate=ReplaceGate
            if CurrentGate!=PreviousGate and(CurrentXSection!='bye' and CurrentGate!=0):
                MAX=PreviousXSection
                f.write("1,16383,0,1,"+str(MIN)+","+str(MAX)+","+str(MIN)+","+str(MAX)+",0,86399,0,0\n"+str(PreviousGate)+"\n")
                ClauseCounter+=1
                MIN=CurrentXSection
            PreviousXSection=CurrentXSection
            PreviousGate=CurrentGate
            counter+=1
        else:
            if counter!=count-1:
                messagebox.showerror("Error",'Gate not defined in Groups'+unprocessed)
                unprocessed='bye bye'
                return
            
        Match=False
    f.write("Always Valid\n0\n"+eventCode+"\n1")
    f.close()

    with open("RULES.CTL", "r") as f:
        value="#VERSION 3.79 Build 12\n2\n"+str(ClauseCounter+1)+"\n"
        contents = f.readlines()

    contents.insert(0, value)

    with open("RULES.CTL", "w") as f:
        contents = "".join(contents)
        f.write(contents)
        messagebox.showinfo(title='Success', message='Sucess')



def make_Rules2(groups,excel,event):
    w=groups.split('\n')
    if len(w)==0:
        messagebox.showerror('No groups listed')
        return
    s=excel.split('\n')
    if len(s)==0:
        messagebox.showerror('No excel input')
        return
    count=len(s)
    
    f= open("RULES.CTL", "w")
    import re
    unprocessed=0
    PreviousXSection=0
    PreviousGate=0
    MIN=1
    MAX=0
    ClauseCounter=0
    GATE=0
    ReplaceGate='Blah'
    Match=False
    LastMatch=False
    eventCode=event
    #print(count)
    if eventCode=='':
        messagebox.showerror("Error",'No eventcode')
        return
    f.write("0,16383,0,1,0,9999,0,9999,0,86399,33,31647\nALL\n")
    counter=0
    while counter<count-1:

     
        unprocessed=s[counter]

        for Gate in w:
            Gate=Gate.replace('\n','')
            if unprocessed.find(Gate)!=-1 and Match!=True:
                ReplaceGate=Gate
                Match=True
            
        if Match==True:
            try:
                processed=unprocessed.replace(ReplaceGate,'')
                processed=processed.lstrip(' ')
                processed=processed.split(' ',1)
                processed[1]=processed[1].replace(' ','')
                if int(processed[1])<=65335:
                    processed[0]=int(processed[0])
                    processed[1]=int(processed[1])
                else:
                    messagebox.showerror("Error",'Max too high')
                    return
            except:

                messagebox.showerror("Error",'Conflict with gate name')
                return
            f.write("1,16383,0,1,"+str(processed[0])+","+str(processed[1])+","+str(processed[0])+","+str(processed[1])+",0,86399,0,0\n"+str(ReplaceGate)+"\n")
            ClauseCounter+=1
            counter+=1
        else:
            if counter!=count-1:
                messagebox.showerror("Error",'Gate not defined in Groups'+unprocessed)
                unprocessed='bye bye'
                return
            
        Match=False
    f.write("Always Valid\n0\n"+eventCode+"\n1")
    f.close()

    with open("RULES.CTL", "r") as f:
        value="#VERSION 3.79 Build 12\n2\n"+str(ClauseCounter+1)+"\n"
        contents = f.readlines()

    contents.insert(0, value)

    with open("RULES.CTL", "w") as f:
        contents = "".join(contents)
        f.write(contents)
        messagebox.showinfo(title='Success', message='Sucess')
        return




def handleSelection(groups,excel,event,value):
    if value==1:
        make_Rules(groups,excel,event)
    else:
        make_Rules2(groups,excel,event)

class NewprojectApp:
    def __init__(self, master):
        var=tk.IntVar()
        # build ui
        self.frame1 = ttk.Frame(master)
        self.text1 = scrolledtext.ScrolledText(self.frame1)
        self.text1.configure(height='10', width='50')
        _text_ = ''''''
        self.text1.insert('0.0', _text_)
        self.text1.grid(column='0', row='1')
        self.text2 = scrolledtext.ScrolledText(self.frame1)
        self.text2.configure(height='10', width='50')
        _text_ = ''''''
        self.text2.insert('0.0', _text_)
        self.text2.grid(column='2', row='1', sticky='ne')
        self.radiobutton1 = ttk.Radiobutton(self.frame1)
        self.radiobutton1.configure(text='Start-end Xsection', variable=var, value=2)
        self.radiobutton1.grid(column='3', row='1')
        self.radiobutton2 = ttk.Radiobutton(self.frame1)
        self.radiobutton2.configure(text='Single Xsection', variable=var, value=1)
        self.radiobutton2.grid(column='3', row='1', sticky='n')
        self.label1 = ttk.Label(self.frame1)
        self.label1.configure(text='Groups')
        self.label1.grid(column='0', row='0')
        self.label2 = ttk.Label(self.frame1)
        self.label2.configure(text='Excel')
        self.label2.grid(column='2', row='0')
        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(text='Event Code')
        self.label3.grid(column='0', row='2', sticky='w')
        self.label4 = ttk.Label(self.frame1)
        self.label4.configure(text='')
        self.label4.grid(column='2', row='2')
        self.button1 = ttk.Button(self.frame1)
        self.button1.configure(text='Create File', command = lambda: handleSelection(self.text1.get("1.0","end-1c"),self.text2.get("1.0","end-1c"),self.entry1.get(),var.get()))
        self.button1.grid(column='3', row='2')
        self.entry1 = ttk.Entry(self.frame1)
        _text_ = ''''''
        self.entry1.delete('0', 'end')
        self.entry1.insert('0', _text_)
        self.entry1.grid(column='0', row='2')
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()




