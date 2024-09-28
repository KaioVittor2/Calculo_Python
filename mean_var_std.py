import numpy as np

def calculate(valor):
  
    if len(valor) != 9: # primeiro crio a condição de que a lista precisa ter 9 numeros, se não é erro já.
      raise ValueError("List must contain nine numbers.")
    else:

      # Nesse momento, defino o tamanho que iramos analisar
      num_array = np.array(valor).reshape(3,3)
        
      # Aqui calculamos as médias das colunas, das linhas e geral para a função retornar
      mediaLinha = num_array.mean(axis = 0).tolist() 
      mediaColuna = num_array.mean(axis = 1).tolist()
      mediaGeral = num_array.mean()

      # Aqui calculamos as variâncias das colunas, das linhas e geral para a função retornar
      varianciaLinha = num_array.var(axis = 0).tolist()
      varianciaColuna = num_array.var(axis = 1).tolist()
      varianciaGeral = num_array.var()

      # Aqui calculamos os desvios Padrões das colunas, das linhas e geral para a função retornar
      sdLinha = num_array.std(axis = 0).tolist() 
      sdColuna = num_array.std(axis = 1).tolist()
      sdGeral =  num_array.std()

      # Aqui calculamos os valores Máximo das colunas, das linhas e geral para a função retornar
      maximoLinha = num_array.max(axis = 0).tolist() 
      maximoColuna = num_array.max(axis = 1).tolist() 
      maximoGeral = num_array.max()

      # Aqui calculamos os valores minimos das colunas, das linhas e depois geral para a função retornar
      minimoLinha = num_array.min(axis=0).tolist() 
      minimoColuna = num_array.min(axis=1).tolist() 
      minimoGeral = num_array.min()

      # Aqui calculamos as somas das colunas, das linhas e depois geral para a função retornar
      sumaLinha = num_array.sum(axis=0).tolist()
      sumaColuna = num_array.sum(axis=1).tolist()
      sumaGeral = num_array.sum()

      return {'mean': [mediaLinha, mediaColuna, mediaGeral],
             'variance': [varianciaLinha, varianciaColuna, varianciaGeral],
             'standard deviation': [sdLinha, sdColuna, sdGeral],
             'max' : [maximoLinha, maximoColuna, maximoGeral],
             'min' : [minimoLinha, minimoColuna, minimoGeral],
             'sum' : [sumaLinha, sumaColuna, sumaGeral]}