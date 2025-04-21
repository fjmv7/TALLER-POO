

class Publicacion:
    """Clase base que representa una publicación en la biblioteca"""
    
    def __init__(self, titulo: str, autor: str):
        """Constructor de la clase Publicacion"""
        self._titulo = titulo
        self._autor = autor
        self._disponible = True
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def disponible(self) -> bool:
        return self._disponible
    
    def prestar(self) -> str:
        if self._disponible:
            self._disponible = False
            return f"{self._titulo} ha sido prestado"
        return f"{self._titulo} no está disponible"
    
    def devolver(self) -> str:
        if not self._disponible:
            self._disponible = True
            return f"{self._titulo} ha sido devuelto"
        return f"{self._titulo} ya estaba disponible"
    
    def __str__(self) -> str:
        disp = "Disponible" if self._disponible else "Prestado"
        return f"'{self._titulo}' por {self._autor} - {disp}"


class Libro(Publicacion):
    """Clase que representa un libro, hereda de Publicacion"""
    
    def __init__(self, titulo: str, autor: str, isbn: str, paginas: int):
        super().__init__(titulo, autor)  # Solo 2 argumentos para la clase base
        self._isbn = isbn
        self._paginas = paginas
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nISBN: {self._isbn} - {self._paginas} páginas"


class Revista(Publicacion):
    """Clase que representa una revista, hereda de Publicacion"""
    
    def __init__(self, titulo: str, autor: str, issn: str, numero: int):
        super().__init__(titulo, autor)  # Solo 2 argumentos para la clase base
        self._issn = issn
        self._numero = numero
    
    @property
    def issn(self) -> str:
        return self._issn
    
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nISSN: {self._issn} - Número: {self._numero}"