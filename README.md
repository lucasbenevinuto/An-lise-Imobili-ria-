**Projeto de Data Science: Análise de Imóveis para Aluguel nos Estados Unidos**

Descrição do Projeto
Este projeto tem como objetivo analisar imóveis para aluguel nos Estados Unidos, com foco na identificação das comodidades mais relevantes para o preço e localização de maior valor. Através de técnicas de Machine Learning, segmentação de mercado e análise de padrões, foi possível gerar insights valiosos sobre o comportamento do mercado imobiliário.

### Principais Ferramentas Utilizadas
- **Linguagem**: Python
- **Bibliotecas**:
  - `Pandas`: Para manipulação e análise de dados estruturados.
  - `NumPy`: Para operações matemáticas.
  - `Matplotlib` e `Seaborn`: Para visualização gráfica de dados.
  - `Scikit-learn`: Para modelagem estatística, regressão e análise preditiva.

### Descrição do Projeto
O objetivo principal deste projeto é analisar o mercado de aluguéis de apartamentos para a empresa fictícia Liberty Apartments. O foco está em identificar os fatores que influenciam o preço dos aluguéis em três cidades principais nos EUA. A análise foi estruturada para responder a cinco questões fundamentais levantadas pela empresa.

### Objetivos da Análise
1. **Relação entre preço e tamanho do apartamento**:
   - Foi realizado um estudo de correlação e análise de regressão linear entre a metragem quadrada e o preço de aluguel em cada cidade, com o objetivo de identificar padrões entre as localidades.
   
2. **Impacto da localização no preço**:
   - O dataset inclui dados geográficos que foram utilizados para segmentar as cidades em bairros ou áreas, permitindo um estudo da variação dos preços de aluguel com base na localização.

3. **Análise de amenidades**:
   - Uma análise foi conduzida para identificar quais amenidades, como estacionamento, academia, varanda, etc., mais influenciam no valor do aluguel em cada cidade.

4. **Principais fatores determinantes do preço**:
   - Usando técnicas de análise multivariada e regressão, foi identificada a influência de múltiplos fatores, como localização, metragem e amenidades, sobre o preço final do aluguel.

5. **Segmentação do mercado**:
   - Clusters de imóveis foram identificados com base em características similares, permitindo segmentar o mercado em diferentes grupos.

### Análises Realizadas
- **Análise descritiva**:
  - Um resumo estatístico dos dados foi gerado, incluindo a média, mediana e dispersão dos preços de aluguel.
  
- **Visualização de dados**:
  - Gráficos de dispersão e boxplots foram utilizados para explorar a distribuição dos preços, a correlação com o tamanho dos imóveis e a distribuição geográfica dos preços dentro de cada cidade.
  
- **Modelagem preditiva**:
  - Modelos de regressão linear foram implementados para prever o preço dos imóveis com base nas variáveis explicativas, como localização, tamanho e amenidades.
  
- **Clusterização**:
  - Técnicas de agrupamento foram utilizadas para identificar grupos homogêneos de apartamentos com base em suas características e valores de aluguel.

### Como Reproduzir o Projeto
1. Clone o repositório.
   ```bash
   git clone https://github.com/seu_repositorio/projeto-liberty-apartments.git
   ```
   
2. Instale as dependências.
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o Jupyter Notebook para visualizar as análises.
   ```bash
   jupyter notebook 10k.ipynb
   ```

### Insights Relevantes
- **Correlação entre tamanho e preço**: A metragem do imóvel é o fator que mais impacta o preço do aluguel em todas as cidades. No entanto, a elasticidade do preço em relação ao tamanho varia entre as cidades.
  
- **Impacto da localização**: Certas áreas das cidades têm aluguéis significativamente mais altos devido à proximidade com centros comerciais e áreas valorizadas. Essas informações podem ser usadas para ajustar as estratégias de marketing e precificação.

- **Amenidades valorizadas**: O impacto das amenidades no preço varia entre as cidades. Em algumas localidades, a presença de uma academia e estacionamento aumenta significativamente o valor do aluguel, enquanto em outras a demanda por varandas é maior.

### Estrutura do Repositório
```
/projeto-liberty-apartments
│
├── data/                # Diretório com os dados brutos
├── notebooks/           # Jupyter notebooks com as análises
├── src/                 # Scripts auxiliares
├── README.md            # Este arquivo
├── requirements.txt     # Dependências do projeto
└── LICENSE              # Licença do projeto
```

Esse README é um guia completo para o projeto de análise dos aluguéis da Liberty Apartments, fornecendo uma visão geral do projeto, ferramentas utilizadas, insights obtidos e instruções para execução.