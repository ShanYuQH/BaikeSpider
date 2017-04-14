# -*- coding:utf-8 -*-
from baike_spider import html_down, html_outputer,\
 html_parser, url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        # 初始化URL管理器
        self.downloader = html_down.HtmlDownloader()
        # 初始化HTML下载器
        self.parser = html_parser.HtmlParser()
        # 初始化HTML解析器
        self.outputer = html_outputer.HtmlOutputer()
        # 初始化HTML输出器

    def crawl(self, root_url):
        count = 1
        # 爬取计数
        self.urls.add_new_url(root_url)
        # 将入口URL添加进管理器
        # 若URL池不为空则进行爬取
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            # 获取要下载的URL
            print 'crawl %d : %s' % (count, new_url)
            # 打印正在爬取第几个页面及其URL
            html_cont = self.downloader.download(new_url)
            # 下载页面
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            # 获取新的URL列表和页面数据
            self.urls.add_new_urls(new_urls)
            # 将新的URL列表添加进管理器
            self.outputer.collect_data(new_data)
            # 收集数据

            if count == 500:
                break
            count += 1

            # except:
            #     print 'Crawl Failed'

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
