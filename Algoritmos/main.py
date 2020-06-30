import logging

from Algoritmos.ListasLigadas.linked_double_list import LinkedDoubleList
from Algoritmos.Nodos.node import Node


klisostom = 10
deborah = 20
gabi = 30

no_klisostom = Node(klisostom)
no_deborah = Node(deborah)
no_gabi = Node(gabi)

lista = LinkedDoubleList()
lista.list_insert(lista, no_klisostom)
lista.list_insert(lista, no_deborah)
lista.list_insert(lista, no_gabi)

lista.show(lista)
lista.list_delete(lista, no_klisostom)
print()
lista.show(lista)
print(lista.list_search(lista, no_klisostom))