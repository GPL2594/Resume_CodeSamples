import sys;from tkinter import * ; from tkinter import filedialog
import tkinter.colorchooser; import tkinter.messagebox; from random import *
from tkinter import ttk; import matplotlib; matplotlib.use('TkAgg'); import matplotlib.dates as md8s
import matplotlib.ticker as mtick; import matplotlib.pyplot as plt; from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler; from matplotlib.figure import Figure; import matplotlib.animation  as animation
import math ; import urllib as url; import json ; import pandas as pd; import numpy as np; import inspect
import os, sys
from PIL import ImageTk 
from PIL import Image


class App(Tk):
	x = {}
	x['height'] = 700; x['width'] = 1400; x['stat'] = 'Everything is working fine'
	x['ver12'] = ('Verdana', 12); x['ver10'] = ('Verdana', 10); x['ver8'] = ('Verdana', 8)

	
	size = 128, 128
	
#	for infile in glob.glob("*.jpg"):
#	    file, ext = os.path.splitext(infile)
#	    im = Image.open(infile)
#	    im.thumbnail(size, Image.ANTIALIAS)
#	    im.save(file + ".thumbnail", "JPEG")
				
	matplotlib.style.use('ggplot')
	def show(frame):
		App.x[frame].tkraise()
		App.x['current_frame'].set(frame)

			
	def switch(button):
		button_1 = App.x[button][0]
		action_1 = App.x[button][1]
		var1 = App.x[button][2]
		button_2 = App.x[button][3]
		action_2 = App.x[button][4]
		var2 = App.x[button][5]
	
		App.x[button][-1].set(button_1)
		App.x[button][1](var1)
		
		App.x[button][0] = button_2
		App.x[button][1] = action_2
		App.x[button][2] = var2
		App.x[button][3] = button_1
		App.x[button][4] = action_1
		App.x[button][5] = var1
	
	def randomXY(file='randomxy.txt', mode='w', length = 1000, xspan=[0,1000], yspan=[0,1000]):
		f = open(file, mode)
		for i in range(length):
			print('{} {}'.format(uniform(xspan[0], xspan[1]), uniform(yspan[0], yspan[1])), file=f)
		f.close()
		
	def write(datum, file='written_data.txt', mode='a'):
		f = open(file, mode)
		if type(datum) is list:
			for i in datum:
				print('{}'.format(datum), file=f)
		elif type(datum) is dict:
			for i in datum.items():
				print('{} {}'.format(list(i)[0], list(i)[1]), file=f)
		else:
			print('{}'.format(datum), file=f)
		f.close()
	
	def animate():
		App.randomXY()
		f, ff= open('randomxy.txt', 'r'), f.read().split(sep='\n')
		f.close()
		for i in ff:
			if len(i.split())==2:
				xx = float(i.split()[0])
				yy = float(i.split()[1])
				x.append(xx)
				y.append(yy)
		App.x['sub_fig'].clear()
		App.x['sub_fig'].plot(x,y)	
		
	def BitCoinTrade(i):
		data_link = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
		data = url.request.urlopen(data_link)
		data = data.readall().decode('utf-8')
		data = json.loads(data)
		data = data['btc_usd']
		data = pd.DataFrame(data)
		buys = data[(data['type']=='bid')]
		sells = data[(data['type']=='ask')]
		buys['date_stamp'] = np.array(buys['timestamp']).astype('datetime64[s]')
		buy_date = (buys['date_stamp']).tolist()
		sells['date_stamp'] = np.array(sells['timestamp']).astype('datetime64[s]')
		sell_date = (sells['date_stamp']).tolist()		
		title = 'Live Bitcoin Trade\nLast Price: '+str(data['price'][1999])
		App.x['sub_fig'].clear()
		App.x['sub_fig'].plot_date(buy_date, buys['price'], '#3366FF', label='Buys')
		App.x['sub_fig'].plot_date(sell_date, sells['price'], '#FF33CC', label='Sells')
		App.x['sub_fig'].set_title(title)
		App.x['sub_fig'].legend(bbox_to_anchor=(0, 1, 1.1, 0.1), loc=3, ncol=2, borderaxespad=0)
	
	def set_dimensions(resolution, height, width):
		App.x['dimensions'] = []
		App.x['dimensions'].append(
		[['resolution_pixel', resolution], ['height_inch', height], ['width_inch', width]]
		) 
		for i in App.x['dimensions'][0]:
			App.setvar(i[0],DoubleVar(),i[1])
		App.x['dimensions'].append(
		[['height_cm', App.x['height_inch'].get() * 2.5],['width_cm', App.x['width_inch'].get() * 2.5],
		['height_pixel', App.x['height_inch'].get() * App.x['resolution_pixel'].get()],
		['width_pixel', App.x['width_inch'].get() * App.x['resolution_pixel'].get()]]
		)
		for i in App.x['dimensions'][1]:
			App.setvar(i[0],DoubleVar(),i[1])

	def setvar(name, kind, value): 
		var = kind 
		var.set(value) 
		App.x[name] = var

	def setmenu(heading, *args):
		if heading in App.x['dropdown_menu']:
			h = App.x['dropdown_menu'][heading][0]
			if args:
				for arg in enumerate(args):
					try:
						h.add_command(label=arg[1][0], command=arg[1][1])
						App.x['dropdown_menu'][heading][1].update({arg[1][0]:arg[1][1]})
					except IndexError:
						cmd = lambda: tkinter.messagebox.showinfo('!','This feature is not Support yet')
						h.add_command(label=arg[1][0], command=cmd)
						App.x['dropdown_menu'][heading][1].update({arg[1][0]:cmd})
			else: return
		else:
			h = Menu(App.x['menu_bar'], tearoff=1)
			App.x['dropdown_menu'].update({heading:(h,{})})
			App.x['menu_bar'].add_cascade(label=heading, menu=h)
			if args:
				for arg in enumerate(args):
					try:
						h.add_command(label=arg[1][0], command=arg[1][1])
						App.x['dropdown_menu'][heading][1].update({arg[1][0]:arg[1][1]})
					except IndexError:
						cmd = lambda: tkinter.messagebox.showinfo('!','This feature is not Support yet')
						h.add_command(label=arg[1][0], command=cmd)
						App.x['dropdown_menu'][heading][1].update({arg[1][0]:cmd})
			else: return
	
	def buttons(spec):
		for i in spec:
			b = ttk.Button(App.x['menu_frame'], text=i[0], textvariable=i[1], command=i[2]).grid(row=i[3], column=i[4], sticky=NSEW)
			App.x['buttons_obj'] = {i[0]:b}
			
	def communicate(in_msg, out_msg, msg_type = 'msg2msg'):
		out_msg.set(in_msg.get())
		if msg_type == 'msg2msg': 
			return out_msg
		elif msg_type == 'msg2win': 
			return tkinter.messagebox.showinfo('!', out_msg.get())
			
	def radiobutton(spec):
		frame = ttk.LabelFrame(App.x['control_frame'], text=spec[0])
		frame.grid(row=spec[1][0], column=spec[1][1], columnspan=2, sticky=NSEW)
		xy = [(x,y) for x in list(range(spec[2][0])) for y in list(range(spec[2][1]))]
		counter = 0
		for i in xy: 
			button = ttk.Radiobutton(frame,text=spec[5][counter][0],variable=spec[3],value=spec[5][counter][1],command=spec[4])
			button.grid(row=i[0],column=i[1],sticky=NSEW)
			counter +=1
	
	def config_position(row_range, column_range):
		for r in range(row_range):
			y = r
			for c in range(column_range):
				x = c
				App.x['position'].update({(x,y):True})
				
			
	def __init__(self, *args, **kwargs):
		Tk.__init__(self,  *args, **kwargs)
		self.configure(bg='#3399FF')
		master_frame = Frame(self); master_frame.pack(side=TOP, fill=BOTH, expand=1)
		master_frame.winfo_toplevel() ; master_frame.rowconfigure(0,weight=1)  
		master_frame.rowconfigure(1,weight=6) ; master_frame.columnconfigure(0,weight=6)  
		master_frame.columnconfigure(1,weight=1) 
		self.wm_title('Giovanni App'); App.x['quit'] = self.destroy
		menubar = Menu(self); self.config(menu=menubar); App.x['menu_bar'] = menubar
		self.spec()
		App.x['master_frame'] = master_frame
		App.x['matplot'] = matplot(App.x['master_frame'])

		App.x['canvas'] = canvas(App.x['master_frame'])

		App.x['menu'] = menu(App.x['master_frame'])

		App.x['control'] = control(App.x['master_frame'])

		App.show(App.x['current_frame'].get())
		self.iconbitmap(r'sexy.ico')
		#self.warn()
		

	def warn(self):
		App.x['question'] = ['Warning!', 'This app is still in development phase. Use it at your own risk! \nClick YES to continue if you agree, NO to quit']
		App.x['response'] = tkinter.messagebox.askquestion(App.x['question'][0], App.x['question'][1])
		if App.x['response']=='no': self.destroy()
		if App.x['response']=='yes': 
			App.x['msg'] = ['Info', 'Great! Let\'s start :-)']
			tkinter.messagebox.showinfo(App.x['msg'][0], App.x['msg'][1])
	def check_empty(location, frame):
		App.x['location']
		
		
	def spec(self):
		App.x['position'] = {}
		App.setvar('current_status', StringVar(), 'No Issues')
		App.setvar('frame_id', StringVar(), 'canvas_frame')
		App.x['frames'] = ['matplot_frame', 'canvas_frame']
		App.setvar('options', StringVar(), 'Option 1')
		App.setvar('current_frame', StringVar(), 'canvas_frame')
		App.setvar('question_response', StringVar(), '')
		App.x['select_view']=['Select View',(0,1),(2,2),App.x['current_frame'],lambda:App.show(App.x['current_frame'].get()),
		[('matplot','matplot_frame'), ('Canvas','canvas_frame'),('simulation','simulation_frame'), ('multiple','page2_frame')]
		]
		App.x['buttons_spec'] = [
		['Import File',filedialog.askopenfile,0,1],
		['Ask question',lambda:tkinter.messagebox.askquestion(App.x['question'][0], App.x['question'][1]),0,2],
		['show Response',lambda:tkinter.messagebox.showinfo(App.x['msg'][0], App.x['msg'][1]),0,5],
		['slider menu','',0,6],['list menu','',0,7],
		['Quit',App.x['quit'],0,9],['Graph',lambda:App.x['draw'](eval(App.x['input'].get())),1,0],
		['Import Data',lambda: App.x['import_data'](link=''),1,1],['Select Color',tkinter.colorchooser.askcolor,1,2],
		['Dropdown Menu','',1,3],['unused','',1,5]		
		]
		App.x['buttons_obj'] = {}
		App.setvar('file', StringVar(), '')
		App.x['dropdown_menu'] = {}
		App.setvar('input', StringVar(), '')
		App.setvar('input', StringVar(), '')



