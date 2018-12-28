import pygame as pg
import time
from xbee import Xbee

# Global variables
DELAY = 0.01
SRV_IP = '192.168.1.118'
SRV_PT = 9750
K_STATE = tuple([0 for i in range(323)])

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
        global K_STATE
        if event.type == pg.QUIT:
            self._running = False
        if event.type == pg.KEYDOWN:
            k_tmp = pg.key.get_pressed()
            msg = keyUpdate(K_STATE, k_tmp)
            for m in msg: self.s.send(m.encode())
            K_STATE = k_tmp
            #print(msg)
        if event.type == pg.KEYUP:
            k_tmp = pg.key.get_pressed()
            msg = keyUpdate(K_STATE, k_tmp)
            for m in msg: self.s.send(m.encode())
            K_STATE = k_tmp
            #print(msg)

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


def keyUpdate(kold, knew):
    res = []
    for i in range(len(knew)):
        if kold[i] != knew[i]:
            res.append(pg.key.name(i)+['u','d'][knew[i]])
    return res


if __name__ == "__main__":
    
    xb = Xbee(SRV_IP, SRV_PT)
    xb.connect()

    theApp = App(xb.sk)
    theApp.on_execute()

    xb.close()


