# DESAFIO
# Exercício Classes abstratas, curso Mestre Pythonista, instrutor Jhonatan de Souza.

''' Crie uma classe abstrata chamada Monitor, que irá ter dois métodos abstratos:
aumentar_claridade e reduzir_claridade.
Os métodos irão receber um número que representam o quanto de claridade deve ser aumentado
ou diminuído ao chamar eles.
Após ter criado a classe abstrata, crie uma nova classe chamada de MonitorFullHD e coloque a implementação
dos métodos aumentar_claridade dentro deles. '''
from abc import ABC, abstractmethod


class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, valor):
        pass

    @abstractmethod
    def reduzir_claridade(self, valor):
        pass


class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando a claridade em {valor} pontos')

    def reduzir_claridade(self, valor):
        print(f'Reduzindo a claridade em {valor} pontos')


monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(5)
