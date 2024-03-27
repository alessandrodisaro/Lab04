import flet as ft

import controller


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.lvOut = None
        self._lingua = None
        self._ricerca = None
        self._button = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        # dropdown della selezione lingua
        self._lingua = ft.Dropdown(
            label="Select a language",
            width=300,
            options=[
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Spanish")
            ], on_change=self.check_lingua_corretta
        )
        # dropdown dei tipi di ricerca
        self._ricerca = ft.Dropdown(
            label="Search mode",
            width=300,
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic")
            ], on_change=self.check_ricerca_corretta
        )
        # text field
        self._testo = ft.TextField(label="Add your text here", on_submit=self.check_testo)
        # bottone tranlsate
        self._button = ft.ElevatedButton(text="Translate", on_click=self.__controller.handleSpellCheck)
        #listView di output
        self.lvOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        # righe
        row1 = ft.Row([self._lingua])
        row2 = ft.Row([self._ricerca, self._testo, self._button])  # che sono il campo della tipo di ricerca, campo di inserimento testo e il bottone
        row3 = ft.Row([self.lvOut])
        # update della pagina
        self.page.add(row1, row2, row3)
        # l' update qua sotto era qua nel template iniziale
        # self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def check_lingua_corretta(self, e):
        if self._lingua.value == "Italian" or self._lingua.value == "English" or self._lingua.value == "Spanish":
            txtOut = ft.Text(f"{self._lingua.value} was selected")
            #self.lvOut.controls.clear()
            self.lvOut.controls.append(txtOut)
            self.page.update()
        else:
            txtOut = ft.Text("Language selected is not supported")
            #self.lvOut.controls.clear()
            self.lvOut.controls.append(txtOut)
            self.page.update()

    def check_ricerca_corretta(self, e):
        if self._ricerca.value == "Default" or self._ricerca.value == "Linear" or self._ricerca.value == "Dichotomic":
            txtOut = ft.Text(f"{self._ricerca.value} was selected")
            #self.lvOut.controls.clear()
            self.lvOut.controls.append(txtOut)
            self.page.update()
        else:
            txtOut = ft.Text("Language selected is not supported")
            #self.lvOut.controls.clear()
            self.lvOut.controls.append(txtOut)
            self.page.update()

    def check_testo(self, e):
        if self._testo.value != "":
            txtOut = ft.Text("Text selected")
            self.lvOut.controls.append(txtOut)
            self.lvOut.update()
        else:
            txtOut = ft.Text("No text was inserted")
            self.lvOut.controls.append(txtOut)
            self.lvOut.update()

