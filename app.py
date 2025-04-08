import pandas as pd
import matplotlib.pyplot as plt

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja1 = pd.read_csv(url1)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)


# Faturamento das lojas
faturamento_lojas = []
lojas = []

for i, loja in enumerate([loja1, loja2, loja3, loja4], start=1):
    nome_loja = f'Loja {i}'
    loja['Faturamento'] = loja['Preço'] + loja['Frete']
    faturamento_loja = loja['Faturamento'].sum()

    print(f'Faturamento {nome_loja}: R${faturamento_loja:.2f}')

    lojas.append(nome_loja)
    faturamento_lojas.append(faturamento_loja)

# Gráfico coluna - faturamento
plt.figure(figsize=(10, 6))
plt.bar(lojas, faturamento_lojas, color='skyblue')
plt.title('Faturamento por Loja')
plt.xlabel('Lojas')
plt.ylabel('Faturamento (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Exibir o valor em cima de cada barra
for i, valor in enumerate(faturamento_lojas):
    plt.text(i, valor + 100, f'R${valor:.2f}', ha='center', fontsize=10)
plt.show()


# vendas or categoria
vendas_categorias = {}
for i, loja in enumerate([loja1, loja2, loja3, loja4], start=1):
    vendas_categoria = loja['Categoria do Produto'].value_counts()
    
    vendas_categorias[f'Loja {i}'] = vendas_categoria.to_dict()


# Pegarvas categorias existentes
categorias = set()
for categorias_loja in vendas_categorias.values():
    categorias.update(categorias_loja.keys())

categorias = list(categorias)
# Gráfico Linear - Vendas por Categoria
plt.figure(figsize=(10, 6))
for loja, vendas in vendas_categorias.items():
    vendas_por_categoria = [vendas.get(categoria, 0) for categoria in categorias]
    plt.plot(categorias, vendas_por_categoria, marker='o', label=loja)

plt.xlabel('Categorias')
plt.ylabel('Quantidade Vendida')
plt.title('Vendas por Categoria em Cada Loja')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Média das avaliações
lojas = [f'Loja {i}' for i in range(1, 5)]
medias = [loja['Avaliação da compra'].mean() for loja in [loja1, loja2, loja3, loja4]]

# Gráfico coluna - Média das avaliações
plt.figure(figsize=(10, 6))
plt.bar(lojas, medias, color='skyblue')
plt.xlabel('Lojas')
plt.ylabel('Média das Avaliações')
plt.title('Média de Avaliações das Compras por Loja')
plt.ylim(0, 5)  # considerando que a avaliação vai de 0 a 5
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, media in enumerate(medias):
    plt.text(i, media + 0.05, f'{media:.2f}', ha='center')

plt.show()


# Mais e menos vendidos por loja
lojas = []
mais_vendidos = []
menos_vendidos = []
qtd_vendas_mais = []
qtd_vendas_menos = []
produtos_vendas = []

for i, loja in enumerate([loja1, loja2, loja3, loja4], start=1):
    nome_loja = f'Loja {i}'
    mais_vendido = loja['Produto'].value_counts().idxmax()
    menos_vendido = loja['Produto'].value_counts().idxmin()
    qtd_mais = loja['Produto'].value_counts().max()
    qtd_menos = loja['Produto'].value_counts().min()

    produtos_vendas.append({
        nome_loja: {
            'Mais vendido': mais_vendido,
            'Menos vendido': menos_vendido
        }
    })

    lojas.append(nome_loja)
    mais_vendidos.append(mais_vendido)
    menos_vendidos.append(menos_vendido)
    qtd_vendas_mais.append(qtd_mais)
    qtd_vendas_menos.append(qtd_menos)

# Gráfico de pizza - Mais vendidos
plt.figure(figsize=(8, 8))
plt.pie(qtd_vendas_mais, labels=[f'{loja}\n{produto}\nQtd: {qtd}' for loja, produto, qtd in zip(lojas, mais_vendidos, qtd_vendas_mais)])
plt.title('Produto mais vendido por loja')
plt.show()

# Gráfico de pizza - Menos vendidos
plt.figure(figsize=(8, 8))
plt.pie(qtd_vendas_menos, labels=[f'{loja}\n{produto}\nQtd: {qtd}' for loja, produto, qtd in zip(lojas, menos_vendidos, qtd_vendas_menos)])
plt.title('Produto menos vendido por loja')
plt.show()


# Frete médio por loja
frete_medio_lojas = []
for i, loja in enumerate([loja1, loja2, loja3, loja4], start=1):
    frete_medio = loja['Frete'].mean()
    frete_medio_lojas.append({
        f'Loja {i}': round(float(frete_medio), 2)
    })

print(f'O frete médio por loja é: {frete_medio_lojas}')

# Gráfico de barras - frete médio por loja
lojas = [list(loja.keys())[0] for loja in frete_medio_lojas]
valores = [list(loja.values())[0] for loja in frete_medio_lojas]

plt.figure(figsize=(8,5))
plt.bar(lojas, valores, color='salmon')
plt.title('Frete Médio por Loja')
plt.xlabel('Lojas')
plt.ylabel('Frete Médio (R$)')
plt.show()
