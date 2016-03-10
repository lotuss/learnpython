# coding=utf-8
import re


# "."的使用
#"."是占位符，几个点就表示几个符号
# a="xy123"
# b=re.findall('x..',a)
# print b


#"*"的使用
#"*匹配其前面的东西出现的次"
# a='xyxy123'
# b=re.findall('x*',a)
# print b


#“？”的使用
# a="xy123"
# b=re.findall('x?',a)
# print b

seccret_code='hadkfalifexxIxxfasdjifia134xxlovexx23345sdfxxyouxx8dfse'

#".*贪心算法的使用"
b=re.findall('xx.*xx',seccret_code)
print b
#".*?婴儿少量多餐算法的实现"


c=re.findall('xx.*?xx',seccret_code)
print c

#使用括号与不使用括号的区别
d=re.findall('xx(.*?)xx',seccret_code)
print d

#换行情况
s='''fsdhxxhello
xxfghtxxworldxxfsd'''
f=re.findall('xx(.*?)xx',s,re.S)
print f

#search应用
s2="wegxxIxx123axxlovexxdef"
g=re.search('xx(.*?)xx123axx(.*?)xx',s2).group(2)
print g