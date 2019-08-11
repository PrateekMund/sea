#此应用专门解决
#选择困难症！！！
"晓东_sodo作品"
"邮箱：3481833891@qq.com 或 xiaodong_suodao@163.com"
"GiHub：XiaoDong23"

from random import randint
from easygui import msgbox,enterbox

list1 = []
msgbox('本产品专治选择困难症！！！','提示','明白')
#数量
while True:
    try:
        num = int(enterbox('请输入选择数量：'))
    except:
        msgbox('请输入正确数字！！！')
        continue
    else:
        break
#选项
for temp in range(1,num +1):   
    things = enterbox('请输入第' + str(temp) + '个选项：')
    list1.append(things)
#选择
#由于前面range函数加了一，所以这里再多减一
random = randint(0,num - 2)
answer = list1[random]
#结果
msgbox('选择是‘' + answer + '’','选择','关闭')
