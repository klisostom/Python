from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    """ Classe Node """

    def __init__(self, key: T, next_nodo=None, prev_nodo=None) -> None:
        self.__key = key
        self.__next = next_nodo
        self.__prev = prev_nodo

    def get_next(self) -> T:
        """ Retorna o próximo nodo """

        return self.__next

    def get_prev(self) -> T:
        """ Retorna o nodo anterior """

        return self.__prev

    def set_next(self, novo_next: T) -> None:
        """ Atualiza para um novo next """

        self.__next = novo_next

    def set_prev(self, novo_prev: T) -> None:
        """ Atualiza para um novo prev """

        self.__prev = novo_prev

    def get_key(self) -> T:
        """ Retorna o conteúdo do nodo """

        return self.__key
