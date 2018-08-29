
x = input("Entre com a posicao do ponto x: ")
y = input("Entre com a posicao do ponto y: ")
x0 = input("Entre com a posicao do ponto x0: ")
y0 = input("Entre com a posicao do ponto y0: ")
x1 = input("Entre com a posicao do ponto x1: ")
y1 = input("Entre com a posicao do ponto y1: ")

 
def retangulo(x, y, x0, y0, x1, y1):
    if (((x >= x0) and (x <= x1)) and ((y >= y0) and (y <= y1)))
        r = 1
    else:
        r = 0
    return r

resposta = retangulo(x0, y0, x1, y1, x, y)
print("A resposta é: %d", resposta)

