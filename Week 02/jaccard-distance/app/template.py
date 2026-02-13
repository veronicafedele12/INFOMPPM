import streamlit as st
import pandas

def tile_item(column, item: pandas.Series):
  with column:
    st.image(item['Image-URL-M'], width='stretch')
    st.caption(item['Book-Title'])

def recommendations(df: pandas.DataFrame):

  # check the number of items
  nbr_items = df.shape[0]

  if nbr_items != 0:    

    # create columns with the corresponding number of items
    columns = st.columns(nbr_items)

    # apply tile_item to each column-item tuple (created with python 'zip')
    for column, (_, item) in zip(columns, df.iterrows()):
      tile_item(column, item)
