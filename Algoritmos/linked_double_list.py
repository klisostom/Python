from typing import TypeVar, Generic

from Algoritmos.node import Node

T = TypeVar('T')


class LinkedDoubleList(Generic[T]):
    """ Classe da lista duplamente encadeada """

    def __init__(self) -> None:
        self.__head = Node(None)
        self.__tail = Node(None)

    def list_search(self, lista: T, data: Node[T]) -> T:
        """ The procedure LIST-SEARCH(L, k) finds the first element with key k
        in list L by a simple linear search,
        returning a pointer to this element. """
        x_temp = lista.get_head()

        while x_temp is not None and x_temp.get_data() is not data:
            x_temp = x_temp.get_next()

        return x_temp

    def list_insert(self, lista: T, nodo_x: Node[T]) -> None:
        nodo_x.set_next(lista.get_head())

        if lista.get_head() is not None:
            lista.get_head().set_prev(nodo_x)

        lista.set_head(nodo_x)
        nodo_x.set_prev(None)

    def get_head(self) -> Node[T]:
        """ Recupera o cabeçalho """
        return self.__head

    def get_tail(self) -> Node[T]:
        """ Recupera a calda """
        return self.__tail

    def set_head(self, novo_head: Node[T]) -> None:
        """ Atualiza para um novo cabeçalho """
        self.__head = novo_head

    def set_tail(self, novo_tail: Node[T]) -> None:
        """ Atualiza para um novo cabeçalho """
        self.__tail = novo_tail
