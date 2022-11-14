import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def case():

    st.write("#Título do TFG")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Pequena explicação

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        Analisando os dados históricos do consumo de energia elétrica disponibilizados pela ONS (Operadpr Nacional do Sistema Elétrico) da região sudeste brasileira,
        observa - se uma leve tendência de alta e uma sazonalidade marcada por picos e vales. Os dados utilizados são de 2003 a 2020, na frequência mensal.

        Fonte: https://dados.ons.org.br/dataset/curva-carga/resource/3d93f874-c6a4-499e-9b6e-c16844607011?inner_span=True
"""
    )

    # image = Image.open('jetbrains://pycharm/navigate/reference?project=Energy&path=venv/images/consumo_histórico.png')
    # st.image(image, caption='Consumo mensal de energia elétrica')

    st.write(
        """
        Utilizando machine learning para aprender o fenômeno, podemos modela - lo e realizar uma estimativa de como será seu comportamento no ano de 2020.
        O resultado gráfico da estimativa é mostrado abaixo, em que observa - se que a máxima é X.
"""
    )

    # image = Image.open('IMAGEM DO FORECAST')
    # st.image(image, caption='Consumo mensal de energia elétrica')

    st.write(
        """
        Da mesma forma, podemos analisar o comportamento histórico da irradiância solar disponibilizados pelo projeot The Power Project da NASA.
        Os dados utilizados são de 2004 a 2020, na frequência mensal.

        Fonte: https://power.larc.nasa.gov/
"""
    )

    # image = Image.open('IMAGEM DO FORECAST')
    # st.image(image, caption='Consumo mensal de energia elétrica')

    st.write(
        """
        Utilizando o mesmo algoritmo, podemos modelar e realizar uma estimativa para a irradiância solar na região sudeste para os próximos 
        12 meses. O resultado gráfico da estimativa é mostrado abaixo.

"""
    )

    # image = Image.open('IMAGEM DO FORECAST')
    # st.image(image, caption='Consumo mensal de energia elétrica')

    st.write(
        """
        Trazendo valor a estimativa gerada, podemos realizar o dimensionamento de placas solares, uma vez que o cálculo é dado por:\n

        Potência Média da Placa x Irradiância Média Mensal x 20% Perda x 30 Dias\n

        Sendo 20% a perda padrão por placa, em condições STC.\n

        Dessa forma, para exemplificar, utilizaremos como placa de estudo MAXPOWER CS6U-330P da CanadianSolar, a qual possui potência de 330W.\n        
"""
    )

    df_padrao = pd.DataFrame({'Mês': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'Potência-Média-Placa (W)': 330,
                              'Irradiância-Média-Mensal (kWh/m²)': 'X'})
    st.dataframe(df_padrao)

    st.write(
        """
        Aplicando a fórmula temos o seguinte resultado:  
"""
    )
    df_energia_gerada = pd.DataFrame({'Mês': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'Potência-Média-Placa (W)': 330,
                                      'Irradiância-Média-Mensal (kWh/m²)': 'X',
                                      'Energia-Por-Placa': [122, 234, 255, 123, 543, 356, 332, 543, 123, 453, 235,
                                                            433]})
    st.dataframe(df_energia_gerada)
    st.line_chart(df_energia_gerada, x='Mês', y='Energia-Por-Placa')

    st.write(
        """
          Estimando o número de placas, podemos aplicar pela estimativa máxima do consumo elétrica ou a partir da mínima irradiância estimativa,
          visto que  são os dois casos extremos.\n 
          Dessa forma, para a o caso de máxima de consumo temos:\n

          E para o caso de mínima irradiância:\n 
"""
    )


def interative():

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write(
        """
        This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )



page_names_to_funcs = {
    "Home": case,
    "Mapping Demo": interative
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()