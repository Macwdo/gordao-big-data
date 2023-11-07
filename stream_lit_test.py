import pandas as pd
import streamlit as st
import plotly.express as px



class DataUtils:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.__dataframe = dataframe
        pass
    
    def count_chart(self, product_type: str, chart_color: str) -> None:
        df = self.__dataframe
        product_df = df[df['tipo_de_produto'] == product_type]
        product_counter = product_df['produto'].value_counts()
        st.bar_chart(product_counter, color=chart_color)

    def total_received_by_product(self, product_type: str):
        df = self.__dataframe
        product_df = df[df['tipo_de_produto'] == product_type]
        return product_df["valor"].sum()

    def most_sold(self, product_type: str | None = None) -> str:
        df = self.__dataframe

        if product_type is None:
            product_counter = df['produto'].value_counts()
            most_sold = product_counter.idxmax()
            return most_sold

        product_df = df[df['tipo_de_produto'] == product_type]
        product_counter = product_df['produto'].value_counts()

        most_sold = product_counter.idxmax()
        return most_sold
    
    def write_snippet(self, product_type: str, label: str, chart_color: str) -> str:
        st.write(f"### {label}")
        most_sold = self.most_sold(f"{product_type}")
        total_received = self.total_received_by_product(f"{product_type}")
        st.write(f'##### Sabor mais vendido {most_sold.title()} e um total arrecadado de R${total_received}')
        self.count_chart(f"{product_type}", chart_color)
        st.write("*****")

    def date_sorted_chart(self) -> None:
        df = self.__dataframe
        df['data_da_venda'] = pd.to_datetime(df['data_da_venda'], format='%d/%m/%Y')

        date_sales = df.groupby('data_da_venda').size().reset_index(name='quantidade_vendida')

        fig = px.bar(
            date_sales,
            x='data_da_venda',
            y='quantidade_vendida',
            labels={'quantidade_vendida': 'Quantidade Vendida', 'data_da_venda': "Data da venda"},
            color_discrete_sequence=['purple']     
        )
        
        st.plotly_chart(fig, use_container_width=True)

    def run(self):
        st.write("# Analise de dados 🎲")
        st.write("*****")

        st.write("## Bibliotecas usadas 📚")
        st.code("""
            matplotlib==3.8.1
            numpy==1.26.1
            pandas==2.1.2
            plotly==5.18.0
            streamlit==1.28.1
        """)

        st.write("## Como importamos o dados ⬇️")
        st.code("import pandas as pd\n\n\ndf = pd.read_json('./data.json')")


        st.write(self.__dataframe)


        st.write("*****")
        st.write("## Produtos vendidos em ordem de tempo ⏳")

        self.date_sorted_chart()

        st.code("""
    def date_sorted_chart(self) -> None:
        df = self.__dataframe
        df['data_da_venda'] = pd.to_datetime(df['data_da_venda'], format='%d/%m/%Y')

        date_sales = df.groupby('data_da_venda').size().reset_index(name='quantidade_vendida')

        fig = px.bar(
            date_sales,
            x='data_da_venda',
            y='quantidade_vendida',
            labels={'quantidade_vendida': 'Quantidade Vendida', 'data_da_venda': "Data da venda"},
            color_discrete_sequence=['purple']     
        )
        
        st.plotly_chart(fig, use_container_width=True)
    """)

        st.write("*****")

        st.write("## Vendas por tipo de produto")

        st.write("*****")

        self.write_snippet("tapiocas", "Tapiocas 🥟", "#9e964d")
        self.write_snippet("bebidas", "Bebidas 🍺", "#a32a26")
        self.write_snippet("hamburguers", "Hamburguers 🍔", "#d19f08")

        st.code("""
                 
    def write_snippet(self, product_type: str, label: str, chart_color: str) -> str:
        st.write(f"### {label}")
        most_sold = self.most_sold(f"{product_type}")
        total_received = self.total_received_by_product(f"{product_type}")
        st.write(f'##### Sabor mais vendido {most_sold.title()} e um total arrecadado de R${total_received}')
        self.count_chart(f"{product_type}", chart_color)
        st.write("*****")

        """)

        total = self.total_received_by_product("tapiocas") + self.total_received_by_product("bebidas") + self.total_received_by_product("hamburguers")
        most_sold = self.most_sold()

        st.write("# Resumo 📉")
        st.write(f"""
            #### Tivemos um Total arrecadado de R${total}!\n
            #### O produto mais vendido entre todas categorias foi {most_sold.title()}\n
            *****
            #### Produtos mais vendidos de sua categoria
            Bebida | Tapioca | Hamburguer
            :---------: | :------: | :-------:
            {self.most_sold('bebidas').title()} | {self.most_sold('tapiocas').title()} | {self.most_sold('hamburguers').title()}
        """)

        st.write("# Acabou !")
        st.write("*****")
        st.link_button("Link do repositorio", "https://github.com/Macwdo/gordao-big-data")
        st.write("Link da aplicação.")
        st.image("./static-9f922a9cdf4ff88ab32cee5bc2fd82ce.svg")


if __name__ == "__main__":
    df = pd.read_json("./data.json")
    utils = DataUtils(df)
    utils.run()

