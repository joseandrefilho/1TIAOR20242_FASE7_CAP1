
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

---

# Cap 1 - A consolidação de um sistema  
### Projeto PBL - Fase 7

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

## 📌 Descrição do Projeto
Este repositório apresenta o projeto da Fase 7 do curso 1TIAOR20242 da FIAP, desenvolvido no contexto do Projeto Baseado em Problemas (PBL).  
O desafio proposto pela empresa fictícia **FarmTech Solutions** envolveu a aplicação de técnicas de **Visão Computacional** com foco em:

- 📦 Detecção de objetos
- 🧠 Classificação de imagens
- 🛠️ Comparação entre arquiteturas modernas de IA

---
## 📦 Entregas do Projeto

### 🧩 Entrega 1 – YOLOv5 Adaptado
Desenvolvimento completo de um sistema de detecção de veículos (**carros** e **motos**) utilizando o modelo **YOLOv5**, treinado com dataset customizado.

🔗 [`README_entrega01.md`](./notebooks/README_entrega01.md)  
📓 [`Notebook Entrega 1`](./notebooks/Entrega01_YOLOv5_adaptado.ipynb)

---

### 🧪 Entrega 2 – Comparação entre Abordagens

Comparação entre três abordagens distintas:
- ✅ YOLOv5 adaptado (com re-treinamento)
- 📦 YOLOv5 tradicional (pré-treinado, sem ajustes)
- 🧱 CNN do zero (classificação binária com softmax)

🔗 [`README_entrega02.md`](./notebooks/README_entrega02.md)  
📓 [`Notebook Entrega 2`](./notebooks/Entrega02_Comparacao_YOLO_CNN.ipynb)

---

---

## 📈 Principais Aprendizados

- Diferença prática entre **detecção e classificação**
- Importância da **personalização de modelos** (ex: YOLO adaptado vs tradicional)
- Limitações e pontos fortes de abordagens como **CNNs simples**
- Boas práticas de organização de projetos em **notebooks e GitHub**
- Técnicas para análise crítica de resultados com **métricas e visualizações**

---

## 🧗‍♀️ Desafios Enfrentados

- Curadoria e organização do dataset (imagens balanceadas, rotulagem no MakeSense)
- Configuração de ambiente local com GPU e integração com Google Colab
- Interpretação de métricas complexas como mAP e F1-score
- Prevenção de overfitting em treinos com CNN

---

## ▶️ Demonstração em Vídeo

🎥 Link para o vídeo de apresentação (YouTube – não listado): **[\[Clique aqui\]](https://youtu.be/OYT0TIxygZY)**

---

## 📁 Estrutura Geral do Projeto

```
📦 1TIAOR20242_FASE6_CAP1
│
│── 📁 configurations                                   
│   ├── 📄 veiculos_local.yaml                          # Configuração para uso local (caminhos relativos) 
│   ├── 📄 veiculos.yaml                                # Configuração para uso no Colab (caminhos absolutos) 
├── 📁 dataset_cnn                                      # Para treino da CNN
├── 📁 dataset_images                                   # Para treino do YOLO
├── 📁 notebooks
│   ├── 📄 Entrega01_YOLOv5_adaptado.ipynb              # Notebook da entrega 01
│   ├── 📄 Entrega02_Comparacao_YOLO_CNN.ipynb          # Notebook da entrega 02
│   ├── 📄 README_entrega01.md                          # Readme contendo a documentação da entrega 01
│   ├── 📄 README_entrega02.md                          # Readme contendo a documentação da entrega 02
├── 📄 README.md                                        # Este arquivo
└── 📄 requirements.txt                                 
```
---
## 🛠️ Como Executar o Projeto

### 🔁 Execução no Google Colab
1. Acesse o notebook da entrega desejada na pasta `notebooks/`.
2. Execute as células sequencialmente.
3. Conecte seu Google Drive quando solicitado.
4. Garanta que as imagens estejam no Google Drive e que os arquivos de configuração estejam na pasta correta.
5. Verifique se os caminhos das pastas e modelos estão corretos.

### 💻 Execução Local
1. Certifique-se de ter uma GPU compatível (NVIDIA) com CUDA.
2. Clone este repositório:
```bash
git clone https://github.com/joseandrefilho/1TIAOR20242_FASE6_CAP1.git
cd seurepositorio
```
3. Ative um ambiente virtual e instale os requisitos.
4. Execute os notebooks via Jupyter ou VSCode.

### ✅ Requisitos
Antes de tudo, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

> Obs.: O projeto detecta automaticamente se está no Colab ou local e adapta os caminhos conforme o ambiente.

---


## 📝 Licença

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
Este projeto segue o modelo FIAP e está licenciado sob 
<a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer">Attribution 4.0 International (CC BY 4.0)</a>.
</p>
