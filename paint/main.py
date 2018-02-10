#standard
from random import random 

#kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        '''touch object contains the mouse information like:
            <MouseMotionEvent spos=(0.60875, 0.44666666666666666) pos=(487.0, 268.0)>
        
        Widget axis is centered at lower left corner
        '''
        if touch.button == 'middle':
            self.canvas.clear()
            return 
            
        with self.canvas:
            Color(random(), 1., 1., mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            '''touch.ud is a python dictionary attached to the touch object which can be 
            used to store user data, which seams like can be used between multiple calls'''
            touch.ud['line'] = Line(points=(touch.x, touch.y))
    
    def on_touch_move(self, touch):
        '''touch_move is not same as mouse move, this is called only if user is actually 
        touching (i.e. click on left button) while moving
        
        It will be called if any of the mouse buttons are down (in case of right and middle click
        we even get some extra marker'''
        try: touch.ud['line'].points += [touch.x, touch.y]
        except (KeyError): pass 

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()
        


if __name__ == '__main__':
    MyPaintApp().run()
