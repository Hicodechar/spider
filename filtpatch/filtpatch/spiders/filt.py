# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup


class FiltSpider(scrapy.Spider):
    name = 'filt'

    with open("myurl", "rt") as f:
        # start_urls = [url.strip() for url in f.readlines()]
        start_urls = []
        for line in f.readlines():
            l = line.strip()
            start_urls.append(l)
    # start_urls = ['http://patchwork.kernel.org/']

    def parse(self, response):
        html = response.body
        # self.log(self.start_urls)
        self.log("1111111111111111111111111111")
        # self.log(html)

        self.log("2222222222222222222222222222")
        soup = BeautifulSoup(html, 'html.parser')
        tlbInfo = soup.find_all(string=re.compile("\sTLB\s"))
            # tlbInfo = commentInfo[idx].find_all(string='TLB')
        if(len(tlbInfo)!=0):
            fname = response.url.split('/')[-2]
            fpath = "ans/"+fname+".html"
            with open(fpath, 'w') as f:
                f.write(response.body.decode("utf-8"))
                f.close()
            with open("TLB_url", 'a') as Tf:
                Tf.write(response.url+'\n')
                Tf.close()
