
from pathlib import Path
import shutil

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class CopierApp(App):
    def build(self):
        self.title = "Temp Copier"
        root = BoxLayout(
            orientation="vertical",
            padding=18,
            spacing=12
        )

        root.add_widget(Label(
            text="TEMP COPIER",
            font_size=24,
            size_hint_y=None,
            height=55
        ))

        root.add_widget(Label(
            text="Source file path:"
        ))
        self.source = TextInput(
            hint_text="/path/to/file.txt",
            multiline=False,
            size_hint_y=None,
            height=48
        )
        root.add_widget(self.source)

        root.add_widget(Label(
            text="Destination file path:"
        ))
        self.destination = TextInput(
            hint_text="/path/to/copy.txt",
            multiline=False,
            size_hint_y=None,
            height=48
        )
        root.add_widget(self.destination)

        copy_button = Button(
            text="COPY FILE",
            size_hint_y=None,
            height=52
        )
        copy_button.bind(on_press=self.copy_file)
        root.add_widget(copy_button)

        self.status = Label(
            text="Ready",
            size_hint_y=None,
            height=60
        )
        root.add_widget(self.status)

        return root

    def copy_file(self, _button):
        source = Path(self.source.text.strip())
        destination = Path(self.destination.text.strip())

        try:
            if not source.is_file():
                raise FileNotFoundError(
                    "Source file was not found."
                )

            if source.resolve() == destination.resolve():
                raise ValueError(
                    "Source and destination must differ."
                )

            destination.parent.mkdir(
                parents=True,
                exist_ok=True
            )
            shutil.copy2(source, destination)

            self.status.text = "Copy completed."
        except Exception as error:
            self.status.text = f"Error: {error}"


if __name__ == "__main__":
    CopierApp().run()
      
