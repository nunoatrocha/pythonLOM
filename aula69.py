"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 10
def escopo1():
    global x
    x = 20
    print(x)
    def escopo2():
        global x
        x = 30
        y = 40
        print(x, y)
    escopo2()
    print(x)
    
print(x)
escopo1()
print(x)