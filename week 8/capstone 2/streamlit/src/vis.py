import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

df = pd.read_csv(r"C:\Users\nargi\Documents\coding temple\week 8\capstone 2\makeup.csv")
page = st.sidebar.selectbox(
    'Page',
    ('About', 'Brand Info', 'Visualizations', 'Summary')
)

if page == 'About':
    st.title(':lipstick: Welcome!')
    st.image('https://radicalcosmetics.com/wp-content/uploads/2022/03/Products-sample-kit-radical-cosmetics.png', width = 600)
    st.markdown('''
            I used the following tools to create this application:
             - Makeup API (http://makeup-api.herokuapp.com/api/v1/products.json)
             - Python
             - Pandas
             - Streamlit''')
    st.header('Here are the different pages of my application:')
    st.subheader('Brand Info')
    st.markdown('''Requests to select a brand and its products to view the product images. Also displays raw data if selected.
                
                Note: Some images my not populate''')
    st.subheader('Visualizations')
    st.write('Display visualizations of scatterplots, histograms, and bar charts')
    st.subheader('Summary')
    st.write('dhwjd')
 
                
if page == 'Brand Info':
    brands_ordered = sorted(df['brand'].unique(), key=str)
    st.title('Looking for a specific brand?')
    user_selected_brand = st.selectbox("Select a brand", options = brands_ordered)
    df_filtered = df[df['brand'] == user_selected_brand]
    if st.checkbox('Show me my raw data'):
        df_filtered
    user_selected_product = st.selectbox("Please select a product from the brand", options = list(df_filtered['name'].unique()))
    df_filtered_2 = df_filtered[df_filtered['name'] == user_selected_product]
    if st.checkbox("Want to see an image?"):
        image_url = df_filtered_2['image_link'].values[0]
        st.markdown(f"![]({image_url})")
        
        
if page == 'Visualizations':
    numeric_columns = list(df.select_dtypes(include = 'number'))
    numeric_columns.remove('id')
    st.title(':chart_with_upwards_trend: Visualizations')
    vis_to_use = ['scatterplot', 'histogram', 'bar chart']
    vis = st.selectbox("Select the type of visualization you want to see", options = vis_to_use)
    if vis == 'scatterplot': 
        x = st.selectbox('Select the column for the X-axis', options=numeric_columns)
        y = st.selectbox('Select the column for the Y-axis', options=numeric_columns)
        if x and y:
            try:
                st.plotly_chart(px.scatter(df, x, y, hover_data = [x,y,'brand', 'name']))
            except:
                st.error('Error')  
    if vis == 'histogram':
        x = st.selectbox('Select the column to view distribution', options=numeric_columns)
        if x:
            try:
                st.plotly_chart(px.histogram(df, x))
            except:
                st.error('Error')
    if vis == 'bar chart':
        x = st.selectbox('Select the column for the X-axis', options = list(df.select_dtypes(include = 'object')))
        try:
            st.plotly_chart(px.histogram(df, x=x).update_xaxes(categoryorder = "total descending"))
        except:
            st.error('Error')
            
            
if page == 'Summary':
    st.title('Summary')
    
        
        