class canvas(App):
	def __init__(self, master_frame):
		self.frame = Frame(master=master_frame); self.frame.grid(row=1, column=0, columnspan=2, sticky=NSEW)
		self.frame.winfo_toplevel(); self.frame.rowconfigure(0,weight=1) ; self.frame.rowconfigure(1,weight=1)          
		self.frame.columnconfigure(0,weight=1) ; self.frame.columnconfigure(1,weight=1)
		App.x['canvas_frame'] = self.frame
		canvas = Canvas(self.frame, width=699, height=300)
		canvas.pack()

		
		
class control(App):
	def __init__(self, master_frame):
		self.frame = Frame(master=master_frame); self.frame.grid(row=0, column=1, sticky=NSEW)
		self.frame.frame_name = 'Menu'; self.frame.winfo_toplevel() ; self.frame.rowconfigure(0,weight=1)  
		self.frame.rowconfigure(1,weight=1)  ; self.frame.columnconfigure(0,weight=1)  
		self.frame.columnconfigure(1,weight=1); App.x['control_frame'] = self.frame
		App.radiobutton(App.x['select_view'])

class menu(App):
	def __init__(self, master_frame):
		self.frame = Frame(master=master_frame, relief=RAISED)
		self.frame.grid(row=0, column=0, sticky=NSEW); self.frame.winfo_toplevel()                
		self.frame.rowconfigure(0,weight=1)  ; self.frame.rowconfigure(1,weight=1)          
		self.frame.columnconfigure(0,weight=1)  ; self.frame.columnconfigure(1,weight=1)
		App.x['menu_frame']  = self.frame; self.btn(); self.menubar() 
		self.frame.configure(bg='#D8E6E6'); self.frame.grid_rowconfigure(0, weight=1) 
		self.frame.grid_rowconfigure(1, weight=1)
		for i in range(15): self.frame.grid_columnconfigure(i, weight=1)

	def btn(self):
		for i in App.x['buttons_spec']: 
			b = ttk.Button(self.frame, text=i[0], command=i[1]).grid(row=i[2], column=i[3], pady=3, padx=3, sticky=NSEW)
			App.x['buttons_obj'].update({i[0]:b})
		ttk.Label(self.frame, text='Adjust Paremeter').grid(row=1, column=7, sticky=NSEW)
		Spinbox(self.frame, from_ = 0, to=150).grid(row=1, column=8, sticky=NSEW)
		ttk.Label(self.frame, text='Enter Data & click Graph').grid(row=1, column=9, sticky=NSEW)
		ttk.Entry(self.frame, textvariable=App.x['input']).grid(row=1, column=10, sticky=NSEW)
		

	def menubar(self):	
		#App.buttons(App.x['buttons_spec'])
		App.setmenu('File', ['Open File'], ['Open Folder'])

