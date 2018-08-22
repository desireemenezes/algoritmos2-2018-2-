
print("**** CALCULO MEDIA PYTHON SYNTAX ****")

n1 = raw_input("Digite a primeira nota: ")
n2 = raw_input("Digite a segunda nota: ")

media = (float(n1) + float(n2))/2

if media > 6:
    print("PARABENS, VOCE ESTA APROVADO")
else:
    print("VOCE ESTA REPROVADO")

print("MEDIA FINAL: %s" % media)

