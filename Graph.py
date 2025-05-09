
def lifetimGraph():
    global path_length
    propose = 100 - (2 * path_length * 0.3)
    extension = 100 - (1 * path_length * 0.3)
    height = [propose,extension]
    bars = ('Propose Algorithm','Extension Algorithm')
    y_pos = np.arange(len(bars))
    plt.xlabel('Technique Name')
    plt.ylabel('Network Lifetime')         
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.title('Propose VS Extension Network Lifetime Graph')
    plt.show()    

    
    
def energyGraph():
    global path_length 
    height = [(2 * path_length * 0.3),(1 * path_length * 0.3)]
    bars = ('Propose Algorithm','Extension Algorithm')
    y_pos = np.arange(len(bars))
    plt.xlabel('Technique Name')
    plt.ylabel('Energy Consumption')         
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.title('Propose VS Extension Energy Consumption Graph')
    plt.show()         

             

def close():
    global root
    root.destroy()
    
def Main():
    global root
    global tf1
    global text
    global canvas
    global mobile_list
    root = tkinter.Tk()
    root.geometry("1300x1200")
    root.title("An Energy Efficient Routing Protocol Based on Improved Artificial Bee Colony Algorithm for Wireless Sensor Networks")
    root.resizable(True,True)
    font1 = ('times', 12, 'bold')

    canvas = Canvas(root, width = 800, height = 700)
    canvas.pack()

    l1 = Label(root, text='Node ID:')
    l1.config(font=font1)
    l1.place(x=820,y=10)

    mid = []
    for i in range(1,20):
        mid.append(str(i))
    mobile_list = ttk.Combobox(root,values=mid,postcommand=lambda: mobile_list.configure(values=mid))
    mobile_list.place(x=970,y=10)
    mobile_list.current(0)
    mobile_list.config(font=font1)

    createButton = Button(root, text="Generate Network", command=generate)
    createButton.place(x=820,y=60)
    createButton.config(font=font1)

    initButton = Button(root, text="Init Network with CGTABC1 Algorithm Optimizes FCM", command=initializeCGTABC1)
    initButton.place(x=820,y=110)
    initButton.config(font=font1)

    algButton = Button(root, text="Cluster Heads Selection using CGTABC2 Algorithm", command=CGTABC2Algorithm)
    algButton.place(x=820,y=160)
    algButton.config(font=font1)

    graphButton = Button(root, text="Propose & Extension Network Lifetime", command=lifetimGraph)
    graphButton.place(x=820,y=210)
    graphButton.config(font=font1)

    exitButton = Button(root, text="Propose & Extension Energy Consumption", command=energyGraph)
    exitButton.place(x=820,y=260)
    exitButton.config(font=font1)

    text=Text(root,height=20,width=60)
    scroll=Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.place(x=820,y=310)
    
    
    root.mainloop()
