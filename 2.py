import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas

import cv2
import numpy as np
import streamlit as st

import time

import streamlit as st
import streamlit.components.v1 as components



genre = st.radio( "What's your favorite movie genre",
('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
 st.write('You selected comedy.')
else:
 st.write("You didn't select comedy.")



st.title('Welcome to 摸鱼圣地！！！')

st.date_input('某天')
st.time_input('某时')

uploaded_file = st.file_uploader('我们跑路啦！！！！！', type="png")

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="BGR")

from PIL import Image
image = Image.open('4.png')
st.image(image, caption='跑路进行时~~~~~',
use_column_width=True)


from PIL import Image
image = Image.open('3.png')
st.image(image, caption='跑路完毕乌拉！！！',
use_column_width=True)


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

st.title('，帅！')
st.write('，大帅比！！')
st.write("下面是一个表格的尝试:")
st.write(pandas.DataFrame({
    '520': [1, 3, 1,4],
    '9527': [7, 0, 8, 6]
}))
"""
# just a magit
Here's NO ONE :
"""
df = pandas.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write('三呢？？？？？？？？？')

st.write('为啥加不了超霸气的巨大字体')
st.write('**我也不知道什么原理的地图**')
st.write('为啥加粗时灵时不灵')

map_data = pandas.DataFrame(
    numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


if st.checkbox('看不到我！！！！！'):
    chart_data = pandas.DataFrame(
       numpy.random.randn(40, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

option = st.selectbox(
    '《豆腐吃咸的还是甜的？》',
     df['second column']
    )
'甜党天下无敌！！！！！！！', option


genre = st.radio( "《豆腐吃咸的还是甜的？》",
('甜的', '甜的', '甜的'))
if genre == '甜的':
 st.write('甜党天下第一！！！！！！！')
else:
 st.write("咸党滚出克")

st.markdown('** _really_ cool**.')


