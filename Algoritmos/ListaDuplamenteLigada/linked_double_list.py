from typing import TypeVar, Generic
from Algoritmos.Nodos.node import Node

T = TypeVar('T')


class LinkedDoubleList(Generic[T]):
    """
    Classe da lista duplamente encadeada
    """

    def __init__(self) -> None:
        self.__head = Node(None)
        self.__tail = Node(None)

    def show(self, lista: T) -> None:
        """
        Mostra todos os valores dos nodos da lista
        """
        x_temp = lista.get_head()

        while x_temp is not None and x_temp.get_next() is not None:
            print(x_temp.get_data())
            x_temp = x_temp.get_next()

    def list_search(self, lista: T, data: Node[T]) -> T:
        """ The procedure LIST-SEARCH(L, k) finds the first element with key k
        in list L by a simple linear search, returning a pointer to this
        element. If no object with key k appears in the list, then the procedure
        returns NIL.
        """
        x_temp = lista.get_head()

        while x_temp is not None and x_temp.get_data() is not data:
            x_temp = x_temp.get_next()

        return x_temp

    def list_insert(self, lista: T, nodo_x: Node[T]) -> None:
        """
        Given an element x whose key attribute has already been set, the
        LIST-INSERT procedure “splices” x onto the front of the linked list.
        """
        nodo_x.set_next(lista.get_head())

        if lista.get_head() is not None:
            lista.get_head().set_prev(nodo_x)

        lista.set_head(nodo_x)
        nodo_x.set_prev(None)

    def list_delete(self, lista: T, nodo_x: Node[T]) -> None:
        """
        The procedure LIST-DELETE removes an element x from a linked list L.
        It must be given a pointer to x, and it then "splices" x out of the list
        by updating pointers. If we wish to delete an element with a given key,
        we must first call LIST-SEARCH to retrieve a pointer to the element.
        """

        if nodo_x.get_prev() is not None:
            nodo_x.get_prev().set_next(nodo_x.get_next())
        else:
            lista.set_head(nodo_x.get_next())
        if nodo_x.get_next() is not None:
            nodo_x.get_next().set_prev(nodo_x.get_prev())

    def get_head(self) -> Node[T]:
        """
        Recupera o cabeçalho
        """
        return self.__head

    def get_tail(self) -> Node[T]:
        """
        Recupera a calda
        """
        return self.__tail

    def set_head(self, novo_head: Node[T]) -> None:
        """
        Atualiza para um novo cabeçalho
        """
        self.__head = novo_head

    def set_tail(self, novo_tail: Node[T]) -> None:
        """
        Atualiza para um novo cabeçalho
        """
        self.__tail = novo_tail
