from urllib import request
import re


class Spider():

    url = 'http://txt.soushupan.xyz:18866/forum.php'
    root_pattern = '<ul class="category_newlist">([\s\S]*?)</ul>'
    name_pattern = '标题: <strong>([\s\S]*?)</strong>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        # htmls = str(htmls, encoding='GDK')
        # print(htmls.decode('gbk'))
        # root_html = re.findall(Spider.root_pattern, htmls.decode('gbk'))
        # print(">>>>")
        # print(root_html)
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls.decode('gbk'))
        name_html = re.findall(Spider.name_pattern, htmls.decode('gbk'))
        for x in name_html:
            print(x)
        a = 1

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()
