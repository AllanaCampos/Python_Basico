# Tutorial Ambiente Virtual

Para criar um ambiente virtual utilizando Conda, deve-se utilizar o seguinte comando:

```
conda create --name nome python=3.11
```

Onde nome se refere ao nome do ambiente virtual. 

É opcional a especificação da versão do python.

Para ativar o ambiente virtual deve-se utilizar o comando:

```
conda activate nome
```

Para desativar:

```
conda deactivate
```

# Visual Studio Code

Para utilizar o ambiente virtual no Visual Studio Code basta utilizar os comandos de ativação e desativação do ambiente virtual no terminal.

Caso o Visual Studio Code não reconheça o ambiente, é possível escolher o interpretador manualmente com os seguintes passos:

1. Abra a paleta de comandos pressionando Ctrl + Shift + p
2. Procure por Python: Select Interpreter e pressione Enter
3. Selecione o interpretador do seu ambiente virtual

# Jupyter

Para utilizar o ambiente virtual no Jupyter com o Anaconda Navigator deve-se abrir o Anaconda Navigator e no menu vertical selecionar Environments.

Esta aba permite a criação de ambientes virtuais e a execução dos já criados, necessitando apenas a seleção do mesmo.

Após escolher o ambiente desejado, volte ao Home e caso já esteja instalado execute o Jupyter, caso contrário instale antes.

