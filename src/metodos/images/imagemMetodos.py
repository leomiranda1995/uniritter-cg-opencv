import numpy as np
import cv2

def selecionaImagem():
  # DESENVOLVER O INPUT DE IMAGEM PARA QUE O USUÁRIO SELECIONE
  imagem = cv2.imread("arquivos/bulbasaur.png")
  return imagem

def showImagem(imagem):
  from matplotlib import pyplot as plt
  imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
  plt.imshow(imagem)
  plt.show()

def gravaImagem(imagem):
  # DESENVOLVER A FUNCIONALIDADE DE PEGAR O NOME DO ARQUIVO ORIGINAL E GRAVAR COM ALGUM IDENTIFICADOR
  # DESENVOLVER A FUNCIONALIDADE DE PRINTAR UMA MENSAGEM COM O NOME  E LOCAL DO ARQUIVO GRAVADO
  cv2.imwrite("arquivos/bulbasaur_modificado.png", imagem)