from abc import ABC, abstractmethod

class MusicaDAO(ABC):
    @abstractmethod
    def crear_musica(self, musica):
        pass

    @abstractmethod
    def obtener_musica(self, id_musica):
        pass

    @abstractmethod
    def actualizar_musica(self, musica):
        pass

    @abstractmethod
    def eliminar_musica(self, id_musica):
        pass


class UserDao(ABC):
    @abstractmethod
    def login(self, musica):
        pass