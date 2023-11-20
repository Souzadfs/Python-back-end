horario = input(" Que horas são agora ? ")

if horario.isdigit():
    hra = float(horario)

    if 0 <= hra <= 12:
        print(f"Agora são {hra:.2f} horas, BOM DIA !!!")
    elif 12 < hra < 18:
        print(f"Agora são {hra:.2f} horas, BOA TARDE !!!")
    elif 18 <= hra <= 23:
        print(f"Agora são {hra:.2f} horas, BOA NOITE !!!")

else:
    print(f" Você digitou {horario}.")