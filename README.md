# Projeto Final de Processamento de Imagem

# Filipe Tietbohl, Leonardo Miranda e Shaueny Ribeiro.

## 🚀 Objetivo
Este projeto foi criado e executado com o objetivo de fazer a aleteração das imagens conforme o usuário desejar, sendo ela selecionada pelo usuário e depois escolher qual o filtro a ser aplicado na imagem, dentre as opções no menu (desenho a lapis, cinza, negativo e sepia).

## 📋 Softwares necessários
Você precisará dos seguintes softwares para executar este aplicação:
* Phyton 3
* OpenCV 4

## 🔧 Instalação
Para auxilio na instalação utilize o tutorial:
* **[Video para ajuda na configuração] (por o link do youtube)**

## ⚙️ Sobre a aplicação

# 🔩 Como inicializar a aplicação
Após ter efetuado o clone do projeto:
1. Abra o Terminal / Prompt de Comando
2. Execute o seguinte comando: `phyton main.py `
3. Informar o caminho da imagem.
4. Aguarde o seguinte texto aparecer: _Bem vindo(a), 1- selecione a imagem, 2- sair_
5. Escolha a opção .
6. Informe o novo nome da imagem.

# 🛠️ Funcionalidades
Foram desenvolvidas 5 funcionalidades, para a execução de alteração de imagem 
 
 ### main:
  * opcoes(): Parte do primeiro menu onde o usuário pode selecionar a imagem ou sair.
  * main(): Menu que o usuário seleciona qual filtro deseja aplicar, entre as 5 opções (Faz a seleção do filtro e depois exibe a imagem com a alteração).

 ### imagemMetodos:
  * selecionaImagem(): É a função de seleção de imagem, que é chamada no main.
  * showImagem(): Função para exibir a imagem.
  * gravaImagem(): Função onde a pega do arquivo original e gravada com o identificador, também printada uma imagem com nome e local de arquivo gravada.

  ### filtrosMetodos:
   * opcoesFiltro(): Menu montado das com as 5 opções de filtros.

  ### filtros:
   * desenhoLapis(img): Foi desenvolvido o filtro de desenho a lapis onde é calculado o inverso, 255 é branco, 0 é preto e aplicado o blur. é feito o blend com o cv2.divide.
    ![image](https://user-images.githubusercontent.com/64978472/205903925-8e24a49f-0889-431d-a320-8961f525bf95.png)
    
    
   *  sepsia(img): Foi desenvolvido o filtro de sepia onde é feita a divisão e alteração das cores solidas.
  
    (ADICIONAR IMAGEM)
    
   *  escalaCinza(img): Foi desenvolvido o filtro de escala de cinza onde a imagem é aplicada a BGR2GRAY.
  
    (ADICIONAR IMAGEM)
    
   * meuPrimeiroFiltro(img): Foi desenvolvido o filtro para fazer a inversão das cores.
 
    (ADICIONAR IMAGEM)
    
   *  negativo(img): Foi desenvolvido o filtro de negativas a foto sendo ele pegando a imagem que é igual a 255 e fazendo a subtração dela mesma.

    (ADICIONAR IMAGEM)
   *  borrar(img): Foi desenvolvido o filtro de borrar, onde é pego a imagem e aplicado o blur.
