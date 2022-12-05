import metodos.filters.filtros as filtros
import os

def selecionaFiltro(imagem):
  sair = False
  opcao = 0

  while (not sair):
    opcoesFiltro()
    opcao = int(input())

    sair = True

    match opcao:
      case 0:
        return imagem, 0
      case 1:
        return filtros.sepia(imagem), 1
      case 2:
        return filtros.desenhoLapis(imagem), 2
      case 3:
        return filtros.meuPrimeiroFiltro(imagem), 3
      case 4:
        return filtros.escalaCinza(imagem), 4 # DESENVOLVER FILTRO
      case 5:
        return filtros.negativo(imagem), 5 # DESENVOLVER FILTRO
      case default:
        sair = False
        

def opcoesFiltro():
    os.system("cls")
    print("1 - Sepia")
    print("2 - Desenho a Lápis")
    print("3 - Primeiro Filtro")
    print("4 - Escala de Cinza")
    print("5 - Negativo")
    print("0 - Sair")
    print("\nSelecione um filtro:")