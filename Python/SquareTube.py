x = [0,1,2,3,4,5,6,7,]
y = [0,1,2,3,]

a = 0
b = 0
c = 0
d = 0

L1 = int(input('请输入方管长度上限：'))
L2 = int(input('请输入方管长度下限：'))

if L1 < L2 :
    print('长度上限、下限搞反了,请重启！')
else:
    h = int(input('请输入第一个定尺：'))
    i = int(input('请输入第二个定尺：'))
    j = int(input('请输入第三个定尺：'))
    k = int(input('请输入第四个定尺：'))


    if h <= L1 and i <= L1 and j <= L1 and k <= L1 :
        for b in y:
            for a in x:
                for c in x:
                    for d in x:
                        #n = int(830*a+2240*b+880*c+662*d)
                        n = int(h*a+i*b+j*c+k*d)
                        #if 5600 < n <= 5760:
                        if L2 <= n <= L1:
                            print(a,'→',h,b,'→',i,c,'→',j,d,'→',k,'','总长：',n,)
                        #else:
                            #print('P',n)
    else:
        print('方管只能切断，不能拉长哟~')
