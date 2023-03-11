# Para resolver esse problema, precisamos entender que a distância total entre as cidades de Ribeirão Preto e Franca é de 100 km, e que o carro e o caminhão se movem em direções opostas.
# Sabendo que a velocidade do carro é de 110 km/h, podemos calcular o tempo que ele levará para percorrer a distância de 100 km:
# Já para o caminhão, sabemos que ele possui uma velocidade de 80 km/h, mas ele leva 5 minutos (ou 0,0833 horas) a mais para passar em cada pedágio. Como há dois pedágios na rodovia, precisamos adicionar esse tempo ao tempo total do caminhão
# Com esses valores em mãos, podemos calcular a distância que cada veículo percorre até se encontrarem
# Aqui, podemos ver que o carro percorreu exatamente a distância entre as cidades, enquanto o caminhão percorreu uma distância maior. Isso significa que o carro estará mais próximo de Ribeirão Preto do que o caminhão quando eles se encontrarem. Portanto, a resposta correta é "O carro estará mais próximo de Ribeirão Preto."

# Distância entre as cidades (em km)
distancia = 100

# Velocidade do carro (em km/h)
velocidade_carro = 110

# Velocidade do caminhão (em km/h)
velocidade_caminhao = 80

# Tempo que o caminhão gasta para passar em cada pedágio (em horas)
tempo_pedagio_caminhao = 5/60

# Tempo que o carro gasta para percorrer a distância entre as cidades (em horas)
tempo_carro = distancia / velocidade_carro

# Tempo que o caminhão gasta para percorrer a distância entre as cidades (em horas)
tempo_caminhao = distancia / velocidade_caminhao + tempo_pedagio_caminhao * 2

# Distância que cada veículo percorre até o encontro (em km)
distancia_carro = velocidade_carro * tempo_carro
distancia_caminhao = velocidade_caminhao * tempo_caminhao

# Verifica qual veículo está mais próximo de Ribeirão Preto
if distancia_carro < distancia_caminhao:
    print("O carro estará mais próximo de Ribeirão Preto.")
else:
    print("O caminhão estará mais próximo de Ribeirão Preto.")


