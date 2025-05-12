
# 🧠 Projeto PBL – Fase 6: Comparação de Abordagens em Visão Computacional  
## 🚗 Detecção e Classificação de Veículos: YOLOv5 Adaptado, YOLOv5 Tradicional e CNN do Zero

Este repositório contém a **Entrega 2** do Projeto da Fase 6 do curso 1TIAOR da FIAP.  
Dando continuidade ao sistema de visão computacional iniciado na Entrega 1, o objetivo desta etapa é comparar diferentes abordagens para detecção e/ou classificação de veículos (**carros** e **motos**), avaliando desempenho, facilidade de uso e aplicabilidade.

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

## 📜 Descrição do Desafio

A FarmTech Solutions, empresa fictícia que orienta o contexto do projeto, deseja entender quais abordagens de Visão Computacional são mais adequadas para detectar veículos em diferentes contextos.

Nesta entrega, foram aplicadas três abordagens distintas:

| Abordagem                      | Técnica                      | Objetivo                   |
|-------------------------------|------------------------------|----------------------------|
| ✅ YOLOv5 Adaptado            | Modelo treinado do zero      | Detecção com bounding box |
| 📦 YOLOv5 Tradicional         | Modelo pré-treinado (COCO)   | Detecção genérica          |
| 🧱 CNN Desenvolvida do Zero   | Rede simples de classificação | Classificação binária      |

---

## ⚙️ Execução do Projeto

O notebook desta entrega foi projetado para ser executado tanto no **Google Colab** quanto **localmente com GPU**, com:

- Detecção automática do ambiente
- Montagem do Google Drive
- Validação de estrutura e integridade dos dados
- Execução modular e organizada por blocos

---

## 📊 Comparações Realizadas

As abordagens foram comparadas com base em:

- 🔧 Facilidade de uso e integração
- 📈 Precisão (mAP, acurácia, recall, F1-score)
- ⏱️ Tempo de treinamento e de inferência
- 🧠 Capacidade de generalização
- 🖼️ Resultados visuais das detecções e classificações

Além disso, a CNN foi treinada em duas configurações:
- 🔁 **30 épocas**
- 🔁 **60 épocas**

---

## 📁 Estrutura do Projeto

```
📦 1TIAOR20242_FASE6_CAP1
│── 📁 notebooks
│   ├── 📄 Entrega01_YOLOv5_adaptado.ipynb
│   ├── 📄 Entrega02_Comparacao_YOLO_CNN.ipynb
│
│── 📁 dataset_images          # Imagens anotadas para YOLO
│── 📁 dataset_cnn             # Imagens organizadas por classe para CNN
│── 📁 modelos                 # Modelos treinados (YOLO e CNN)
│
│── 📄 README_entrega01.md
│── 📄 README_entrega02.md
│── 📄 requirements.txt
```

---

## 📈 Resultados e Conclusões

- 🏆 **YOLOv5 Adaptado (60 épocas)** obteve o melhor desempenho com mAP@0.5 ≈ 0.9950, com foco e precisão nos objetos do domínio.
- ⚙️ **YOLOv5 Tradicional** foi fácil de usar, mas apresentou falsos positivos devido à sua natureza genérica (ex: confundiu motos com "train").
- 🧠 **CNN (60 épocas)** apresentou desempenho razoável para classificação direta (acurácia de 62,5%), mas sem capacidade de localizar objetos.

---

## 📓 Notebooks

📥 Acesse o notebook desta entrega:

[`Entrega02_Comparacao_YOLO_CNN.ipynb`](./Entrega02_Comparacao_YOLO_CNN.ipynb)

---

## 📋 Licença

Este projeto segue a licença Creative Commons:

[![CC BY 4.0](https://mirrors.creativecommons.org/presskit/icons/cc.svg)](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)
[![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg)](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)
