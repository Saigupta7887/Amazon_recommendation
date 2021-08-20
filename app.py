#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle
import pandas as pd
import os


dress_dict=pd.read_csv("python1.csv")
simalri=pd.read_csv("final.csv")





 

st.title('Sai Dress Recommendation System')
options = dress_dict['Dress_type']
index = st.selectbox("selectbox", range(len(options)), format_func=lambda x: options[x])


def recommend(index):
  csr=[]
  for i in simalri.iloc[index]:
     csr.append(dress_dict.iloc[i])
  return csr



if st.button('Show Recommendation'):
	recommendation=recommend(index)
	recommendation=pd.DataFrame(recommendation)
	count = 0



	for i in range(4):
	    for j in st.columns(3):

	        if count == 10:
	            break
	        with j:
	            st.image(recommendation['Image'].values[count])
	            st.markdown('<p style="text-align: center; font-weight:bold;">{}</p>'.format(recommendation['Dress_type'].values[count]),
	unsafe_allow_html=True)
	            st.markdown('<p style="text-align:center;">{}</p>'.format(recommendation['Brand'].values[count]),
	unsafe_allow_html=True)
	            st.markdown('<p style="text-align: center;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color:#565959;">₹{}</span></p>'.format(recommendation['Disc_price'].values[count],recommendation['Actual_price'].values[count]), unsafe_allow_html=True)
	            count += 1
		

