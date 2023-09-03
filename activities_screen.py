from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button


class Activity:
    def __init__(self, activity, points_gain, count=0):
        self.activity = activity
        self.points = points_gain
        self.count = count


class ActivitiesViewButton(RecycleDataViewBehavior, Button):
    def __init__(self, **kwargs):
        super(ActivitiesViewButton, self).__init__(**kwargs)
        self.data = kwargs.get('data', {})

    def refresh_view_attrs(self, rv, index, data):
        self.text = data['text']
        self.data = data
        return super(ActivitiesViewButton, self).refresh_view_attrs(rv, index, data)

    def on_press(self):
        # Вызывайте нужное вам действие при нажатии на кнопку
        activity_data = self.data  # Здесь можно получить данные элемента
        print(f"Button pressed for activity: {activity_data['text']}")


class ActivitiesView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'text': f'Item {i}'} for i in range(20)]


class ActivitiesScreen(Screen):
    def __init__(self, **var_args):
        super(ActivitiesScreen, self).__init__(**var_args)

        app = App.get_running_app()
        self.points_label = Label(text=f"My Current Points: {app.get_points()}", font_size=30)

        layout = BoxLayout(orientation='vertical', spacing=10)
        # layout.add_widget(self.points_label)

        rv = ActivitiesView()
        layout.add_widget(rv)

        self.add_widget(layout)
