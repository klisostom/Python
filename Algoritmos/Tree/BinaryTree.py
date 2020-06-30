from Algoritmos.Nodos.node_root import NodeRoot

from typing import TypeVar, Generic

T = TypeVar('T')


class BinaryTree(NodeRoot(Generic[T])):

    def __init__(self, key: T, parent: T, left: T, right: T) -> None:
        super(BinaryTree, self).__init__(key, left, right, parent)
        self.__root = parent

    def is_left_empty(self) -> bool:
        return super(BinaryTree, self).get_prev() is None

    def is_right_empty(self) -> bool:
        return super(BinaryTree, self).get_next() is None

    def is_binarytree_empty(self) -> bool:
        return self.__root is None
