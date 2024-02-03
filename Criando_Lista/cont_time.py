from datetime import datetime, timedelta

def calcular_tempo_restante(data_alvo):
   
    data_atual = datetime.now()

    data_alvo = datetime.strptime(data_alvo, "%Y-%m-%d")

    diferenca = data_alvo - data_atual

 
    diferenca_dias = diferenca.days
    print(f"Tempo restante para a viagem até BARRETOS COUNTRY RESORT\n junto com a TROPA\n Denis\n Debora\n Lara\n Analice\n Alexandre\n Cibele\n Heloisa\n Arthur\n {diferenca_dias} dias")


data_alvo_input = input("Insira a data alvo (formato: Ano-Mês-Dia): ")

calcular_tempo_restante(data_alvo_input)
