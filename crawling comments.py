import time
import requests
import re

# 评论列表
commentlist = []
# 评论总数
commentnumber = 12691

# 起始的number会在页面刷新后发生更改
number = 1613708132614
# 默认起始的cursor为0
cursor = '0'
# 用于统计获得评论数
count = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
for i in range(commentnumber // 10):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + str(
        number)
    source = requests.get(url, headers=headers).content.decode()

    result = re.findall('"content":"(.*?)","up":', source, re.S)
    commentlist.append(result)

    # 下一页的cursor在当前页面中进行获取
    cursor = re.findall('"last":"(.*?)","', source, re.S)[0]
    # number+1代表下一页
    number += 1
    # 统计当前已获取评论数
    count += len(result)

# print(count)
# print(len(commentlist))
# print(commentlist)

# 将获取的评论写入txt文档
with open('评论.txt', "a", encoding="utf-8") as f:
    for list1 in commentlist:
        for comment in list1:
            f.write(comment)
            f.write('\n')
