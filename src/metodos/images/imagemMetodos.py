import numpy as np
import cv2
import os
from tkinter import filedialog

def selecionaImagem():
  # DESENVOLVER O INPUT DE IMAGEM PARA QUE O USUÁRIO SELECIONE
  selecao_imagem = filedialog.askopenfilename(filetypes=[("Arquivos PNG", "*.png"), ("Arquivos JPG", "*.jpg")])
  imagem = cv2.imread(selecao_imagem)
  return imagem

def showImagem(imagem):
  from matplotlib import pyplot as plt
  imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
  plt.imshow(imagem)
  plt.show()

def gravaImagem(imagem):
  os.system("cls")
  print("Informe o nome do novo arquivo:")
  nomeArquivo = input()
  cv2.imwrite("arquivos/" + nomeArquivo + ".png", imagem)