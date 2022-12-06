# Projeto Final de Processamento de Imagem

### Filipe Tietbohl, Leonardo Miranda e Shaueny Ribeiro.

## 🚀 Objetivo
Este projeto foi criado e executado com o objetivo de fazer a alteração das imagens conforme o usuário desejar, sendo ela selecionada pelo usuário e depois escolher qual o filtro a ser aplicado na imagem, dentre as opções 5 opções no menu (desenho a lapis, cinza, negativo, sepia e inversão de cores).

## 📄 Repositórios
Foi utilizado um repositório público secundário para a execução do trabalho como teste.
* [Repositório de teste](https://github.com/leomiranda1995/uniritter-cg-opencv)
* [Repositório da entrega do trabalho](https://github.com/profvini/projetopi-leonardo_miranda)

## 📋 Softwares necessários
Você precisará dos seguintes softwares para executar este aplicação:
Instalar o Python em seu computador
* [Phyton 3](https://www.python.org/downloads/)

* [Clonar o projeto](https://github.com/leomiranda1995/uniritter-cg-opencv.git)

## 🔧 Instalação
Para auxilio na instalação execute o arquivo Config.bat da raiz do projeto ou siga o tutorial abaixo:
* Após abra o prompt de comando na raiz do projeto e execute os comandos abaixo:
```sh
pip install virtualenv
pip install opencv-python
virtualenv opencv
cd opencv\Scripts
activate
cd..
cd..
cd src
pip install numpy
pip install matplotlib
```

## ⚙️ Sobre a aplicação

## 🔩 Como inicializar a aplicação
Após ter efetuado o clone do projeto e instalado as dependências do projeto:
1. Abra o Terminal / Prompt de Comando no diretório \src
2. Execute o seguinte comando: `python main.py `
3. Informar o caminho da imagem. (ex: arquivos/bulbasaur.png)
4. Aguarde o seguinte texto aparecer: _Bem vindo(a), 1- selecione a imagem, 2- sair_
5. Escolha a opção .
6. Escolha entre as 5 opções de filtros.
7. Informe o novo nome da imagem. (ex: bulbasaur_novo)

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
   * desenhoLapis(img): Foi desenvolvido o filtro de desenho a lapis onde a imagem é convertida em tons de cinza para após ser invertida para negativo. Após é aplicado o método de blur guassiano e após combinadas as imagens em tons de cinza da etapa 1 com o negativo desfocado da etapa 3
    
![desenho de lapis](https://user-images.githubusercontent.com/64978472/205940521-4044454e-3139-45be-a706-beb1eadac35a.png)



   *  sepia(img): Foi desenvolvido o filtro de sepia onde é feita a divisão e alteração das cores solidas.
 
![sepia](https://user-images.githubusercontent.com/64978472/205940346-ced907f7-8282-48b1-8f9c-ed95c393f8ba.png)    
  
  
  
   * inversaoCores(img): Foi desenvolvido o filtro para inverter as cores de azul por vemelho, verde por azul e vermelho por verde.
 
![cor inversa](https://user-images.githubusercontent.com/64978472/205941308-210951cb-2cb7-483d-a00f-c1d1009869b1.png)




   *  negativo(img): Foi desenvolvido o filtro de negativas a foto sendo ele inverte a imagem para negativo, com o cálculo (255 - imagem).

![WhatsApp Image 2022-12-06 at 11 28 15](https://user-images.githubusercontent.com/64978472/205940689-61bfb02d-cf7e-4b82-9234-147e701d327f.jpeg)
    

   *  borrar(img): Foi desenvolvido o filtro de borrar, onde é aplicado o método blur na imagem, passando a imagem e o parâmetro de dimensão para borrar a imagem
   
![WhatsApp Image 2022-12-06 at 11 28 15 (1)](https://user-images.githubusercontent.com/64978472/205940853-32341f75-358b-4911-b8dd-c29c045d4927.jpeg)



## 🎯 Status do projeto
Projeto finalizado, atendendo a todos os requisitos solicitados pelo professor Vinicius Cassol. Foi implementado uma funcionalidade a mais do que o solicitado.


