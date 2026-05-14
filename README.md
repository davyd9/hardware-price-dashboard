# Buscador de Preços - Hardware Dashboard

Um dashboard analítico e interativo desenvolvido em **Python** com **Streamlit** para simular o monitoramento e a organização de centenas de peças de hardware, com redirecionamento dinâmico de compras.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Interface Web (Front-end):** Streamlit
* **Manipulação de Dados:** Pandas
* **Requisições e Formatação:** Requests & urllib

## Arquitetura e Soluções Técnicas
Este projeto foi desenvolvido com foco em resiliência e experiência do usuário (UX):

* **Data Mocking Estratégico:** Para contornar bloqueios de segurança e requisições limitadas de APIs públicas (Erro HTTP 403 Forbidden), o sistema utiliza um motor de simulação de dados de alta fidelidade. Isso garante que o portfólio esteja 100% operante e rápido para testes de recrutadores.
* **Organização Automática (Data Wrangling):** O script processa as categorias em tempo real e utiliza o poder do `Pandas` para agrupar e isolar os produtos em abas expansíveis, evitando a poluição visual na tela.
* **Deep Linking:** Geração automatizada de URLs de busca precisas para o e-commerce real. O sistema processa strings de texto, substitui caracteres especiais e cria links de compra autênticos baseados no nome gerado da peça.

##  Como executar localmente

1. Clone este repositório para sua máquina:
   ```bash
   git clone [https://github.com/davyd9/hardware-price-dashboard.git](https://github.com/davyd9/hardware-price-dashboard.git)
