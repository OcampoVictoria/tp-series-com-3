class Serie:
    def __init__(self, titulo, creador, año, genero):
        self._titulo=titulo
        self._creador=creador
        self._año=año
        self._genero=genero

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def creador(self):
        return self._creador

    @property
    def año(self):
        return self._año

    @property
    def genero(self):
        return self._genero

    def __repr__(self):
        return f"{self._titulo} ({self._año})-{self._creador}"
