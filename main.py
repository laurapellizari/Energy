import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def case():

    st.markdown(f'# Dimensionamento de Sistema para Geração de Energia Solar Utilizando Aprendizado de Máquina')

    st.markdown(
        """
        ### Aplicação 

        O uso do aprendizado de máquina para resolver problemas da sociedade se mostra bastante presente nos dias de hoje. 
        Essa ferramenta foi desenvolvida a fim de demonstrar um caso de uso em que é estimado o consumo de energia elétrica
        e a irradiância solar para auxiliar em um dimensionamento eficaz e eficiente.
    """
    )

    st.markdown(f'# Análise histórica e Machine Learning')
    st.write(
        """
        Analisando os dados históricos do consumo de energia elétrica disponibilizados pela ONS (Operadpr Nacional do Sistema Elétrico) da região sudeste brasileira,
        observa - se uma leve tendência de alta e uma sazonalidade marcada por picos e vales. Os dados utilizados são de 2012 a 2020, na frequência mensal,  sendo 
        o ano de 2020 separado para dados de teste.

        Fonte: https://dados.ons.org.br/dataset/curva-carga/resource/3d93f874-c6a4-499e-9b6e-c16844607011?inner_span=True
"""
    )

    image = Image.open('images/st-consumo-historico.png')
    st.image(image, caption='Consumo mensal de energia elétrica MW')

    st.write(
        """
        Utilizando machine learning para aprender o fenômeno, podemos modela - lo e realizar uma estimativa de como será seu comportamento no ano de 2020.
        O resultado gráfico da estimativa é mostrado abaixo, em que observa - se que a máxima é 5.85e+15.
"""
    )

    image = Image.open('images/st-forecasting-energy.png')
    st.image(image, caption='Estimativa Consumo mensal de energia elétrica MW')

    st.write(
        """
        Da mesma forma, podemos analisar o comportamento histórico da irradiância solar disponibilizados pelo projeot The Power Project da NASA.
        Os dados utilizados são de 2004 a 2020, na frequência mensal, sendo o ano de 2020 separado para dados de teste.

        Fonte: https://power.larc.nasa.gov/
"""
    )

    image = Image.open('images/st-irrad-hist.png')
    st.image(image, caption='Irradiância solar em kW/m²')

    st.write(
        """
        Utilizando o mesmo algoritmo, podemos modelar e realizar uma estimativa para a irradiância solar na região sudeste para os próximos 
        12 meses, em que observa - se que a média 5.33 kW/m²/dia resultado gráfico da estimativa é mostrado abaixo.

"""
    )

    image = Image.open('images/st-forecasting-irrad.png')
    st.image(image, caption='Estimativa Irradiância média mensal kWh/m²')

    st.write(
        """
        ### Dimensionamento 
        
        Trazendo valor a estimativa gerada, podemos realizar o dimensionamento de placas solares, uma vez que o cálculo é dado por:\n
"""
    )
    st.latex(r'''
    Potência Total = \frac{Energia}{Tempo \times TD \times Irr} 
    ''')
    st.latex(r'''
    N = \frac
    {Potência
    Total}{Potência / Placa}
    ''')
    st.write("""
        Dessa forma, para exemplificar, utilizaremos como placa de estudo MAXPOWER CS6U-330P da CanadianSolar, a qual possui potência de 330W.\n        
"""
    )
    st.write(
        """
        Portanto, chegamos ao seguinte resultado:
"""
    )
    st.latex(r'''
    N = 57842
    ''')


def interative():

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write(
        """
        Uma vez que foi gerada a estimativa da irradiância média mensal da região sudeste para o ano de 2020,
        é possível dimensionar quantas placas seriam necessárias para a região sudeste, com base na potência fornecida 
        conforme uma placa escolhida pelo usuário.
"""
    )
    pot = st.text_input("Potência Média da Placa")

    if (st.button('Dimensionar')):
        pot_input = pot.title()
        result = round ((19087541 / int(pot_input)), 0)
        st.success(str(result) + ' placas')



page_names_to_funcs = {
    "Início": case,
    "Dimensionamento Online": interative
}

demo_name = st.sidebar.selectbox("Escolha uma página", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()