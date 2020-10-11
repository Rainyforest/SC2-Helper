from tkinter import *
from tkinter.filedialog import askopenfilename
import replay
from replay import Replay
import time
import utils

class UIMain:
    preread_offset = 3

    def __init__(self):
        self.root = Tk()
        self.init_window()
        self.replay = None
        self.broadcasting = False
        self.start_time = None
        self.player = None
        self.build_iter_idx = 0
        self.file_path = "" 
        self.my_label = Label(self.root,text="Select A Replay")
        self.my_label.pack()
        self.entry = Entry(self.root, width = 50, borderwidth = 2)
        self.entry.pack()
        self.btn_browse = Button(self.root, text = "Browse", command = lambda: self.btn_browse_on_click())
        self.btn_browse.pack()
        self.btn_play = Button(self.root, text = "Start", command = lambda: self.btn_play_on_click())
        self.btn_play.pack()
        self.btn_stop = Button(self.root, text = "Stop", command = lambda: self.btn_stop_on_click())
        self.btn_stop.pack()
        self.root.mainloop()

    def init_window(self):
        self.root.title("SC2 Helper")
        # set window size
        self.root.geometry("500x300")
        self.center_screen()

    def center_screen(self):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win = self.root
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def btn_play_on_click(self):
        self.replay = Replay(self.file_path)
        self.broadcast(0)

    def btn_stop_on_click(self):
        self.broadcasting = False


    def btn_browse_on_click(self):
        self.file_path = self.file_dialog()
        self.entry.insert(0,self.file_path)

    def file_dialog(self):
        self.root.withdraw() # we don't want a full GUI, so keep the root window from appearing
        file_path = askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("SC2 Replay Files","*.SC2Replay"),("all files","*.*")))
        self.root.deiconify()
        print(file_path)
        return file_path

    def broadcast(self,player_idx):
        players = self.replay.players
        if player_idx not in range(0,len(players)):
            return
        self.player = players[player_idx]
        self.start_time = time.time()
        self.broadcasting = True
        self.build_iter_idx = 0
        self.loop()

    def loop(self):
        if self.broadcasting:
            self.root.after(300, lambda: self.loop())
            if self.build_iter_idx < len(self.player.build_order):
                now = time.time()
                curr_build = self.player.build_order[self.build_iter_idx]
                if now >= self.start_time + float(curr_build.time_in_seconds) * (6/5) - self.preread_offset:
                    utils.announce_build(curr_build)
                    self.build_iter_idx += 1
            else: self.broadcasting = False
        else:
            pass
def main():
    UI = UIMain()
if __name__=="__main__":
    main()