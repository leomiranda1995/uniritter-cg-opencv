import numpy as np
import cv2
import metodos.images.cores as cores

def desenhoLapis(img):
  # calculando o inverso, 255 é branco 0 é preto e aplicando o blur
  img_gray_inv = 255 - img
  img_blur = cv2.GaussianBlur(img_gray_inv, (21,21), 0, 0)

  # fazemos o blend com o cv2.divide
  img_blend = cv2.divide(img, 255 - img_blur, scale = 256)
  return img_blend


def sepia(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32)/255
    #solid color
    sepia = np.ones(img.shape)
    sepia[:,:,0] *= 153 #B
    sepia[:,:,1] *= 204 #G
    sepia[:,:,2] *= 255 #R
    #hadamard
    sepia[:,:,0] *= normalized_gray #B
    sepia[:,:,1] *= normalized_gray #G
    sepia[:,:,2] *= normalized_gray #R
    return np.array(sepia, np.uint8)


def meuPrimeiroFiltro(img):
  altura, largura, canaisDeCor = img.shape

  for y in range(0, altura):
    for x in range(0, largura):
      azul, verde, vermelho = cores.getColor(img, x, y)
      img = cores.setColor(img, x, y, verde, azul, azul)
  return img
 
def escalaCinza(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return img

def negativo(img):
  img = 255 - img
  return img


def borrar(img):
  img = cv2.blur(img,(9,5))
  return img