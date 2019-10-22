import requests,os
from lxml import html
from pyquery import PyQuery as pq

class Spider:


    def __init__(self,name):
        # 初始化
        self.url = 'http://tieba.baidu.com/f?kw={}ie=utf-8&pn=0'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) ',
            'Cookie': 'BAIDUID=B0DE976DA9CCD49E2445943C03A13D9B:FG=1; BIDUPSID=B0DE976DA9CCD49E2445943C03A13D9B; PSTM=1571624046; H_PS_PSSID=1439_21083_29567_29221_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=6; TIEBA_USERTYPE=e79b9cfa3d1d3128bdb9b23b; TIEBAUID=cb23caae14130a0d384a57f1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1571645304; wise_device=0; bdshare_firstime=1571645369637; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1571645503'
        }

    def get_data(self,url):
        # 发送请求获取响应数据返回数据
        response = requests.get(url,headers=self.headers)
        return response.content

    def parse_list_page(self,data):
        # 提取当前页面所有的帖子详情页url和下一页的url
        # 获取doc对象
        doc = pq(data)
        # 提取详情页url
        lis = doc('#thread_list li').items()
        detail_url_list = []
        for li in lis:

            if li.find('a.j_th_tit '):
                url ='http://tieba.baidu.com' + li.find('a.j_th_tit ').attr('href')
                detail_url_list.append(url)
        # 获取下一页的url

        next_url = 'http:' + doc('a:contains("下一页>")').attr('href')

        return detail_url_list,next_url

    def parse_detail_page(self,url):
        data = self.get_data(url)
        doc = pq(data)
        image_url_list = []
        image_url_items = doc('cc img.BDE_Image').items()
        for url in image_url_items:
            image_url_list.append(url.attr('src'))
        print(image_url_list)
        return image_url_list

    def save_data(self,image_url_list):
        # 遍历列表发送请求下载图片
        if not os.path.exists('images'):
            os.makedirs('images')
        for url in image_url_list:
            filename = 'images/'+url.split('/')[-1]
            if filename.endswith('.jpg') or filename.endswith('.png'):
                data = self.get_data(url)

                with open(filename,'wb') as f:
                    f.write(data)
    def run(self):
        # 入口
        # 调用获取url信息的方法
        next_url = self.url
        while next_url:
            data = self.get_data(next_url)
            # 调用分析列表页的方法
            detail_url_list, next_url=self.parse_list_page(data)
            for url in detail_url_list:
                # 获取详情页,找图片,下载图片
                image_url_list = self.parse_detail_page(url)
                self.save_data(image_url_list)



if __name__ == '__main__':
    xiaohua = Spider('校花吧')
    xiaohua.run()

















