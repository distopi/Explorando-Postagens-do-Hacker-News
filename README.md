# 📊 Explorando Postagens do Hacker News

Este repositório contém a minha solução e aprimoramento do projeto guiado **"Exploring Hacker News Posts"** da plataforma Dataquest. 

Embora seja um projeto com foco em iniciantes na análise de dados, aproveitei a oportunidade para ir além do escopo original (baseado em Jupyter Notebook) e refatorar a análise em um script Python estruturado. O objetivo é demonstrar não apenas a capacidade de extrair *insights* de dados, mas também a habilidade de escrever **código limpo, modularizado e pronto para produção**.

---

## 🎯 Objetivo da Análise

O [Hacker News](https://news.ycombinator.com/) é uma plataforma popular onde startups e profissionais de tecnologia compartilham artigos e projetos. As postagens mais comuns são divididas em duas categorias:
- **Ask HN:** Perguntas feitas à comunidade (ex: "Qual o melhor framework para front-end?").
- **Show HN:** Projetos, produtos ou descobertas compartilhadas com a comunidade.

O objetivo deste projeto é comparar esses dois tipos de postagens para determinar:
1. Qual categoria recebe mais comentários em média?
2. As postagens criadas em determinados horários recebem mais engajamento?

---

## 🌳 Habilidades Desbloqueadas

Este projeto serviu como um excelente laboratório prático para consolidar conhecimentos fundamentais em Python:

- **Manipulação de Arquivos:** Leitura fluente de planilhas usando `csv.DictReader`.
- **Tratamento Temporal:** Conversão e formatação de strings de tempo usando o módulo `datetime`.
- **Estruturas de Dados:** Uso otimizado de listas, dicionários e `collections.defaultdict` para agregações.
- **Boas Práticas (Clean Code):** Separação de responsabilidades em funções puras, isolamento de escopo (`__main__`) e *Type Hinting*.
- **Prevenção de Erros:** Tratamento de exceções (blocos `try/except`) para arquivos ausentes ou dados inconsistentes.

---

## 📈 Principais Insights Obtidos

Após processar o dataset (que foi previamente limpo pela equipe da Dataquest para remover postagens sem comentários), descobrimos que:

1. **Perguntar gera mais engajamento:** As postagens do tipo `Ask HN` recebem, em média, mais comentários do que as postagens `Show HN`. A comunidade é muito ativa em ajudar e debater dúvidas.
2. **O *Timing* é crucial:** Ao analisar as postagens `Ask HN`, identificamos que os posts criados no meio da tarde (horário da costa leste dos EUA, EST) tendem a atrair o maior número médio de comentários, indicando um pico de usuários ativos e dispostos a interagir.


```bash
git clone [https://github.com/seu-usuario/hacker-news-analysis.git](https://github.com/seu-usuario/hacker-news-analysis.git)
cd hacker-news-analysis
python main.py
