import streamlit as st
import pandas as pd
import random
import urllib.parse
import time

# 1. Configuração visual da página
st.set_page_config(page_title="Radar de Hardware VIP", layout="wide")
st.title(" Radar de Preços - Mercado Livre (Edição Hardware)")
st.markdown("Monitoramento de mercado simulado de alta performance com links reais de redirecionamento.")

#peças Hardware
categorias_hardware = [
    "SSD SATA", "SSD NVMe M.2", "Memória RAM DDR4", "Memória RAM DDR5",
    "Placa de Vídeo RTX", "Placa de Vídeo Radeon", "Processador AMD Ryzen",
    "Processador Intel Core", "Placa Mãe AM4", "Fonte de Alimentação"
]

# Marcas famosas para simular
marcas = {
    "SSD SATA": ["Kingston", "Crucial", "SanDisk", "Western Digital"],
    "SSD NVMe M.2": ["Samsung 980", "WD Black", "XPG S70", "Corsair"],
    "Memória RAM DDR4": ["Corsair Vengeance", "HyperX Fury", "XPG Spectrix", "Crucial Ballistix"],
    "Memória RAM DDR5": ["Corsair Dominator", "G.Skill Trident Z5", "Kingston Fury", "Adata"],
    "Placa de Vídeo RTX": ["ASUS Dual RTX 3060", "Gigabyte RTX 4060", "MSI RTX 4070", "Galax RTX 3050"],
    "Placa de Vídeo Radeon": ["Sapphire RX 6600", "ASUS RX 7600", "PowerColor RX 6700 XT", "Gigabyte RX 7800 XT"],
    "Processador AMD Ryzen": ["Ryzen 5 5600", "Ryzen 7 5700X", "Ryzen 5 7600", "Ryzen 9 5900X"],
    "Processador Intel Core": ["Core i5 12400F", "Core i7 13700K", "Core i3 12100F", "Core i9 14900K"],
    "Placa Mãe AM4": ["ASUS TUF B550M", "Gigabyte B450M DS3H", "MSI MAG B550", "ASRock A320M"],
    "Fonte de Alimentação": ["Corsair CV650", "XPG Core Reactor 850W", "Pichau Nidus 500W", "EVGA 600W"]
}

if st.button("🚀 Iniciar Varredura Profunda (Simulação API)", use_container_width=True):
    lista_ofertas = []
    
    progresso = st.progress(0)
    status_texto = st.empty()
    
    with st.spinner("Processando banco de dados de hardware..."):
        
        for i, categoria in enumerate(categorias_hardware):
            status_texto.text(f"Mapeando a categoria: {categoria}...")
            
            # Gerando 30 produtos
            for _ in range(30):
                marca_escolhida = random.choice(marcas[categoria])
                variacao = random.choice(["Gamer", "Pro", "Edição Limitada", "RGB", "Black", "Branca", ""])
                
                titulo_produto = f"{categoria} {marca_escolhida} {variacao}".strip()
                
                #preços coerentes
                preco_base = random.uniform(200.0, 3500.0)
                tem_desconto = random.choice([True, False, False]) # 33% de chance de ter desconto
                
                if tem_desconto:
                    percentual = random.randint(5, 35)
                    preco_final = preco_base * (1 - (percentual / 100))
                    desconto_texto = f" {percentual}% OFF"
                else:
                    preco_final = preco_base
                    desconto_texto = "Sem desconto"
                    
                preco_formatado = f"R$ {preco_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                
                #link de busca real no Mercado Livre!
                termo_busca = urllib.parse.quote(titulo_produto.lower().replace(" ", "-"))
                link_ml = f"https://lista.mercadolivre.com.br/{termo_busca}"
                
                lista_ofertas.append({
                    "Categoria": categoria,
                    "Produto": titulo_produto,
                    "Preço Final": preco_formatado,
                    "Desconto": desconto_texto,
                    "Link de Compra Real": link_ml
                })
            
            time.sleep(0.1)
            progresso.progress((i + 1) / len(categorias_hardware))
            
        status_texto.text("Banco de dados sincronizado e organizado!")

    # 2. Mostrando e Organizando o resultado na tela
    if lista_ofertas:
        st.success(f"Sistema Operante! {len(lista_ofertas)} peças de hardware processadas.")
        
        df = pd.DataFrame(lista_ofertas)
        
        categorias_encontradas = df["Categoria"].unique()
        
        # Criando o menu sanfona APENAS com o nome da categoria
        for cat in categorias_encontradas:
            quantidade_itens = len(df[df['Categoria'] == cat])
            
            with st.expander(f" {cat} ({quantidade_itens} anúncios)", expanded=False):
                
                df_filtrado = df[df["Categoria"] == cat].drop(columns=["Categoria"])
                
                st.dataframe(
                    df_filtrado,
                    column_config={
                        "Link de Compra Real": st.column_config.LinkColumn("🛒 Ver no Mercado Livre")
                    },
                    hide_index=True,
                    use_container_width=True
                )

#Contato
st.markdown("---")
st.markdown("**Desenvolvido por Davyd**")
st.markdown(" **Email:** davydeduardo97@gmail.com")
st.markdown(" **Telefone:** 41 99813-0514")