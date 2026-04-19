[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)

# ClientServerBasics (3.0)

## Calculadora Distribuída com Teste de Carga

Sistema cliente-servidor utilizando sockets TCP em Python para execução de operações matemáticas simples, com suporte a múltiplos servidores e geração concorrente de requisições para avaliação de desempenho.

---

## Arquivos

* `server.py` – servidor TCP multithread responsável por processar requisições
* `client.py` – cliente concorrente que gera múltiplas requisições automaticamente
* `constCS.py` – configuração de rede (HOST, PORT e lista de servidores)

---

## Funcionalidades

* Operações suportadas:

  * Soma
  * Subtração
  * Multiplicação
  * Divisão (com tratamento de divisão por zero)

* Servidor:

  * Multithread (uma thread por conexão)
  * Retorna resultado + tempo de processamento

* Cliente:

  * Geração automática de requisições aleatórias
  * Execução concorrente com `ThreadPoolExecutor`
  * Balanceamento simples via escolha aleatória de servidores
  * Coleta de métricas:

    * RTT (tempo de ida e volta)
    * Tempo de processamento
    * Taxa de perda
    * Tempo total

---

## Configuração

### Servidor

No arquivo `constCS.py`, configure:

```python
HOST = "0.0.0.0"
PORT = 5678  # altere para cada instância de servidor
```

Execute:

```bash
python3 server.py
```

Você pode subir múltiplos servidores em portas diferentes.

---

### Cliente

No `constCS.py`, configure a lista de servidores disponíveis:

```python
SERVERS = [
    ("IP_SERVIDOR_1", 5678),
    ("IP_SERVIDOR_2", 5679),
    ("IP_SERVIDOR_3", 5680),
]
```

Execute:

```bash
python3 client.py
```

---

## Execução

O cliente solicitará:

```
Quantas requisições por execução?
```

O sistema realiza:

* 10 execuções (`NUM_RUNS`)
* Cada execução com N requisições concorrentes

---

## Métricas exibidas

Por execução:

* Tempo total
* RTT médio
* Tempo médio de processamento
* Percentual de perda

Exemplo:

```
=== Execução 1/10 ===
Tempo total: 0.8421s
RTT médio: 0.012345s
Processamento médio: 0.000321s
Perda: 2.00%
```

Média final:

```
=== MÉDIA FINAL (10 execuções) ===
Tempo total médio: 0.8012s
RTT médio geral: 0.011876s
Processamento médio geral: 0.000298s
Perda média: 1.75%
```

---

## Formato da requisição

Mensagem enviada ao servidor:

```
<a> <b> <op>
```

Onde:

* `a`, `b` → números reais
* `op`:

  * 0 → soma
  * 1 → subtração
  * 2 → multiplicação
  * 3 → divisão

---

## Formato da resposta

```
<resultado>|<tempo_processamento>
```

Exemplo:

```
15.0|0.000123
```

---

## Observações

* Cliente e servidor utilizam concorrência
* A escolha do servidor é aleatória (load balancing simples)
* Pode ocorrer perda de requisições (timeout)
* Divisão por zero é tratada no servidor
* `MAX_WORKERS` controla o nível de concorrência do cliente
