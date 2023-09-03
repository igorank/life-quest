from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button


class Activity:
    def __init__(self, activity, points_gain, count=0):
        self.name = activity
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
        app = App.get_running_app()
        activities = app.store.get("activities")
        self.data = [{'text': i['name']} for i in activities]


class ActivitiesScreen(Screen):
    def __init__(self, **var_args):
        super(ActivitiesScreen, self).__init__(**var_args)

        # app = App.get_running_app()
        add_button = Button(text="Add Activity", on_press=self.goto_add_activity, size_hint_y=None, height=100)
        back_button = Button(text="Back", on_press=self.goto_main, size_hint_y=None, height=100)

        rv = ActivitiesView()

        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(rv)
        layout.add_widget(add_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def goto_add_activity(self, instance):
        self.manager.current = 'add_activity'

    def goto_main(self, instance):
        self.manager.current = 'main'
