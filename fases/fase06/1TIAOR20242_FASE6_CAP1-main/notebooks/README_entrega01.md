# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🚗 Projeto PBL – Fase 6: Visão Computacional com YOLOv5

Este repositório contém a **Entrega 1** do Projeto da Fase 6 da FIAP, onde desenvolvemos um sistema de visão computacional para detecção de veículos usando YOLOv5 adaptado.


---

## 👨‍🎓 Integrantes:

- [Edmar Ferreira Souza](https://www.linkedin.com/in/)
- [Alexandre Oliveira Mantovani](https://www.linkedin.com/in/alexomantovani)
- [Ricardo Lourenço Coube](https://www.linkedin.com/in/ricardolcoube/)
- [Jose Andre Filho](https://www.linkedin.com/in/joseandrefilho)

## 👩‍🏫 Professores:

- Tutor: [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona)
- Coordenador: [André Godoi](https://www.linkedin.com/in/profandregodoi)

---

## 📜 Descrição

### Reconhecimento de Veículos: Carros e Motos

Este projeto faz parte da **Fase 6 do Projeto Baseado em Problemas (PBL)** da FIAP, no contexto da empresa fictícia *FarmTech Solutions*, que está expandindo sua atuação em inteligência artificial para a área de visão computacional.

O desafio consistiu em criar um modelo de detecção de objetos capaz de identificar dois tipos de veículos: **carros** e **motos**, utilizando imagens reais rotuladas manualmente e analisando o impacto do número de épocas no desempenho do modelo.


## 📁 Estrutura de Pastas

Abaixo está a estrutura dos principais arquivos e diretórios deste projeto:

```
📦 1TIAOR20242_FASE6_CAP1
│── 📁 configurations                                          # Arquivos de configuração YAML para treino
│   ├── 📄 veiculos_local.yaml                                 # Configuração para uso local (caminhos relativos) 
│   ├── 📄 veiculos.yaml                                       # Configuração para uso no Colab (caminhos absolutos) 
│── 📁 dataset_images                                          # Pasta principal contendo imagens e labels
│   ├── 📁 images                                              # Subpasta com as imagens divididas em conjuntos
│   │   ├── 📁 train                                           # Imagens utilizadas no treinamento (64 imagens)
│   │   ├── 📁 val                                             # Imagens utilizadas na validação (8 imagens)
│   │   ├── 📁 test                                            # Imagens utilizadas para avaliação final (8 imagens)
│   ├── 📁 labels                                              # Subpasta com os arquivos de rótulo no formato YOLO
│   │   ├── 📁 train                                           # Labels correspondentes às imagens de treinamento
│   │   ├── 📁 val                                             # Labels correspondentes às imagens de validação
│   │   ├── 📁 test                                            # Labels correspondentes às imagens de teste
│── 📁 notebooks                                               # Notebooks e logs do projeto 
│   ├── 📁 logs                                                # Saída completa dos treinamentos 
│   │   ├── 📄 veiculos_yolo_30ep.log                          # Log do treinamento com 30 épocas 
│   │   ├── 📄 veiculos_yolo_60ep.log                          # Log do treinamento com 60 épocas 
│   ├── 📄 1TIAOR20242_FASE6_CAP1_Entrega01.ipynb              # Notebook da Entrega 1 (YOLOv5 adaptado) 
│   ├── 📄 1TIAOR20242_FASE6_CAP1_Entrega02.ipynb              # Notebook da Entrega 2 (comparações com outras abordagens) 
│── 📄 README.md                                               # Documento de apresentação do projeto 
│── 📄 requirements.txt                                        # Dependências utilizadas para execução local

```
> A estrutura foi organizada para facilitar a execução e manutenção do projeto em diferentes ambientes (local e Colab), além de manter uma separação clara entre dados, modelos e documentação.


### Aquisição e preparação do dataset

Para este projeto, foram utilizadas imagens de dois objetos distintos: **carros** e **motos**. As imagens foram obtidas manualmente a partir de pesquisas com licenciamento livre (Creative Commons), screenshots e tiradas por nossos integrantes, priorizando variedade de ângulos e contextos.

Após a coleta, foram selecionadas:

- 40 imagens de carros
- 40 imagens de motos

As imagens foram rotuladas manualmente utilizando a plataforma [MakeSense.ai](https://www.makesense.ai/), onde foram desenhadas as bounding boxes para cada objeto identificado e atribuídos os rótulos correspondentes.

A estrutura final do dataset foi organizada conforme o padrão exigido pelo YOLOv5, separando as imagens e seus respectivos rótulos em três conjuntos:

- **Treinamento**: 32 imagens de cada classe (total de 64)
- **Validação**: 4 imagens de cada classe (total de 8)
- **Teste**: 4 imagens de cada classe (total de 8)


## ⚙️ Execução do Projeto

O notebook foi desenvolvido para rodar tanto no **Google Colab** quanto **localmente com GPU**, com detecção automática do ambiente e carregamento dinâmico das configurações.


## 📊 Comparações Realizadas

Modelos treinados com:
- 🔁 **30 épocas** (~72 segundos)
- 🔁 **60 épocas** (~120 segundos)

As comparações incluem:
- `box_loss`, `obj_loss`, `precision`, `recall`, `mAP@0.5`
- Visualização gráfica (`results.csv` e `results.png`)
- Inferência em imagens de teste com grid visual 2x8

## 🧠 Principais Aprendizados

- ✅ YOLOv5 adaptado funciona muito bem com datasets pequenos e balanceados
- 🔄 Treinar mais épocas melhora a performance, mas aumenta o custo computacional
- 🔍 Visualização e análise gráfica são essenciais para validar o comportamento real do modelo
- 🔄 Ter suporte para Colab e execução local traz flexibilidade para o desenvolvimento e testes
- 🛠️ Ferramentas como MakeSense.ai aceleram a rotulagem e padronizam o dataset

## 📓 Notebook

📥 Acesse o notebook da entrega 1 aqui:

[`1TIAOR20242_FASE6_CAP1_Entrega01.ipynb`](./Entrega01_YOLOv5_adaptado.ipynb)

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
