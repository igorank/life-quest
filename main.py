import logitClasses

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView


class LabelDataItem(Label):
    pass


class MainScreen(RecycleView):

    def __init__(self, **var_args):
        super(MainScreen, self).__init__(**var_args)
        # self.cols = 2
        # self.add_widget(Label(text='My Current Points:'))
        activities_list = logitClasses.activities_get()
        print(activities_list)
        self.data = [{'text': str(act.Activity)} for act in activities_list]


# the Base Class of our Kivy App
class MyApp(App):
    def build(self):
        self.title = 'LifeQuest'
        Window.size = (1920, 1200)
        return MainScreen()


if __name__ == '__main__':
    Builder.load_file('main.kv')  # Load the .kv file
    MyApp().run()
