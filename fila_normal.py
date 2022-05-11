class FilaNormal:

    def __init__(self):
        self.codigo: int = 0
        self.fila = []
        self.clientes_atendidos = []
        self.senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Atenção Sr(a) {cliente_atual}, Dirija-se ao Caixa {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {'Dia': dia, 'Agencia': agencia, 'Clientes Atendidos': self.clientes_atendidos,
                           'Quantidade de Clientes Atendidos': len(self.clientes_atendidos)}
        return estatistica
