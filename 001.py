# Vamos primeiro criar um arquivo e escrever o primeiro dia da semana
file = open("days.txt", "w")
file.write("Sunday\n")
file.close()

# Agora vamos adicionar os outros dias da semana
file = open("days.txt", "a")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in days:
    if i == days[-1]:
        file.write(i)
    else:
        file.write(i + "\n")
file.close()

# Por fim, vamos ler, e imprimir, linha a linha o nosso arquivo
file = open("days.txt", "r")
while True:
    string = file.readline()
    if string[-1] == "\n":
        print(string[:-1])
    else:
        print(string)
        break