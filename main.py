import streamlit as st
import pandas as pd

st.title("Título do TFG")
st.markdown("Selecione ")


regressor = st.sidebar.selectbox("Select a Regression Algorithm",
                                 ['Linear Regression', 'K-Nearest Neighbors',
                                  'Random Forest', 'Gradient Boosting', 'XGBoost',
                                  'Support Vector Machines', 'Extra Trees'])

st.subheader('Total Energy Generation in ' +  ' (MW)')

forecast_horizon = st.sidebar.slider(label='Forecast Horizon (hours)',
                                     min_value=12, max_value=168, value=48)

window_length = st.sidebar.slider(label='Window Length',
                                  min_value=1, value=30)

df = pd.DataFrame(columns=['teste'])

# Plotting total energy generation for selected country
st.area_chart(df, use_container_width=False, width=800)

cols_renewable = ['Wind Onshore', 'Wind Offshore', 'Solar']

# Selecting the renewable energy columns,
# Only if they are available in the dataframe
df = df[df.columns & cols_renewable]

