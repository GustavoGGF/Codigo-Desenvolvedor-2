import json

# Carregar os dados do faturamento a partir de um arquivo JSON
with open("dados.json", "r") as file:
    dados = json.load(file)

# Filtrar os dias com faturamento maior que zero
faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Calcular menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular a média dos dias com faturamento
media_mensal = sum(faturamento) / len(faturamento)

# Contar os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibir os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
