# Curso em Vídeo Python 3

Acompanhamento do curso de Python 3 do Gustavo Guanabara, do Curso em Vídeo. O repositório
guarda as anotações de cada aula e a resolução dos exercícios, organizados na mesma divisão em
Mundos que o curso usa.

[Playlist do curso no YouTube](https://www.youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0)

## Progresso

**Curso concluído: 115 dos 115 exercícios.**

| Mundo | Conteúdo | Exercícios |
| --- | --- | --- |
| 1 — Fundamentos | tipos primitivos, operadores, módulos, strings, condições, cores no terminal | 35 de 35 |
| 2 — Estruturas de controle | condições aninhadas, `for`, `while`, interrupção de repetições | 36 de 36 |
| 3 — Estruturas compostas | tuplas, listas, dicionários, funções, modularização, tratamento de erro | 44 de 44 |

## Organização

```text
Mundo 1 - Fundamentos/
  Aulas/          anotações das aulas, numeradas como no curso
  Exercícios/     ex001 … ex035

Mundo 2 - Estruturas de controle/
  Aulas/          aulas 12 a 15
  Exercícios/     ex036 … ex071

Mundo 3 - Estruturas compostas/
  Aulas/          aulas 16 a 23, incluindo a pasta de modularização
  Exercícios/     ex072 … ex115

Extras/
  Funções reutilizáveis/   utilidades próprias usadas em vários exercícios
  Sistema de estoque/      exercício extra, fora do curso
  Rascunhos/               testes soltos
```

Os arquivos de aula seguem a numeração dos vídeos, então a ordem da pasta é a ordem do curso.
Alguns exercícios do Mundo 3 têm uma segunda versão com o sufixo `_guanabara`: é a resolução do
professor, guardada ao lado da minha para comparação. A partir do exercício 107 as soluções são
pastas com vários arquivos, porque as aulas passam a tratar de módulos e pacotes.

## Extras

Conteúdo que não faz parte do curso.

**Sistema de estoque** (`Extras/Sistema de estoque/apresentar.py`). É um exercício extra de console
para uma loja de artigos esportivos: login, cadastro, edição e exclusão de produtos, controle de
estoque com limites mínimo e máximo, cadastro de usuários e registro de venda. Roda em memória,
sem persistência.

## Como executar

Os exercícios usam só a biblioteca padrão do Python, com uma exceção. Rode qualquer um direto:

```bash
python "Mundo 1 - Fundamentos/Exercícios/ex001.py"
```

A partir do exercício 107 as soluções são pastas: o que se executa é o `teste.py` ou o
`sistema.py` de dentro delas. Funciona de qualquer diretório, o Python resolve os imports a
partir da pasta do próprio script, e os exercícios que leem ou gravam arquivo fazem o mesmo com
os caminhos.

### A exceção: exercício 021

O `ex021.py` toca um arquivo de áudio e é o único que depende de biblioteca externa:

```bash
pip install pygame
```

O mp3 não está versionado, é obra de terceiro, e distribuir não é da minha alçada. Para rodar,
coloque qualquer arquivo de áudio como `ex021.mp3`, na mesma pasta do script. O caminho é
resolvido a partir da localização do próprio arquivo, então ele funciona de qualquer diretório.
