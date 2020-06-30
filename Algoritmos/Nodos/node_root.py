from typing import TypeVar, Generic

from Algoritmos.Nodos.node import Node

T = TypeVar('T')


class NodeRoot(Node(Generic[T])):

    def __init__(self, key: T, prev=None, next=None, parent=None) -> None:
        super(NodeRoot, self).__init__(key, next, prev)
        self.__parent = parent

    def get_parent(self) -> T:
        return self.__parent

    def set_parent(self, parent) -> None:
        self.__parent = parent
