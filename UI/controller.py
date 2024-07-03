import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        sightingList = self._model.listSightings
        self._listShape = self._model.listShapes
        for n in sightingList:
            if n.datetime.year not in self._listYear:
                self._listYear.append(n.datetime.year)

        for a in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(a))

        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        a = self._view.ddyear.value
        s = self._view.ddshape.value

        self._model.buildGraph(s, a)
        self._view.txt_result.controls.append(ft.Text(f"numero di vertici: {self._model.get_num_of_nodes()} numero di archi: {self._model.get_num_of_edges()}"))

        for n in self._model.get_sum_weight_per_node():
            self._view.txt_result.controls.append(ft.Text(f"Nodo {n[0]}, somma pesi su archi = {n[1]}"))

        self._view.update_page()

    def handle_path(self, e):
        pass