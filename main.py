import streamlit as st
import qrcode
import pyzbar.pyzbar as pyzbar
import numpy as np
from PIL import Image
import cv2

# -*- coding:utf-8 -*-

import streamlit as st
import qrcode
import pyzbar.pyzbar as pyzbar
import numpy as np
from PIL import Image
import cv2

# -*- coding:utf-8 -*-

QR_Code_generate = st.sidebar.checkbox('生成二维码')
QR_Code_analysis = st.sidebar.checkbox('解析二维码')
if QR_Code_generate:
    data = st.text_input('     ', '请输入需要编码的信息', key=1)
    generate = st.button('生成')
    if generate and data != '请输入需要编码的信息':
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('图片.png')
        image = Image.open('图片.png')
        st.image(image, caption='跑路进行时~~~~~',
        use_column_width=200)
        with open('图片.png', "rb") as file:
                 btn = st.download_button(
                 label="下载",
                 data=file,
                 file_name="二维码图片.png",
                 mime="image/png"
                 )
                 
decode_result = 0
def decodeDisplay(image):#二维码解码
    global decode_result
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (225, 225, 225), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (225, 225, 225), 2)
        decode_result = ("{}".format(barcodeData))

    return image

if QR_Code_analysis:
    """
    # 请上传二维码图片
    """
    uploaded_file = st.file_uploader('  ', type=['png', 'jpg'] )
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes,1)
        st.image(opencv_image, channels="BGR",output_format='PNG')
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        decodeDisplay(gray)
        st.info(decode_result)

        

