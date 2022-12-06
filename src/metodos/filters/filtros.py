import numpy as np
import cv2
import metodos.images.cores as cores

def desenhoLapis(img, caminhoImagem):
  # Imagem convertida em tons de cinza
  img = cv2.imread(caminhoImagem, cv2.IMREAD_GRAYSCALE)

  # Imagem invertida em tons de cinza para ter o negativo
  img_gray_inv = 255 - img

  # Blur Guassiano aplicado ao negativo.
  img_blur = cv2.GaussianBlur(img_gray_inv, (21,21), 0, 0)

  # Imagem coCombine a imagem em tons de cinza da etapa 1 com o negativo desfocado da etapa 3
  img_blend = cv2.divide(img, 255 - img_blur, scale = 256)
  return img_blend


def sepia(img):
    # Converter para escala de cor cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Dividir a imagem em escala de cinza por 255
    normalized_gray = np.array(gray, np.float32)/255
    #solid color
    # Para cada canal de cor é efetuada uma multiplicação de seus valores
    sepia = np.ones(img.shape)
    sepia[:,:,0] *= 153 #B
    sepia[:,:,1] *= 204 #G
    sepia[:,:,2] *= 255 #R
    #hadamard
    # Do resultado anterior cada canal de cor é multiplicado pelos canais de cores da imagem em escala de cinza dividida
    sepia[:,:,0] *= normalized_gray #B
    sepia[:,:,1] *= normalized_gray #G
    sepia[:,:,2] *= normalized_gray #R
    return np.array(sepia, np.uint8)


def inversaoCores(img):
  altura, largura, canaisDeCor = img.shape

  for y in range(0, altura):
    for x in range(0, largura):
      azul, verde, vermelho = cores.getColor(img, x, y)
      img = cores.setColor(img, x, y, vermelho, azul, verde)
  return img
 
def escalaCinza(img):
  # Converter para escala de cor cinza
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return img

def negativo(img):
  # Invertida a imagem para negativo, com o cálculo (255 - imagem)
  img = 255 - img
  return img


def borrar(img):
  # Aplicado o método blur na imagem, passando a imagem e o parâmetro dimensão de como queremos borrar a imagem
  img = cv2.blur(img,(9,5))
  return img