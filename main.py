import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('streamlit 入門')

st.write('DataFrame')

img = Image.open('sample.jpg')
st.image(img,caption='momo',use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

left_column,right_column = st.columns(2)

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容woかく')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

button = left_column.button('右から無二文字をを表示')

if button:
    right_column.write("unko")


# text = st.sidebar.text_input('あなたのちんぽ')
# condition = st.sidebar.slider('あなたのちんぽの大きさは',0,100,50)

# st.dataframe(df.style.highlight_max(axis=0),width=400,height=400)

# st.area_chart(df)

# st.map(df)