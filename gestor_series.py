import json
from serie import Serie

class GestorSeries:
    def __init__(self):
        self._series=[] #lista de obj serie

    def agregar(self, serie):
        self._series.append(serie)

    def cargar_desde_json(self, ruta):
        with open(ruta, encoding="utf_8") as f:
            datos=json.load(f)
        for item in datos:
            self.agregar(Serie(item["titulo"], item["creador"], item["año"], item["genero"]))

    def buscar(self, titulo):
        return[s for s in self._series if titulo.lower() in s.titulo.lower()]

    def listar(self):
        return list(self._series)

    def filtrar(self, creador=None, genero=None):
        resultado=self._series
        if creador:
            resultado = [s for s in resultado if s.creador.lower()==creador.lower()]
        if genero:
            resultado = [s for s in resultado if s.genero.lower()==genero.lower()]
        return resultado