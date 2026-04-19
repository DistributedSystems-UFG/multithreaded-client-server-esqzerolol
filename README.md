[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)

# ClientServerBasics (3.0)

## Calculadora Distribuída com Teste de Carga

Sistema cliente-servidor utilizando sockets TCP em Python para execução de operações matemáticas simples, com suporte a múltiplos servidores e geração concorrente de requisições para avaliação de desempenho.

---

## Arquivos

- `server.py` – servidor TCP multithread responsável por processar requisições
- `client.py` – cliente concorrente que gera múltiplas requisições automaticamente
- `constCS.py` – configuração de rede (HOST, PORT e lista de servidores)

---

## Funcionalidades

- Operações suportadas:
  - Soma
  - Subtração
  - Multiplicação
  - Divisão (com tratamento de divisão por zero)

- Servidor:
  - Multithread (uma thread por conexão)
  - Retorna resultado + tempo de processamento

- Cliente:
  - Geração automática de requisições aleatórias
  - Execução concorrente com `ThreadPoolExecutor`
  - Balanceamento simples via escolha aleatória de servidores
  - Coleta de métricas:
    - RTT (tempo de ida e volta)
    - Tempo de processamento
    - Taxa de perda
    - Tempo total

---

## Configuração

### Servidor

No arquivo `constCS.py`, configure:

```python
HOST = "0.0.0.0"
PORT = 5678  # altere para cada instância de servidor
