# init-template (pt-BR)

Este projeto tem como objetivo facilitar a criação de novos projetos, ou de projetos dentro de projetos utilizando templates de projetos que podem inclusive ser feito
por você!

## Como usar?
É fundamental ter o python 3.8.^ instalado 

NOTA: Até o presente momento este pacote é disponivel apenas em sistemas Unix (Linux e Mac), porém, muito em breve terá suporte para Windows, se estiver muito motivado para usar no windows têm 2 formas que serão discutidas no final da página

1. Com o pip:
  Este pacote já está disponivel no pip, para instalar é só usar o comando ```pip install init-template``` com isso instalando o pacote, então navegar para onde deseja iniciar um template e usar "python3 -m init_template.main --help" que listará os argumentos para a criação do projeto. Nota não recomendo instalar esse pacote num ambiente virtual, pois, para usá-lo se fará necessário a ativação do ambiente toda vez.

2. Clonando este repositório:
  Simples assim use ```git clone https://github.com/EliasOlie/init-template.git``` e preferencialmente faça um alias no seu .bashrc ou .zshrc da seguinte maneira ```alias [nome-do-comando]=python3 /caminho/completo/até/o/arquivo/main.py ``` (Deixe esse um espaço em branco entre "main.py" e o fim do comando para concatenar as opções) então toda vez que usar o nome do comando do alias ele vai executar esse módulo


## Usando o seu próprio template

Para usar o seu próprio template você pode:

1. Criar um repositório público no github com as configurações/estrutura desejada e usar o link do repositório com a flag "-t link" ou "--template link"

Em breve haverá uma forma de adicionar o seu repo ao código e assim virar opção direta! ;)

## Contribuindo

Muito obrigado por ajudar esse projeto e a comunidade open-source ❤️

1. Faça um fork desse repositório

  ![image](https://user-images.githubusercontent.com/63745733/195986925-f4317466-9cf3-4bdc-87cc-ee4820414e3d.png)
  Só clicar em fork que fará uma cópia desse repo para você

2. Clone o seu fork localmente

3. Faça suas alterações:
  NOTA!!!!
  Use uma branch de desenvolvimento!! ```git checkout -b dev```
  Use o guia de convenção da PEP 8: https://peps.python.org/pep-0008/ para reger o estilo do código, preferencialmente no vscode use ```ctrl + shift + p ``` para abrir a paleta de comandos e procure a opção "Format document" ou "Formatar documento" que baixará o pacote autopep8 e formatá o código com a conveção da pep8

4. Faça o commit das suas alterações e um pull request
  Após dar ```git push``` quando você for no seu repo "forqueado" você vai encontrar uma um botão verde escrito "Compare & pull request" é só clicar
  NOTA!!! É imprescindível que você escreva boas mensagens de commit e descreva na pr o máximo de detalhes sobre a sua mudança, o que de fato você mudou e como!

5. Agora é só esperar!
  Nota: desde já agradecemos pela contribuição, mas nem todo código vai ser aceito, muitas vezes podem vir sugestões que são nocivas ou que fugam do escopo do projeto e terão que ser descartadas, mas olhe pelo lado bom, ainda que sua branch não venha a ser usada, você têm ela e pode com ela criar seu próprio pacote e contribuir ainda mais!


## Solução temporária para usuários Windows:

1. WSL:
  Se você usa WSL é só seguir o passo a passo normal optando por qualquer uma das formas de instalação

2. Git bash
  Se você tem o git instalado, então pode (<s>e deve já que tanto o powershell quanto o cmd são péssimos</s>) usar o git bash como seu emulador de terminal e seguir o passo a passo normal optando por quialquer uma das formas de instalação

# init-template (en-US)

This project aims to facilitate the creation of new projects, or projects within projects using project templates that can even be done
by you!

## How to use

It is critical to have python 3.8.^ installed

NOTE: So far this package is only available for Unix systems (Linux and Mac), however, very soon it will have support for Windows, if you are very motivated to use it on Windows there are 2 ways that will be discussed at the end of the page

1. With pip:
  This package is already available on pip, to install just use the command ```pip install init-template``` with that installing the package, then navigate to where you want to start a template and use "python3 -m init_template.main --help" which will list the arguments for creating the project. Note I do not recommend installing this package in a virtual environment, because to use it, it will be necessary to activate the environment every time.

2. Cloning this repository:
  Simple as that use ```git clone https://github.com/EliasOlie/init-template.git``` and preferably make an alias in your .bashrc or .zshrc as follows ```alias [name-of- command]=python3 /full/path/to/the/file/main.py ``` (Leave the empty space between "main.py" and the end to concatenate the options) so every time you use the alias command name it will run that module

## Using your own template

To use your own template you can:

1. Create a public repository on github with the desired settings/structure and use the repository link with the "-t link" or "--template link" flag

Soon there will be a way to add your repo to the code and thus become a direct option! ;)

## Contributing

Thank you so much for helping this project and the open-source community ❤️

1. Fork this repository

  ![image](https://user-images.githubusercontent.com/63745733/195986925-f4317466-9cf3-4bdc-87cc-ee4820414e3d.png)
  Just click on fork that will make a copy of this repo for you

2. Clone your fork locally

3. Make your changes:
  NOTE!!!!
  Use a development branch!! ```git checkout -b dev```
  Use the PEP 8 convention guide: https://peps.python.org/pep-0008/ to govern the code style, preferably in vscode use ```ctrl + shift + p ``` to open the command palette and look for the option "Format document" which will download the autopep8 package and format the code with the pep8 convention

4. Commit your changes and a male a pull request
  After giving ```git push``` when you go to your forked repo you will find a green button that says "Compare & pull request" just click
  NOTE!!! It is imperative that you write good commit messages and describe in the pr as much detail as possible about your change, what you actually changed and how!

5. Now just wait!
  Note: we thank you in advance for your contribution, but not all code will be accepted, many times suggestions may come that are harmful or that escape the scope of the project and will have to be discarded, but look on the bright side, even if your branch does not come to be used, you have it and you can create your own package with it and contribute even more!

## Temporary workaround for Windows users:

1. WSL:
  If you use WSL, just follow the normal step by step, opting for any of the installation methods

2. gitbash
  If you have git installed, then you can (<s>and you should since both powershell and cmd suck</s>) use git bash as your terminal emulator and follow the normal step by step opting for either of installation forms