import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lendo diretamente do CSV
df = pd.read_csv('./HOME_5G.csv')  # Substitua 'seuarquivo.csv' pelo caminho do seu arquivo CSV

# Calculando média e desvio padrão
media = np.mean(df['Response Time (seconds)'])
desvio_padrao = np.std(df['Response Time (seconds)'])

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Request'], df['Response Time (seconds)'], marker='o', label='Tempo de resposta')
plt.axhline(y=media, color='r', linestyle='--', label='Média')
plt.axhline(y=desvio_padrao + media, color='g', linestyle='--', label='Média + Desvio Padrão')
plt.axhline(y=media - desvio_padrao, color='g', linestyle='--', label='Média - Desvio Padrão')

# Adicionando rótulos e título
plt.xlabel('Requisição')
plt.ylabel('Tempo de resposta (segundos)')
plt.title('Distribuição do tempo de resposta')
plt.legend()

# Exibindo o gráfico
plt.show()