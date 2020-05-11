import tkinter as tk
from PIL import ImageTk,Image
#import matplotlib
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure


root = tk.Tk()
root.title('LOOK AHEAD')
#root.iconbitmap(r'D:\resources\GUI\ada.ico')
#root.geometry("500X500")
root.geometry("720x480")

#creation
#%%


#%%
#selector
f0 = tk.LabelFrame(root,text='Select', padx=5,pady=5, width=11100,height=100)
stks = ['TESLA','RELIANCE','APPLE','SBIN']

sk1 = tk.StringVar()
s1 = tk.OptionMenu(f0,sk1,*stks)

sk2 = tk.StringVar()
s2 = tk.OptionMenu(f0,sk2,*stks)

sk3 = tk.StringVar()
s3 = tk.OptionMenu(f0,sk3,*stks)

sk4 = tk.StringVar()
s4 = tk.OptionMenu(f0,sk4,*stks)

sk5 = tk.StringVar()
s5 = tk.OptionMenu(f0,sk5,*stks)

#separator
sep = tk.Label(root,text='#'*50,padx=5,pady=5)

f1 = tk.LabelFrame(root,text='Stock1', padx=5,pady=5)
f1.config(width=50,column=50)
p11 = tk.Label(f1,text='*')
p21 = tk.Label(f1,text='*')
p31 = tk.Label(f1,text='*')
p41 = tk.Label(f1,text='*')

f2 = tk.LabelFrame(root,text='Stock2',padx=5,pady=5)
p12 = tk.Label(f2,text='*')
p22 = tk.Label(f2,text='*')
p32 = tk.Label(f2,text='*')
p42 = tk.Label(f2,text='*')

f3 = tk.LabelFrame(root,text='Stock3',padx=5,pady=5)
p13 = tk.Label(f3,text='*')
p23 = tk.Label(f3,text='*')
p33 = tk.Label(f3,text='*')
p43 = tk.Label(f3,text='*')

f4 = tk.LabelFrame(root,text='Stock4',padx=5,pady=5)
p14 = tk.Label(f4,text='*')
p24 = tk.Label(f4,text='*')
p34 = tk.Label(f4,text='*')
p44 = tk.Label(f4,text='*')

f5 = tk.LabelFrame(root,text='Stock5',padx=5,pady=5)
p15 = tk.Label(f5,text='*')
p25 = tk.Label(f5,text='*')
p35 = tk.Label(f5,text='*')
p45 = tk.Label(f5,text='*')

f6 = tk.LabelFrame(root,text='Stock6',padx=5,pady=5)
p16 = tk.Label(f6,text='*')
p26 = tk.Label(f6,text='*')
p36 = tk.Label(f6,text='*')
p46 = tk.Label(f6,text='*')



#display
s1.grid(row=0, column=0)
s2.grid(row=0, column=1)
s3.grid(row=0, column=2)
s4.grid(row=0, column=3)
s5.grid(row=0, column=4)

sep.grid(row=1,column=0, columnspan=3)

f0.grid(row=0, column=0, padx=5,pady=5, columnspan=3)
f1.grid(row=2, column=0, padx=5,pady=5)
f2.grid(row=2, column=1, padx=5,pady=5)
f3.grid(row=2, column=2, padx=5,pady=5)
f4.grid(row=3, column=0, padx=5,pady=5)
f5.grid(row=3, column=1, padx=5,pady=5)
f6.grid(row=3, column=2, padx=5,pady=5)


p11.grid(row=0,column=0)
p21.grid(row=0,column=10)
p31.grid(row=10,column=0)
p41.grid(row=10,column=10)
p12.grid(row=0,column=0)
p22.grid(row=0,column=10)
p32.grid(row=10,column=0)
p42.grid(row=10,column=10)
p13.grid(row=0,column=0)
p23.grid(row=0,column=10)
p33.grid(row=10,column=0)
p43.grid(row=10,column=10)
p14.grid(row=0,column=0)
p24.grid(row=0,column=10)
p34.grid(row=10,column=0)
p44.grid(row=10,column=10)
p15.grid(row=0,column=0)
p25.grid(row=0,column=10)
p35.grid(row=10,column=0)
p45.grid(row=10,column=10)
p16.grid(row=0,column=0)
p26.grid(row=0,column=10)
p36.grid(row=10,column=0)
p46.grid(row=10,column=10)







#eventloop
tk.mainloop()