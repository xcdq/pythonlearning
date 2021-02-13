import time

import requests
from lxml import etree

# 爬虫实战:爬取妹子图网的图片

# 第1页：https://www.meizitu.com/a/list_1_1.html
# 第2页：https://www.meizitu.com/a/list_1_2.html
# 第3页：https://www.meizitu.com/a/list_1_3.html
# 故可以推断出URL公式:url="https://www.meizitu.com/a/list_1_"+page_index+".html"
# 其中page_index指的是页码

page_index = 1  # 这里只下载了第一页相关的图片,如需下载更多可以使用for循环
# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}
# 组装请求的URL
url = "https://www.mzitu.com/a/list_1_" + str(page_index) + ".html"
# 发送请求,获取响应的HTML源代码
response = requests.get(url, headers=header).content
# 将源码字符串转换成HTML对象
html = etree.HTML(response)
# 通过xpath表达式提取页面中通往图片详情页面的超链接,返回一个列表
image_link_all_list = html.xpath(
    "//li[@class='wp-item']/div[@class='con']/div[@class='pic']/a/@href")
# 循环列表中的图片详情页面的超链接
for image_link in image_link_all_list:
    # 获取图片详情页面的HTML源码
    response_image_detail = requests.get(image_link).content
    # 将源码字符串转换成HTML对象
    html_image_detail = etree.HTML(response_image_detail)
    # 获取每张图片的下载链接
    image_link_detail_list = html_image_detail.xpath(
        "//div[@id='picture']//img/@src")
    # 获取每张图片的标题
    image_name_detail_list = html_image_detail.xpath(
        "//div[@id='picture']//img/@alt")
    # 条件判断
    if len(image_link_detail_list) == len(image_name_detail_list):
        # 循环图片下载链接
        for i in range(0, len(image_name_detail_list)):
            # 请求每张图片的数据
            data = requests.get(image_link_detail_list[i]).content
            # 下载提示
            print("正在下载图片" + image_name_detail_list[i] + ".jpg中......")
            # 将图片下载保存到电脑本地
            with open(r"C:/Users/Administrator/Pictures/images/" + image_name_detail_list[i] + ".jpg",
                      "wb") as file_object:
                # 写入数据
                file_object.write(data)
                print('OK')
                # 缓一缓
                time.sleep(0.5)
