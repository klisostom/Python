from Algoritmos.linked_double_list import LinkedDoubleList
from Algoritmos.node import Node

idade = 31
idade2 = 43
idade3 = 26

no1 = Node[int](idade)
no2 = Node[int](idade2)
no3 = Node[int](idade3)

lista = LinkedDoubleList[int]()
lista.list_insert(lista, no1)
lista.list_insert(lista, no2)
lista.list_insert(lista, no3)

print(
    (lista.list_search(lista, no1.get_data())).get_data()
)