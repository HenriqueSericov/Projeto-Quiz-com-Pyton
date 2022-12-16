print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? (S/N) ")
print(answer_user)

if answer_user != "S":
    quit()

score = 0


print("Começando.....")
print("Quem desenvolveu o jogo Gta? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Quem é o protagonista do jogo GTA San Andreas  \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl jaqueline \n (D) Carlos Jonhson \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
print(f"quiz acabou..... Pontuação: {score}/2")