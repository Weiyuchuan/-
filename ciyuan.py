import matplotlib.pyplot as plt
from wordcloud import WordCloud


#1导入笼罩图
back_img=plt.imread(r'D:\Documents\Tencent Files\122089717\FileRecv\图4.jpg')

#打开生成词云的文档
f=open(r'D:\Documents\Tencent Files\122089717\FileRecv\danmu2.txt','r',encoding='utf-8').read()

#3生成词云

wordcloud=WordCloud(
    # background_color='white', #指定
    mask = back_img,  #背景图
    font_path =r'D:\Documents\Tencent Files\122089717\FileRecv\ZhengQingKeJingYaTi-ShouBan-2.ttf',
).generate(f)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
