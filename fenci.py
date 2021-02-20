from selenium import webdriver
import time

url = "https://coral.qq.com/5963120294"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)
# 页面最大化
browser.maximize_window()
# while True:

browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")  # 滚动到底部

comment=browser.find_elements_by_xpath('//div[@class="comment-content J_CommentContent"]/text')
commentlist=[]
for item in comment:
    commentlist.append(item)
print(commentlist)
browser.find_element_by_xpath('//div[@class="comment-moreBtn J_shortMore"]').click()
time.sleep(1)
comment=browser.find_elements_by_xpath('//div[@class="comment-content J_CommentContent"]')
for item in comment:
    commentlist.append(item.text)
print(commentlist)