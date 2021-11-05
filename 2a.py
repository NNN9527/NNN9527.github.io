import streamlit as st
import pandas as pd
import numpy as np
import time
import streamlit.components.v1 as components




def shigongjidi():
  st.title('Welcome to 摸鱼圣地！！！')
  st.date_input('某天')
  st.time_input('某时')



   # Add a placeholder 
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range(3):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

  st.write('欢迎来到跑路天堂9527！！！！！！')
  for i in range(3):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
  
  st.write('早上好，打工人！！！')
  for i in range(3):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
  st.write('三点几啦，该起床读书啦！！！')


  st.button('点我开启时间循环！！！！！')

  '做然啊做，老板不会心疼你啦，摸鱼先'


  st.title('9527NNN帅！')
  st.write('9527NNN大帅比！！')
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

  st.markdown('**9527NNN _really_ cool**.')

  components.iframe("https://nnn9527.github.io"
                  ,height=600,width=400, )

  code = '''def hello():
  ...     print("Hello, Streamlit!")'''
  st.code(code, language='python')

  st.markdown('### 三次方计算器 :sunglasses:')
  x = st.slider('输入一个数字')
  st.write(x, '的2次方为：', x**2)
  st.markdown('> Streamlit挺好用 :+1:')





def sidebar():#左边菜单控制栏0
    df_parameters = pd.DataFrame({'function': ['-','游戏','小说','视频'],'tool': ['-','半小时','一小时','自定义']})
    select_parameters=[]
    option_function = '游戏'
    option_function = '小说'
    option_function = '视频'
    option_time = '自定义'
    option_time = '半小时'
    option_time = '一小时'
    option_time = '      '
    
    option_function = st.sidebar.selectbox('请选择娱乐',df_parameters['function'])
    select_parameters.append(option_function)
    option_time = st.sidebar.selectbox('请选择工具',df_parameters['tool']) 

    if option_function =='游戏':
          '游戏'
    else:pass
    if option_function =='小说':
         components.iframe("https://m.ddyueshu.com/wapbook/11508_655702269_3.html"
                  ,height=3800,width=300, )
    else:pass
    if option_function =='视频':
         components.iframe("https://www.bilibili.com/video/BV1i5411K7cY?spm_id_from=333.851.b_7265636f6d6d656e64.1"
                  ,height=600,width=700, )
    else:pass

    if option_time =='半小时':
          '半小时'
    else:pass
    if option_time =='一小时':
    
          '一小时'
    else:pass
    if option_time =='自定义':
      zidingyi1_time= st.sidebar.text_input('     ', '请输入视频时间/小时')
      zidingyi2_time= st.sidebar.text_input('     ', '请输入视频时间/分钟')
      if zidingyi1_time != ('请输入视频时间/小时') and zidingyi2_time != ('请输入视频时间/分钟'):
       st.sidebar.write('游戏始视频')
       st.sidebar.write(zidingyi1_time,'小时')
       st.sidebar.write(zidingyi2_time,'分钟')
      else:pass
    else:pass
    left_column, right_column = st.sidebar.beta_columns(2)
    wenghao=left_column.button('????')
    with right_column:
     zaxiang=st.button('杂项')
     if wenghao:
        '??????'
    if zaxiang:
         shigongjidi()
    left_column, right_column = st.sidebar.beta_columns(2)
    guanyu=left_column.button('关于')
    with right_column:
     bangzhu=st.button('帮助')
     if guanyu:
      st.write("作者是9527NNN")
     else:pass
     if bangzhu:
      st.write("这里没有任何可以帮您的地方")
    return select_parameters

sidebar()















