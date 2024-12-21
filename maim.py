from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instrukshuns import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits  #тут треба поміняти назву файлу на ту, яка в тебе
from rufyear import test                                                             #тут треба поміняти назву файлу на ту, яка в тебе
from sekonds import Seconds                                                          #тут треба поміняти назву файлу на ту, яка в тебе
Window.clearcolor = (0.7,0.4,0,0.34)
batooncolor = (0.9,0.4,0,1)
age = 7
name = ""
p1, p2, p3 = 0, 0, 0

# повертає число або False, якщо рядок не конвертується
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

#Клас для конструювання першого вікна (з інструкцією та введенням імені та віку користувача)
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text="Введіть ім'я:", halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Введіть вік:', halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = batooncolor
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    #метод, який спрацьовує при натисканні на кнопку "Почати"
    def next(self):
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'


#Клас для конструювання другого вікна (тут міряємо пульс перший раз)         
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
    
        instr = Label(text=txt_test1)
 
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        lbl_result = Label(text='Введіть результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)

        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        self.btn = Button(text='Почати', size_hint=(0.3, 0.4), pos_hint={'center_x': 0.5})
        self.btn.background_color = batooncolor
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    #метод, який спрацьовує коли секундомір завершує роботу
    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'

    #метод, який спрацьовує при натисканні на кнопку 
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'


#Клас для конструювання третього вікна (тут робимо присідання)    
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text='Продовжити', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = batooncolor
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    
    #метод, який спрацьовує при натисканні на кнопку 
    def next(self):
        self.manager.current = 'pulse2'
  

#Клас для конструювання четвертого вікна (тут міряємо пульс другий раз)  
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False

        self.stage = 0
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        self.lbl1 = Label(text='Рахуйте пульс')

        lbl_result1 = Label(text='Результат:', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        lbl_result2 = Label(text='Результат після відпочинку:', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        self.btn = Button(text='Почати', size_hint=(0.3, 0.5), pos_hint={'center_x': 0.5})
        self.btn.background_color = batooncolor
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    #метод, який спрацьовує коли секундомір завершує роботу
    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                # закінчили перший підрахунок, відпочиваємо
                self.stage = 1
                self.lbl1.text = 'Відпочивайте'
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                # закінчили відпочинок, вважаємо
                self.stage = 2
                self.lbl1.text='Рахуйте пульс'
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершити'
                self.next_screen = True

    #метод, який спрацьовує при натисканні на кнопку  
    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = 'result'


#Клас для конструювання п'ятого вікна (тут показуємо результат)  
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text = '')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


#Клас для конструювання мобільного додатку з 4-ма екранами
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm
    
app = HeartCheck()
app.run()

