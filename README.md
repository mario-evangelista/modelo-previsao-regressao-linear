# Modelo Preditivo - Análise de Regressão Linear Simples

Este repositório contém um exemplo simples de análise de regressão linear usando Python. O código Python gera uma amostra aleatória de dados bidimensionais e ajusta um modelo de regressão linear a esses dados.

## Pré-requisitos

Certifique-se de ter o Python instalado no seu sistema. Você pode instalar as dependências necessárias executando:

```
pip install pandas matplotlib scikit-learn
```

## Como usar

Execute o script `regressao_linear.py` para gerar os dados e visualizar o ajuste do modelo.

```bash
python regressao_linear.py
```

Isso irá gerar um gráfico de dispersão dos dados originais e a linha de regressão ajustada.

## Detalhes da Implementação

O código Python utiliza a biblioteca `pandas` para manipulação de dados, `matplotlib` para visualização e `scikit-learn` para ajuste do modelo de regressão linear.

O modelo de regressão linear é ajustado usando a classe `LinearRegression` da `scikit-learn`.

## Exemplo de Saída

Após a execução do script, você verá a saída no console com os coeficientes angular e linear do modelo de regressão linear.

```
Coeficiente Angular: [39.75520706]
Coeficiente Linear: -0.6211736673932448
```

Além disso, um gráfico será exibido mostrando os dados originais, a linha de regressão ajustada e um ponto de exemplo.
<div align="center">
<img src="https://github.com/mario-evangelista/modelo-previsao-regressao-linear/assets/121322767/4d7213aa-6bac-42b1-b200-fc6206f30b5d" width="700px" />
</div>

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de recebimento.

```

Certifique-se de substituir `regressao_linear.py` pelo nome do seu arquivo Python, caso seja diferente.
