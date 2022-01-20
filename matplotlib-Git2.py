# from matplotlib import pyplot as plt
# from matplotlib import font_manager
#
# '''散点图'''
# my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")
# y_3=range(11,42)
# y_10=range(21,52)
#
# x_3=range(1,32)
# x_10=range(51,82)
#
# plt.figure(figsize=(15,8),dpi=80)
#
# plt.scatter(x_3,y_3,label="3月份")
# plt.scatter(x_10,y_10,label="10月份")
#
# _x=list(x_3)+list(x_10)
# _xtick_labels=["3月{}日".format(i) for i in x_3]
# _xtick_labels+=["10月{}日".format(i) for i in x_10]
# plt.xticks(_x[::3],_xtick_labels[::3],fontproperties=my_font,rotation=45)
#
# plt.xlabel("时间",fontproperties=my_font)
# plt.ylabel("温度",fontproperties=my_font)
# plt.title("标题",fontproperties=my_font)
#
# plt.legend(prop=my_font,loc="upper left")
#
# plt.show()

'''条形图'''
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
#
# my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")
# a=["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇"]
# b=[56.01,26.94,17.53,16.49]
# plt.figure(figsize=(15,8),dpi=80)
# '''横着条形图'''
# # plt.bar(range(len(a)),b,linewidth=0.3)
# # plt.xticks(range(len(a)),a,fontproperties=my_font,rotation=45)
# '''竖着条形图'''
# plt.barh(range(len(a)),b,height=0.3,color="orange")
# plt.yticks(range(len(a)),a,fontproperties=my_font,rotation=45)
#
# plt.show()
'''多条条形图'''
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

a=["圆形崛起","敦刻尔克","蜘蛛侠","战狼2"]
b_16=[15746,312,4497,319]
b_15=[12357,156,2045,168]
b_14=[2358,399,2358,362]

bar_width=0.2

x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]
x_16=[i+bar_width*2 for i in x_14]

plt.figure(figsize=(15,8),dpi=80)

plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

plt.legend(prop=my_font,loc="upper left")

plt.xticks(x_15,a,fontproperties=my_font)

plt.show()