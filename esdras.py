from kivy.uix.filechooser import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360,600)

Builder.load_file('esdras.kv')

class CalculadoraLayout(Screen):
    def add_to_expression(self, value):
        display = self.ids.display
        display.text += value

    def remover_char(self):
        display = self.ids.display
        display.text = display.text[:-1]

    def clear_expression(self):
        display = self.ids.display
        display.text = ''

    def calculate_result(self):
        display = self.ids.display
        try:
            result = str(eval(display.text))
            display.text = result
        except Exception:
            display.text = 'Erro'

class CalculadoraApp(App):
    def build(self):
        return CalculadoraLayout()

if __name__ == '__main__':
    CalculadoraApp().run()
