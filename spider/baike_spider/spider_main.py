# coding:utf-8
import html_outputer
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HthmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        try:
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print "craw %d:%s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                print 45456
                if count == 1000:
                    break

                count = count + 1
        except:
            print "craw fail:"
        self.outputer.output_html()

if __name__ == "__main__":
    print "12345"
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
