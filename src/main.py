import os

import metodos.images.imagemMetodos as imagemMetodos
import metodos.filters.filtrosMetodos as filtrosMetodos

def opcoes():
    os.system("cls")
    print("Bem vindo(a)\n")
    print("1 - Selecionar imagem")
    print("0 - Sair")
    print("\nSelecione uma opção:")

def main():
  sair = False
  opcao = 0

  while (not sair):
    opcoes()
    opcao = int(input())

    match opcao:
      case 0:
        sair = True
        break
      case 1:
        imagem, caminhoImagem = imagemMetodos.selecionaImagem()
        imagem, filtroSelecionado = filtrosMetodos.selecionaFiltro(imagem, caminhoImagem)

        if (filtroSelecionado != 0):
          imagemMetodos.gravaImagem(imagem)
          imagemMetodos.showImagem(imagem)

main()