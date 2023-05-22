"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 10
def escopo():
    global x
    x = 2
    print(x)
    def escopo2():
        x = 3
        y = 4
        print(x, y)
    escopo2()
    
print(x)
escopo()
print(x)