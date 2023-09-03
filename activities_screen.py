from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class ActivitiesScreen(Screen):
    def __init__(self, **var_args):
        super(ActivitiesScreen, self).__init__(**var_args)

        app = App.get_running_app()
        self.points_label = Label(text=f"My Current Points: {app.get_points()}", font_size=30)

        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(self.points_label)
        self.add_widget(layout)

