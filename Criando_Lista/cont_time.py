from datetime import datetime, timedelta

def calcular_tempo_restante(data_alvo):
    # Obter a data e hora atuais
    data_atual = datetime.now()

    # Converter a string da data alvo para um objeto datetime
    data_alvo = datetime.strptime(data_alvo, "%Y-%m-%d")

    # Calcular a diferença entre a data alvo e a data atual
    diferenca = data_alvo - data_atual

    # Obter a diferença em dias
    diferenca_dias = diferenca.days

    # Imprimir a diferença em dias
    print(f"Tempo restante até {data_alvo}: {diferenca_dias} dias")

# Obter a data alvo do usuário como uma string
data_alvo_input = input("Insira a data alvo (formato: Ano-Mês-Dia): ")

# Chame a função para calcular o tempo restante
calcular_tempo_restante(data_alvo_input)
