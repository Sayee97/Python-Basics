import pprint

msg='hi its a sunny day indeed'
dic={}
for i in msg:
    dic.setdefault(i,0)
    dic[i]=dic[i]+1
pprint.pprint(dic)
