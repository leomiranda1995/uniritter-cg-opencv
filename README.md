# Projeto Final de Processamento de Imagem

# Filipe Tietbohl, Leonardo Miranda e Shaueny Ribeiro.

## 🚀 Objetivo
Este projeto foi criado e executado com o objetivo de fazer a aleteração das imagens conforme o usuário desejar, sendo ela selecionada pelo usuário e depois escolher qual o filtro a ser aplicado na imagem, dentre as opções 5 opções no menu (desenho a lapis, cinza, negativo, sepia e inversão de cores).

## 📄 Repositórios
Foi utilizado um repositório público secundário para a execução do trabalho como teste.
* [Repositório de teste](https://github.com/leomiranda1995/uniritter-cg-opencv)
* [Repositório da entrega do trabalho](https://github.com/profvini/projetopi-leonardo_miranda)

## 📋 Softwares necessários
Você precisará dos seguintes softwares para executar este aplicação:
* Phyton 3
* OpenCV 4

## 🔧 Instalação
Para auxilio na instalação utilize o tutorial:
* [Video explicativo](https://youtu.be/oAH_GJclePY?t=463)
## ⚙️ Sobre a aplicação

## 🔩 Como inicializar a aplicação
Após ter efetuado o clone do projeto:
1. Abra o Terminal / Prompt de Comando
2. Execute o seguinte comando: `phyton main.py `
3. Informar o caminho da imagem.
4. Aguarde o seguinte texto aparecer: _Bem vindo(a), 1- selecione a imagem, 2- sair_
5. Escolha a opção .
6. Escolha entre as 5 opções de filtros.
7. Informe o novo nome da imagem.

## 🛠️ Funcionalidades
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
    
![desenho de lapis](https://user-images.githubusercontent.com/64978472/205937358-1337f434-6e20-4719-8509-92633ebf69ee.png)

    
   *  sepia(img): Foi desenvolvido o filtro de sepia onde é feita a divisão e alteração das cores solidas.
 
     
![sepia](https://user-images.githubusercontent.com/64978472/205937102-360c33a1-ff00-425e-8707-3ba1b902dee8.png)

  
    
   *  escalaCinza(img): Foi desenvolvido o filtro de escala de cinza onde a imagem é aplicada a BGR2GRAY.
  
    (ADICIONAR IMAGEM)
    
   * meuPrimeiroFiltro(img): Foi desenvolvido o filtro para fazer a inversão das cores.
 
![cor inversa](https://user-images.githubusercontent.com/64978472/205937302-9c80cf27-d96e-4a4a-aa6a-f902ff35793d.png)

    
    
   *  negativo(img): Foi desenvolvido o filtro de negativas a foto sendo ele pegando a imagem que é igual a 255 e fazendo a subtração dela mesma.

    (ADICIONAR IMAGEM)
    
   *  borrar(img): Foi desenvolvido o filtro de borrar, onde é pego a imagem e aplicado o blur.


## 🎯 Status do projeto
Projeto finalizado, atendendo a todos os requisitos solicitados pelo professo Vinicius Cassol. Foi implementado uma funcionalidade a mais do que o solicitado.


