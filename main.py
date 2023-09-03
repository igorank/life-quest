from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.storage.jsonstore import JsonStore

from activities_screen import ActivitiesScreen
from add_activity import AddActivityScreen


class MainScreen(Screen):

    def __init__(self, **var_args):
        super(MainScreen, self).__init__(**var_args)

        app = App.get_running_app()
        self.points = app.get_points()

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
        app = App.get_running_app()
        app.store.put('points', value=self.points)
        self.manager.current = 'activities'

    def goto_rewards(self, instance):
        pass

    def goto_inventory(self, instance):
        pass

    @staticmethod
    def quit_app(instance):
        App.get_running_app().stop()

    def on_leave(self, *args):
        app = App.get_running_app()
        app.store.put('points', value=self.points)


# the Base Class of our Kivy App
class MyApp(App):
    def __init__(self):
        super().__init__()
        self.store = JsonStore('data.json')

    def get_points(self) -> int:
        if 'points' in self.store:
            return self.store.get('points')['value']
        else:
            return 0

    def build(self):
        self.title = 'LifeQuest'
        Window.size = (1920, 1200)
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(ActivitiesScreen(name='activities'))
        screen_manager.add_widget(AddActivityScreen(name='add_activity'))
        return screen_manager


if __name__ == '__main__':
    Builder.load_file('settings.kv')  # Load the .kv file
    MyApp().run()