class matplot(App):
	def __init__(self, master_frame):
		self.frame = Frame(master=master_frame); self.frame.grid(row=1, column=0, columnspan=2, sticky=NSEW)
		self.frame.winfo_toplevel(); self.frame.rowconfigure(0,weight=1) ; self.frame.rowconfigure(1,weight=1)          
		self.frame.columnconfigure(0,weight=1) ; self.frame.columnconfigure(1,weight=1)
		App.x['matplot_frame']  = self.frame
		App.x['xy']= ([1,5,9,5,7,0,3,9,5,8,9,8,5,9,5], [8,4,9,0,5,8,7,8,5,9,5,9,0,9,1])
		matplotlib.rcParams.update({'font.size': 4})
		fig = Figure(figsize=(9,3.1), dpi=230)
		sub_fig = fig.add_subplot(111)		
		App.x['fig'] = fig
		App.x['sub_fig'] = sub_fig
		self.canvas = FigureCanvasTkAgg(App.x['fig'], master=self.frame)
		self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)
		self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame)
		self.canvas.show()
		self.drw(App.x['xy'])
		self.toolbar.update()
		self.canvas._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=1)
		App.x['draw'] = self.drw
		App.x['import_data'] = self.import_data
		#self.animate()
		#App.x['animate'] = self.animate
		
	def on_key_event(event):
		print('you pressed %s'%event.key)
		key_press_handler(event, canvas, toolbar)
		canvas.mpl_connect('key_press_event', on_key_event)
	def _quit():
		root.quit()
		root.destroy()  # this is necessary on Windows to prevent # Fatal Python Error: PyEval_RestoreThread: NULL tstate
		button = Button(master=root, text='Quit', command=_quit)
		button.pack(side=BOTTOM)
		
	def drw(self, xy):
		xx = xy[0]
		yy = xy[1]
		App.x['sub_fig'].plot(xx, yy)
		self.canvas.show()
		self.toolbar.update()
		
	def animate(self):
		animation.FuncAnimation(App.x['fig'], App.BitCoinTrade, interval=5000)
		self.canvas.show()
		
	def import_data(self, link):
		data_link = link
		data = url.request.urlopen(data_link)
		data = data.readall().decode('utf-8')
		#data = json.loads(data)
		print(data[0])	

myapp = App()
myapp.mainloop()