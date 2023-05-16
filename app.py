import pandas as pd
import streamlit as st
import plotly.express as px

# Assuming your data is in a file named 'data.xlsx'
df = pd.read_excel('New results.xlsx')

st.markdown("""
    <style>
        # MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


        

st.title("Critical Raw Materials for Ireland")
st.subheader("Raw Material Analysis")



# Sidebar with material selection
material = st.sidebar.selectbox('Select a Material:', df['Material'].unique())

# Subset dataframe to selected material
df_material = df[df['Material'] == material]

# Display material data
col1, col2 = st.columns(2)
with col1:
    st.warning(f"Material: {df_material['Material'].values[0]}")
    st.header(f"State: {df_material['State'].values[0]}")
    st.info(f"Economic Importance (EI) = {df_material['EI'].values[0]:.2f}")
    st.info(f"Supply Risk (SR) = {df_material['SR'].values[0]:.2f}")





logo = 'logo.jpg'

# Load material shares data
df_shares = pd.read_excel('shares.xlsx', sheet_name=material)

# Create pie charts
fig1 = px.pie(df_shares, values='Shares', names='Country-Stage I', title='Material Global Supply Stage I - Ores and concentrations')
fig2 = px.pie(df_shares, values='Shares 2', names='Country-Stage II', title='Material Global Supply II - Refining and Production')

# Display pie charts
st.plotly_chart(fig1)
st.plotly_chart(fig2)

# Display images at the bottom
st.image(logo)


# Your code here...

# Footer
st.markdown('---')  # Optional, adds a horizontal line for aesthetics
st.write("""
This project is funded under the EPA Research Programme 2021-2030 and co-funded by Geological Survey Ireland. 
The EPA Research Programme is a Government of Ireland initiative funded by the Department of the Environment, Climate and Communications.
""")
