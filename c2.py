import pygame as pg
import time
import sys
import socket

# Global variables
MSG = []
DELAY = 0.01
SRV_IP = input('Enter the server ip address:')
SRV_PT = 10000
BUF_SZ = 1024

class App:
    def __init__(self, s):
        self.s = s
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640,400
    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._running = True
    def on_event(self, event):
        global MSG
        #print('e')
        if event.type == pg.QUIT:
            self._running = False
        if event.type == pg.KEYDOWN:
            msg = pg.key.name(event.key) + '-on'
            self.s.send(msg.encode())
            #MSG.append(pg.key.name(event.key))
            #print(''.join(MSG))
        if event.type == pg.KEYUP:
            msg = pg.key.name(event.key) + '-off'
            self.s.send(msg.encode())
            #MSG.remove(pg.key.name(event.key))
            #print(''.join(MSG))
    
    def on_loop(self):
        time.sleep(DELAY)
    
    def on_render(self):
        pass
    
    def on_cleanup(self):
        pg.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        # set up pygame settings
        pg.key.set_repeat()
        # game loop
        while self._running:
            # handle events
            for event in pg.event.get():
                self.on_event(event)
            # update game state
            self.on_loop()
            # render or flush outputs
            self.on_render()
        self.on_cleanup()



if __name__ == "__main__":
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SRV_IP, SRV_PT))

    theApp = App(s)
    theApp.on_execute()

    s.close()


