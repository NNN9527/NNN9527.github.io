import streamlit as st
import mysql.connector
import re
import urllib.request
from urllib import request

class MysqlGroup(object):
    def __init__(self, host, user, password, database, charset):
        self.mydb = mysql.connector.connect(host=host, user=user, port=3306, password=password, database=database,
                                            charset=charset, buffered=True)
        self.mycursor = self.mydb.cursor(buffered=True)

    def shebeiidbiao(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("select * from shebeiid ")
        self.shebeiid_name_list = [tuple[0] for tuple in self.mycursor.description]
        return len(self.shebeiid_name_list)

    def mysql_check(self, check_name, column_name, surface_name):
        self.i = 1
        self.counter1 = 0
        self.cjq = 0
        self.mycursor.execute("SELECT %s FROM %s" % (column_name, surface_name))
        self.myresult1 = self.mycursor.fetchall()
        for elem in self.myresult1:
            if isinstance(elem, tuple):
                self.counter1 += 1
            else:
                pass
        self.u1 = check_name
        for q1 in self.myresult1:
            self.nm = str(q1)
            if self.nm[2:-3] == str(self.u1):
                self.cjq = 1
                break
            else:
                self.i += 1
        return self.cjq

    def mysql_sid(self, check_name, column_name, surface_name):
        self.i = 1
        self.counter1 = 0
        self.cjq1 = 0
        self.mycursor.execute("SELECT %s FROM %s" % (column_name, surface_name))
        self.myresult1 = self.mycursor.fetchall()
        for elem in self.myresult1:
            if isinstance(elem, tuple):
                self.counter1 += 1
            else:
                pass
        self.u1 = check_name
        for q1 in self.myresult1:
            self.nm = str(q1)
            if self.nm[2:-3] == str(self.u1):
                self.cjq1 = 1
                break
            else:
                self.i += 1
        return self.i

    def mysql_increase(self, surface_name, column_name1, column_name2, parameter1, parameter2):  
        self.mycursor.execute(
            "INSERT INTO %s (%s, %s) VALUES ('%s', '%s')" % (surface_name,column_name1, column_name2, parameter1, parameter2))
        self.mydb.commit()
        
    def mysql_insert_null(self, surface_name, column_name1, column_name2):  
        self.mycursor.execute(
            "INSERT INTO %s (%s, %s) VALUES (Null, Null)" % (surface_name,column_name1, column_name2))
        self.mydb.commit()

    def mysql_check_novel(self, column_name, surface_name ,sid):
        self.mycursor.execute("SELECT %s FROM %s" % (column_name, surface_name))
        self.myresult1 = self.mycursor.fetchall()
        self.novel = ''
        self.m = 1
        for j in self.myresult1:
            if self.m == sid:
                self.novel = str(j)
                self.novel = self.novel[2:-3]
        return self.novel

    def mysql_up_novel(self, parameter1, parameter2, parameter3):
        self.mycursor.execute(
            "UPDATE novel SET %s = %s WHERE id = '%s' "%(parameter1, parameter2, parameter3))
        self.mydb.commit()

con1 = MysqlGroup('127.0.0.1', 'root', 'c798658613!', 'streamlifrontend', 'utf8')
con2 = MysqlGroup('127.0.0.1', 'root', 'c798658613!', 'streamlit_reptile', 'utf8')
shebeiid_number = con1.shebeiidbiao()


# 文本框输入
# st.sidebar.write('# 请输入用户名和密码')
st.sidebar.write('**用户名**')
zhanghao = st.sidebar.text_input('     ', '请输入邮箱', key=1)
st.sidebar.write('**密码**')
mima = st.sidebar.text_input('     ', '请输入密码', key=2)
# 两个按钮
left_column, right_column = st.sidebar.columns(2)
denglu = left_column.checkbox('登录')
with right_column:
    zhuche = st.checkbox('立即注册')
# 注册用文本框
if zhuche:
    st.sidebar.write('**账号**')
    zhuchezhanghao = st.sidebar.text_input('     ', '请输入邮箱', key=3)
    st.sidebar.write('**密码**')
    zhuchemima1 = st.sidebar.text_input('     ', '请输入注册的密码', key=4)
    st.sidebar.write('**重复密码**')
    zhuchemima2 = st.sidebar.text_input('     ', '(密码不能小于6位，且不能为纯数字）', key=5)
    zhuche2 = st.sidebar.button('注册')
else:
    pass


def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    else:
        return False


def validateEmail(email):
    if re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email) == None:
        return True
    else:
        return False


sid = 0


def register(username, password):  # 登录功能
    global sid
    sid = 0
    sid1 = 0
    cjq1 = con1.mysql_check(username, 'user', 'data')
    if denglu:
        if cjq1:
            st.sidebar.success("账号正确")
            sid = con1.mysql_sid(username, 'user', 'data')
            sid1 = con1.mysql_sid(password, 'password', 'data')
            if sid == sid1 and denglu:
                st.sidebar.success("密码正确")
                st.sidebar.success("登录成功")
                st.balloons()
                st.balloons()
                st.balloons()
            else:
                st.sidebar.error("密码错误")
        else:
            st.sidebar.error("账号错误")
    else:
        pass


register(zhanghao, mima)


def logon(zhanghao, mima, mimaagain):  # 注册功能
    cjq1 = 0
    if zhuche2:
        if is_contain_chinese(zhanghao) != 1 and validateEmail(zhanghao) != 1:
            cjq1 = con1.mysql_check(zhanghao, 'user', 'data')
            if cjq1 != 1:
                if is_contain_chinese(mima) == 1:
                    st.sidebar.error("密码不能含有中文")
                elif (str.isdigit(mima) == 1) or (len(mima) < 6):
                    st.sidebar.error("密码不能小于6位，且不能为纯数字")
                else:
                    if mima == mimaagain:
                         con1.mysql_increase('data','user', 'password',zhanghao,mima)
                         con1.mysql_insert_null('shebeiname','shebeiname1', 'shebeiname2')
                         con1.mysql_insert_null('shebeiid','shebeiid1', 'shebeiid2')
                         con2.mysql_insert_null('novel','name', 'chapter1')
                         st.sidebar.success("注册成功")
                    else:
                        st.sidebar.error("密码不一致")
            else:
                st.sidebar.error("账号已存在")
        else:
            st.sidebar.error("账号格式错误")


if zhuche:
    if zhuche2 and zhuchezhanghao != ('请输入邮箱'):
        logon(zhuchezhanghao, zhuchemima1, zhuchemima2)
    elif zhuche2 and zhuchezhanghao == ('请输入邮箱'):
        st.info('请输入邮箱')
    else:
        pass
else:
    pass

website = st.sidebar.text_input('     ', '请输入网址', key=1)
chapter1 = con2.mysql_check_novel('chapter1', 'novel', sid)
chapter2 = con2.mysql_check_novel('chapter2', 'novel', sid)



left_column, right_column = st.columns(2)
back_text = left_column.button('上一章')
with right_column:
    next_text  = st.button('下一章')
if next_text:
    con2.mysql_up_novel('chapter2', str(int(chapter2)+1), '1')
if back_text:
    con2.mysql_up_novel('chapter2', str(int(chapter2)-1), '1')
url = 'http://www.wm0.net/'+chapter1+'/'+chapter2+'.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('gbk')
pattern1 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<',re.S)
pattern2 = re.compile('<title>(.*?)</title>',re.S)
re_list = pattern1.findall(html)
sa= pattern2.findall(html)
num = len(re_list)
st.header(sa[0])
for i in range(num):
    st.info(re_list[i])








