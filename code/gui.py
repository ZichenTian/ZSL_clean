# -- coding: utf-8 --
try:
    from tkinter import *
except:
    from Tkinter import *

from PIL import Image, ImageTk
from parse_config import parse_config
from list_processor import *
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
        self.picname_list, self.label_list = process_train_list(config_dict)
        self.label_dict = get_label_dict(config_dict)
        self.index = 0
        self.pic_rootpath = config_dict['pic_rootpath']
        self.zoom_factor = 1
        self.right_list = config_dict['right_list']
        self.wrong_list = config_dict['wrong_list']
        self.createWidges()
    
    def createWidges(self):
        self.labelLabel = Label(self, text=self.label_dict[self.label_list[self.index]])
        self.labelLabel.pack()
        self.imageLabel = Label(self, image=self.readimg())
        self.imageLabel.pack()
        self.previewButton = Button(self, text='前一张(p)', command=self.preview, bg='white')
        self.previewButton.pack()
        self.nextButton = Button(self, text='后一张(n)', command=self.next, bg='white')
        self.nextButton.pack()
        self.rightButton = Button(self, text='标注正确(r)', command=self.right, bg='white')
        self.rightButton.pack()
        self.wrongButton = Button(self, text='标注错误(w)', command=self.wrong, bg='white')
        self.wrongButton.pack()
        self.zoominButton = Button(self, text='放大(i)', command=self.zoom_in, bg='white')
        self.zoominButton.pack()
        self.zoomoutButton = Button(self, text='缩小(o)', command=self.zoom_out, bg='white')
        self.zoomoutButton.pack()
        self.flyEntry = Entry(self)
        self.flyEntry.pack()
        self.flyButton = Button(self, text='跳转', command=self.fly, bg='white')
        self.flyButton.pack()
        self.indexLabel = Label(self, text=str(self.index)+'/'+str(len(self.picname_list)-1))
        self.indexLabel.pack()
        self.master.bind('n', self.next)
        self.master.bind('p', self.preview)
        self.master.bind('r', self.right)
        self.master.bind('w', self.wrong)
        self.master.bind('i', self.zoom_in)
        self.master.bind('o', self.zoom_out)
        
    def fly(self, event=None):
        if int(self.flyEntry.get()) >= 0 and int(self.flyEntry.get()) < len(self.picname_list):
            self.index = int(self.flyEntry.get())
        self.refresh()

    def zoom_in(self, event=None):
        self.zoom_factor += 0.2
        self.refresh()

    def zoom_out(self, event=None):
        self.zoom_factor -= 0.2
        if self.zoom_factor <= 1:
            self.zoom_factor = 1
        self.refresh()

    def readimg(self):
        picname = os.path.join(self.pic_rootpath, self.picname_list[self.index])
        img = Image.open(picname)
        w,h = img.size
        w = int(w*self.zoom_factor)
        h = int(h*self.zoom_factor)
        img = img.resize((w,h))
        self.img = ImageTk.PhotoImage(img)
        return self.img

    def save_and_quit(self):
        self.quit()

    def right(self, event=None):
        if search_picname(self.picname_list[self.index], self.right_list) >= 0:
            pass
        elif search_picname(self.picname_list[self.index], self.wrong_list) >= 0:
            remove_picname(self.picname_list[self.index], self.wrong_list)
            add_picname(self.picname_list[self.index], self.right_list)
        else:
            add_picname(self.picname_list[self.index], self.right_list)
        self.next()

    
    def wrong(self, event=None):
        if search_picname(self.picname_list[self.index], self.right_list) >= 0:
            remove_picname(self.picname_list[self.index], self.right_list)
            add_picname(self.picname_list[self.index], self.wrong_list)
        elif search_picname(self.picname_list[self.index], self.wrong_list) >= 0:
            pass
        else:
            add_picname(self.picname_list[self.index], self.wrong_list)
        self.next()

    def next(self, event=None):
        if self.index >= len(self.picname_list):
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
        self.labelLabel['text'] = self.label_dict[self.label_list[self.index]]
        self.indexLabel['text'] = str(self.index)+'/'+str(len(self.picname_list)-1)
        self.rightButton['bg'] = 'white'
        self.wrongButton['bg'] = 'white'
        if search_picname(self.picname_list[self.index], self.right_list) >= 0:
            self.rightButton['bg'] = 'blue'
        elif search_picname(self.picname_list[self.index], self.wrong_list) >= 0:
            self.wrongButton['bg'] = 'blue'

def gui_main():
    config_dict = parse_config('./config.proto')
    app = Application(config_dict)
    app.master.title('Hello, world!')
    app.refresh()
    app.mainloop()

if __name__ == '__main__':
    gui_main()