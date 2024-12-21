from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    def __init__(self, total, **kwargs):
        self.carent = 0
        self.total = total
        mytext = "залишилось присідань:" + str(self.total)
        super().__init__(text = mytext,**kwargs)

    def next(self, *args):
        self.carent += 1
        sits = self.total - self.carent
        mytext = "залишилось присідань:" + str(sits)
        self.text = mytext