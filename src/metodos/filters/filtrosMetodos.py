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
        return imagem, opcao
      case 1:
        return filtros.sepia(imagem), opcao
      case 2:
        return filtros.desenhoLapis(imagem), opcao
      case 3:
        return filtros.inversaoCores(imagem), opcao
      case 4:
        return filtros.escalaCinza(imagem), opcao
      case 5:
        return filtros.negativo(imagem), opcao
      case 6:
        return filtros.borrar(imagem), opcao
      case default:
        sair = False
        

def opcoesFiltro():
    os.system("cls")
    print("1 - Sepia")
    print("2 - Desenho a Lápis")
    print("3 - Inversão de Cores")
    print("4 - Escala de Cinza")
    print("5 - Negativo")
    print("6 - Borrar")
    print("0 - Sair")
    print("\nSelecione um filtro:")