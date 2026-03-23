[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
# Calculadora
Sistema simples de calculadora usando TCP em Python.

Arquivos:
- Server.py – servidor que faz os cálculos
- Client.py – cliente que envia números e operação
- constCS.py – define HOST e PORT

Como usar:

1. Rodar o servidor na máquina:
modifique o constCS.py do servidor para ter HOST = '0.0.0.0'
python3 Server.py

3. Rodar o cliente na outra máquina:
modifique o constCS.py do cliente para ter HOST = (IP do servidor)
python3 Client.py

5. No cliente, informar os números e operação. Exemplo de entrada:
Enter first number: 10
Enter second number: 5
Operation (0=sum, 1=sub, 2=mult, 3=div): 0

6. Saída esperada:
Result: 15
Time taken: 0.000123 seconds

7. Outras operações:
10 5 1 → Result: 5       (subtração)
10 5 2 → Result: 50      (multiplicação)
10 5 3 → Result: 2       (divisão)
10 0 3 → Result: Error: division by zero
