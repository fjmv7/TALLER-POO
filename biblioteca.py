class Publicacion:
    """Clase base que representa una publicación en la biblioteca"""
    
    def __init__(self, titulo: str, autor: str, año_publicacion: int):
        """Constructor de la clase Publicacion"""
        self._titulo = titulo  # Atributo encapsulado
        self._autor = autor
        self._año = año_publicacion
        self._disponible = True
    
    @property
    def titulo(self) -> str:
        """Getter para el título"""
        return self._titulo
    
    @property
    def disponible(self) -> bool:
        """Getter para disponibilidad"""
        return self._disponible
    
    def prestar(self) -> str:
        """Método para prestar la publicación"""
        if self._disponible:
            self._disponible = False
            return f"{self._titulo} ha sido prestado"
        return f"{self._titulo} no está disponible"
    
    def devolver(self) -> str:
        """Método para devolver la publicación"""
        if not self._disponible:
            self._disponible = True
            return f"{self._titulo} ha sido devuelto"
        return f"{self._titulo} ya estaba disponible"
    
    def __str__(self) -> str:
        """Método mágico para representación como string"""
        disp = "Disponible" if self._disponible else "Prestado"
        return f"'{self._titulo}' por {self._autor} ({self._año}) - {disp}"


class Libro(Publicacion):
    """Clase que representa un libro, hereda de Publicacion"""
    
    def __init__(self, titulo: str, autor: str, año_publicacion: int, paginas: int, isbn: str):
        """Constructor de la clase Libro - CORREGIDO: 5 parámetros (incluyendo self)"""
        super().__init__(titulo, autor, año_publicacion)
        self._isbn = isbn
        self._paginas = paginas
    
    @property
    def isbn(self) -> str:
        """Getter para ISBN"""
        return self._isbn
    
    def __str__(self) -> str:
        """Método mágico para representación como string"""
        base = super().__str__()
        return f"{base}\nISBN: {self._isbn} - {self._paginas} páginas"


class Revista(Publicacion):
    """Clase que representa una revista, hereda de Publicacion"""
    
    def __init__(self, titulo: str, autor: str, año_publicacion: int, numero: int, issn: str):
        """Constructor de la clase Revista - CORREGIDO: 5 parámetros (incluyendo self)"""
        super().__init__(titulo, autor, año_publicacion)
        self._issn = issn
        self._numero = numero
    
    @property
    def issn(self) -> str:
        """Getter para ISSN"""
        return self._issn
    
    def __str__(self) -> str:
        """Método mágico para representación como string"""
        base = super().__str__()
        return f"{base}\nISSN: {self._issn} - Número: {self._numero}"