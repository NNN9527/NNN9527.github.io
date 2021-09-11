import streamlit as st
import pandas as pd
import numpy as np

import time

import streamlit.components.v1 as components





st.title('Welcome to 摸鱼圣地！！！')

st.date_input('某天')
st.time_input('某时')

uploaded_file = st.file_uploader('我们跑路啦！！！！！', type="png")


color = st.color_picker('选择心动色彩', '#64C3FB')


# Add a placeholder 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(3):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.write('欢迎来到跑路天堂9527！！！！！！', color)
for i in range(3):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
  
st.write('早上好，打工人！！！', color)
for i in range(3):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
st.write('三点几啦，该起床读书啦！！！', color)


st.button('点我开启时间循环！！！！！')

'做然啊做，老板不会心疼你啦，摸鱼先'
# embed streamlit docs in a streamlit app
components.iframe("https://www.bilibili.com/video/BV1i5411K7cY?spm_id_from=333.851.b_7265636f6d6d656e64.1"
                  ,height=600,width=730, )

st.title('帅！')
st.write('大帅比！！')
st.write("下面是一个表格的尝试:")
st.write(pd.DataFrame({
    '520': [1, 3, 1,4],
    '9527': [7, 0, 8, 6]
}))
"""
# just a magit
Here's NO ONE :
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write('三呢？？？？？？？？？')

st.write('为啥加不了超霸气的巨大字体')
st.write('**我也不知道什么原理的地图**')
st.write('为啥加粗时灵时不灵')


if st.checkbox('看不到我！！！！！'):
 11
else:pass

columns=['a', 'b', 'c']
option = st.selectbox(
    '《豆腐吃咸的还是甜的？》',
     df['second column']
    )
'甜党天下无敌！！！！！！！', option


genre = st.radio( "《豆腐吃咸的还是甜的？》",
('甜的', '甜的', '咸的'))
if genre == '甜的':
 st.write('甜党天下第一！！！！！！！')
else:
 st.write("亚希拉你")

st.markdown('** _really_ cool**.')

components.iframe("https://nnn9527.github.io"
                  ,height=600,width=730, )

st.balloons()
st.balloons()
st.balloons()


code = '''def hello():
...     print("Hello, Streamlit!")'''
st.code(code, language='python')


def sidebar():
    df_parameters = pd.DataFrame({'industry': ['-','开','关'],'name': ['-','A','B'],'time': ['-','5天','7天']})
    select_parameters=[]
    option_industry = '-'
    option_name = '-'
    option_time = '-'
    
    option_industry = st.sidebar.selectbox('请选择股票行业',df_parameters['industry'])
    if option_industry != '-':
        select_parameters.append(option_industry)
        option_name = st.sidebar.selectbox('请选择股票名称',df_parameters['name'])
    else:
        pass
    
    if option_name!= '-':
        select_parameters.append(option_name)
        option_time = st.sidebar.selectbox('请选择时间窗口',df_parameters['time'])
    else:
        pass
        
    if option_time!= '-':
        select_parameters.append(option_time)
        version_option=st.sidebar.selectbox('选择历史版本：',('-','版本1', '版本2', '版本3'))
        st.sidebar.button('切换页面')
        st.sidebar.button('更新参数')
        
    return select_parameters

sidebar=sidebar()

st.markdown('### 三次方计算器 :sunglasses:')
x = st.slider('输入一个数字')
st.write(x, '的2次方为：', x**2)
st.markdown('> Streamlit挺好用 :+1:')
















