import logitClasses

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.storage.jsonstore import JsonStore


class LabelDataItem(Label):
    pass


class MainScreen(Screen):

    def __init__(self, **var_args):
        super(MainScreen, self).__init__(**var_args)
        self.store = JsonStore('data.json')

        if 'points' in self.store:
            self.points = self.store.get('points')['value']
        else:
            self.points = 0

        self.points_label = Label(text=f"My Current Points: {self.points}", font_size=30)

        button_activity = Button(
            text='Activity list',
            on_press=self.goto_activities
        )

        button_rewards = Button(
            text='Reward list',
            on_press=self.goto_rewards
        )

        button_inventory = Button(
            text='Inventory list',
            on_press=self.goto_inventory
        )

        button_quit = Button(
            text='Quit',
            on_press=self.quit_app
        )

        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(self.points_label)
        layout.add_widget(button_activity)
        layout.add_widget(button_rewards)
        layout.add_widget(button_inventory)
        layout.add_widget(button_quit)

        self.add_widget(layout)

    def goto_activities(self, instance):
        self.manager.current = 'activities'

    def goto_rewards(self, instance):
        pass

    def goto_inventory(self, instance):
        pass

    @staticmethod
    def quit_app(instance):
        App.get_running_app().stop()

    def on_leave(self, *args):
        self.store.put('points', value=self.points)


class ActivitiesScreen(Screen):
    pass


# the Base Class of our Kivy App
class MyApp(App):
    def build(self):
        self.title = 'LifeQuest'
        Window.size = (1920, 1200)
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(ActivitiesScreen(name='activities'))
        return screen_manager


if __name__ == '__main__':
    Builder.load_file('main.kv')  # Load the .kv file
    MyApp().run()
