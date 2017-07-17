*(Versão em português abaixo - Portuguese version below)*

Portuguese Pseudoword Generator
===============================
This program generates pseudowords following Portuguese phonotactic rules.
It has an intuitive interface, and allows to edit results before saving them to a .txt file.

How to run it
-------------
1. Install Python version 3.5 or newer (https://www.python.org/downloads/).
2. Open a Terminal (Linux or Mac) and go to the directory where the PseudowordGenerator.py and the words.txt files are saved. For example, if the folder containing the application is saved in Desktop, type:
```
cd Desktop/PseudoWordGenerator
```
and press enter.
3. Then, still in the Terminal, type:
```
python PseudowordGenerator.py
```
or
```
python3 PseudowordGenerator.py
```

How to use
----------
### What to fill in?

#### Pseudoword configuration
Enter the following requested information:
* `Number of pseudowords` to generate
* `Minimum number of syllables` per word
* `Maximum number of syllables` per word

#### Syllable configuration
Select the desired syllable structure(s) to be used among:
* `onset + peak + coda`
* `onset + peak`
* `peak`
* `peak + coda`

Or select
* `random`

to activate all.

### Output
* Click on "Generate" to generate words according to the input.
* The words are displayed in the listbox on the right.
* To delete any words, select them on the listbox and click on `Delete word(s)`. For multiple selections, keep the `Ctrl` (Windows) or `cmd` (Mac) key pressed and then click on the entries.
* To delete all generated pseudowords at once, click on the `Clear all` button.
* Click on `Save to file` to save the list as it appears on the listbox. A .txt file with the pseudowords will be saved in the directory where the tool is saved.
* Click `Exit` to terminate the program.

About the code
--------------
Written in Python 3.5.

Authors
-------
* Ignacio Rubio Majano
* Andreia Schurt Rauber
* Roshanak Hamidi

Reference
---------
Please cite as:
Rubio Majano, I., Hamidi, R., Rauber, A.S. (2016). Portuguese Pseudoword Generator [Computer Program].
Available at https://sites.google.com/site/asrauber/pseudowordGenerator

***

*(Portuguese version)*

Gerador de pseudopalavras do português
======================================
Este aplicativo gera pseudopalavras seguindo as regras fonotáticas do português.
O aplicativo tem uma interface intuitiva e permite editar os resultados antes de salvá-los em um arquivo .txt.

Como rodar o aplicativo
-----------------------
1. Instale o Python versão 3.5 ou mais recente (https://www.python.org/downloads/).
2. Abra um Terminal (Linux ou Mac) e vá para o diretório onde os arquivos PseudowordGenerator.py e words.txt estão salvos. Por exemplo, se a pasta contendo o aplicativo estiver salva no Desktop, digite:
```
cd Desktop/PseudoWordGenerator
```
e pressione Enter.
3. Em seguida, ainda no Terminal, digite:
```
python PseudowordGenerator.py
```
ou
```
python3 PseudowordGenerator.py
```

Como usar
---------
### Quais informações devo fornecer?
#### Configuração da pseudopalavra
Digite as seguintes informações:
* `Number of pseudowords` a serem generadas
* `Minimum number of syllables` por palavra
* `Maximum number of syllables` por palavra

#### Configuração da sílaba
Selecione a(s) estrutura(s) silábica(s) desejada(s):
* `onset + peak + coda`
* `onset + peak`
* `peak`
* `peak + coda`

Ou selecione
* `random`
para ativar todas as opções.

### Resultados
* Clique em "Generate" para gerar palavras de acordo com as informações fornecidas.
* As palavras serão exibidas na caixa de texto à direita.
* Para deletar uma pseudopalavra, selecione-a na caixa de texto e clique em `Delete word(s)`. Para selecionar várias pseudopalavras, mantenha a tecla `Ctrl` (Windows) ou `cmd` (Mac) pressionada enquanto clica nas entradas.
* Para deletar todas as pseudopalavras geradas de uma única vez, clique no botão `Clear all`.
* Clique em "Save to file" para salvar a lista de pseudopalavras que aparece na caixa de texto. Um arquivo .txt contendo as pseudopalavras será salvo no mesmo diretório onde a ferramenta está salva.
* Clique em `Exit` para sair do aplicativo.

Sobre o programa
----------------
Escrito em Python 3.5.

Autores
-------
* Ignacio Rubio Majano
* Andreia Schurt Rauber
* Roshanak Hamidi

Referência
----------
Citar como:
Rubio Majano, I., Hamidi, R., Rauber, A.S. (2016). Portuguese Pseudoword Generator [Computer Program].
Available at https://sites.google.com/site/asrauber/pseudowordGenerator
