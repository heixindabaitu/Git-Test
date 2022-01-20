# import matplotlib.pyplot as plt
#
# '''figure 图形的意思 figsize大小 dpi清晰度'''
# fig = plt.figure(figsize=(15,6),dpi=80)
#
# x=range(2,26,2)
# y=[15,13,14.5,17,20,25,26,26,24,22,18,15]
# '''绘制图形'''
# plt.plot(x,y)
#
# '''X Y轴刻度'''
# _xtick_labels = [i/2 for i in range(2,49)]
# # plt.xticks(range(2,25))
#
# plt.xticks(_xtick_labels[::3])
# plt.yticks(range(min(y),max(y)+5))
#
#
#
# '''保存图片到当前目录下  .png图片的格式
#                      .svg矢量图格式
# '''
# # plt.savefig("./sig_size.png")
#
# '''展示图形'''
# plt.show()


# from matplotlib import pyplot as plt
# import random
# import matplotlib
# from matplotlib import font_manager
# # 字体设置
# my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")
#
#
#
#
#
# x=range(0,120)
# y=[random.randint(20,35) for i in range(120)]
#
# plt.figure(figsize=(15,6),dpi=80)
#
# plt.plot(x,y)
#
# # 调整x轴刻度
# _xtick_labels = ["10点{}分".format(i) for i in range(60)]
# _xtick_labels += ["11点{}分".format(i) for i in range(60)]
# # 取相同步长
# plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)
#
# # 添加描述信息
# plt.xlabel("时间",fontproperties=my_font)
# plt.ylabel("温度",fontproperties=my_font)
# plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)
#
# plt.show()

'''折线图'''

from matplotlib import pyplot as plt
from matplotlib import font_manager
# 字体设置
my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

y_1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x=range(11,31)

plt.figure(figsize=(15,6),dpi=80)

plt.plot(x,y_1,label="自己",color="orange",linestyle=":",linewidth="5")
plt.plot(x,y_2,label="同桌",color="cyan",)

_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)

# 绘制网格
plt.grid(alpha = 0.4)

# 添加图例
plt.legend(prop=my_font,loc="upper left")

# 展示
plt.show()

#First Git Push