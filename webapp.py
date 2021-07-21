# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:54:57 2021

@author: Purvanshu
"""

import streamlit as st
st.title('Simple streamlit App')
st.text('Type a number in the box')
n = st.number_input('number',step=1)
st.write(f'{n} + 1 ={n+1}')
s = st.text_input('type a name in the box')
st.write (f'hello {s}')