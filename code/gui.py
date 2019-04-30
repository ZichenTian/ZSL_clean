# -- coding: utf-8 --
try:
    from tkinter import *
except:
    from Tkinter import *

from PIL import Image, ImageTk
from parse_config import parse_config
from list_processor import process_train_list
import os

'''
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidges()

    def createWidges(self):
        self.hellolabel = Label(self, text='Hello, world!')
        self.hellolabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

'''

class Application(Frame):
    def __init__(self, config_dict,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.image_list, self.label_list = process_train_list(config_dict)
        self.index = 0
        self.pic_rootpath = config_dict['pic_rootpath']
        self.label_path = config_dict['save_list']
        self.createWidges()
    
    def createWidges(self):
        self.imageLabel = Label(self, image=self.readimg())
        self.imageLabel.pack()
        self.previewButton = Button(self, text='前一张(p)', command=self.preview, bg='white')
        self.previewButton.pack()
        self.nextButton = Button(self, text='后一张(n)', command=self.next, bg='white')
        self.nextButton.pack()
        self.forwardButton = Button(self, text='正视(w)', command=self.forward, bg='white')
        self.forwardButton.pack()
        self.backwardButton = Button(self, text='后视(s)', command=self.backward, bg='white')
        self.backwardButton.pack()
        self.leftButton = Button(self, text='左视(a)', command=self.left, bg='white')
        self.leftButton.pack()
        self.rightButton = Button(self, text='右视(d)', command=self.right, bg='white')
        self.rightButton.pack()
        self.flyEntry = Entry(self)
        self.flyEntry.pack()
        self.flyButton = Button(self, text='跳转', command=self.fly, bg='white')
        self.flyButton.pack()
        self.indexLabel = Label(self, text=str(self.index)+'/'+str(len(self.image_list)-1))
        self.indexLabel.pack()
        self.master.bind('n', self.next)
        self.master.bind('p', self.preview)
        self.master.bind('w', self.forward)
        self.master.bind('s', self.backward)
        self.master.bind('a', self.left)
        self.master.bind('d', self.right)
        
    def fly(self, event=None):
        if int(self.flyEntry.get()) >= 0 and int(self.flyEntry.get()) < len(self.image_list):
            self.index = int(self.flyEntry.get())
        self.refresh()

    def readimg(self):
        picname = self.image_list[self.index]
        img = Image.open(picname)
        self.img = ImageTk.PhotoImage(img)
        return self.img

    def save_and_quit(self):
        self.quit()

    def forward(self, event=None):
        self.label_list[self.index] = '1\n'
        with open(self.label_path, 'wb') as f:
            f.writelines(self.label_list)
        self.next()
    
    def backward(self, event=None):
        self.label_list[self.index] = '2\n'
        with open(self.label_path, 'wb') as f:
            f.writelines(self.label_list)
        self.next()

    def left(self, event=None):
        self.label_list[self.index] = '3\n'
        with open(self.label_path, 'wb') as f:
            f.writelines(self.label_list)
        self.next()

    def right(self, event=None):
        self.label_list[self.index] = '4\n'
        with open(self.label_path, 'wb') as f:
            f.writelines(self.label_list)
        self.next()

    def next(self, event=None):
        if self.index >= len(self.image_list):
            return
        self.index += 1
        self.refresh()
    
    def preview(self, event=None):
        if self.index <= 0:
            return
        self.index -= 1
        self.refresh()

    def refresh(self):
        self.imageLabel['image'] = self.readimg()
        self.indexLabel['text'] = str(self.index)+'/'+str(len(self.image_list)-1)
        self.forwardButton['bg'] = 'white'
        self.backwardButton['bg'] = 'white'
        self.leftButton['bg'] = 'white'
        self.rightButton['bg'] = 'white'
        if self.label_list[self.index] == '1\n':
            self.forwardButton['bg'] = 'blue'
        if self.label_list[self.index] == '2\n':
            self.backwardButton['bg'] = 'blue'
        if self.label_list[self.index] == '3\n':
            self.leftButton['bg'] = 'blue'
        if self.label_list[self.index] == '4\n':
            self.rightButton['bg'] = 'blue'

def gui_main():
    config_dict = parse_config('./config.proto')
    app = Application(config_dict)
    app.master.title('Hello, world!')
    app.refresh()
    app.mainloop()

if __name__ == '__main__':
    gui_main()