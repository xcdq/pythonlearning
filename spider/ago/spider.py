from urllib import request
import re


class Spider():

    # url = 'http://txt.soushupan.xyz:18866/forum.php'
    url = 'http://txt.qiyehuangyewang.com:26974/forum.php'
    root_pattern = '<ul class="category_newlist">([\s\S]*?)</ul>'
    name_pattern = '标题: <strong>([\s\S]*?)</strong>'
    box_pattern = '<div class=".*?box">[\s\S]*?</div>'

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
        # print(htmls.decode('gbk'))
        with open('./text/shu.html', 'w', encoding='gbk') as fp:
            fp.write(htmls.decode('gbk'))
        box_html = re.findall(Spider.box_pattern, htmls.decode('gbk'))
        # root_html = re.findall(Spider.root_pattern, htmls.decode('gbk'))
        for x in box_html:
            name_box = re.findall('</span>(.*?)</h4>', x)
            name_html = re.findall(Spider.name_pattern, x)
            print(name_box[0])
            print()
            for y in name_html:
                print(y)
            print('>>>>>>>>>>>>>>\n\n\n\n')
        a = 1

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()
