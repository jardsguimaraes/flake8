from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_normal = FilaNormal()
fila_prioritaria = FilaPrioritaria()

fila_normal.atualiza_fila()
fila_normal.atualiza_fila()
fila_normal.atualiza_fila()
fila_normal.atualiza_fila()

print(fila_normal.chama_cliente(1))
print(fila_normal.chama_cliente(10))
print(fila_normal.chama_cliente(11))
print('---------------------------')

fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()

print(fila_prioritaria.chama_cliente(1))
print(fila_prioritaria.chama_cliente(5))
print(fila_prioritaria.chama_cliente(8))
