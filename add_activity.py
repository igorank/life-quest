from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


class AddActivityScreen(Screen):
    def __init__(self, **var_args):
        super(AddActivityScreen, self).__init__(**var_args)

        activity_name = Label(text="Activity Name:")
        activity_points = Label(text="Activity Points:")

        self.activity_name_input = TextInput(multiline=False)
        self.activity_points_input = TextInput(multiline=False)

        submit_button = Button(text="Submit", on_press=self.on_submit, size_hint_y=None, height=100)
        back_button = Button(text="Back", on_press=self.goto_activities, size_hint_y=None, height=100)

        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(activity_name)
        layout.add_widget(self.activity_name_input)
        layout.add_widget(activity_points)
        layout.add_widget(self.activity_points_input)
        layout.add_widget(submit_button)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def on_submit(self, instance):
        app = App.get_running_app()

        existing_activities = app.store.get("activities")

        exists = any(activity['name'] == self.activity_name_input.text for activity in existing_activities)

        if exists:  # already exist
            self.manager.current = 'activities'
        else:
            try:
                activity_dict = {'name': self.activity_name_input.text,
                                 'points': int(self.activity_points_input.text), 'count': 0}
            except ValueError:
                pass    # invalid activity_points_input
            else:
                existing_activities.append(activity_dict)
                app.store.put_list('activities', existing_activities)
                self.manager.current = 'activities'

    def goto_activities(self, instance):
        self.manager.current = 'activities'
