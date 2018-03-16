# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup

class PatchSpider(scrapy.Spider):
    name = 'patch'
    # allowed_domains = ['patchwork.kernel.org']
    # start_urls = ['http://patchwork.kernel.org/project/LKML/list/?page=1']
    start_urls = []

    for i in range(1,3248):
        url_index = "http://patchwork.kernel.org/project/LKML/list/?page="+str(i)
        start_urls.append(url_index)
        with open("page_index", "a") as id:
            id.write(str(i)+"\n")
            id.close()
    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                lst = re.findall(r"patch/\d.*/", href)[0]
                url = 'http://patchwork.kernel.org/'+lst
                self.log("1111111111111111%s\n" % (url))
                yield scrapy.Request(url, callback=self.parse_patch)
            except:
                continue
    def parse_patch(self, response):
        html =  response.body
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('a')
        patchInfo = soup.find_all('div', attrs={'class':'patch'})
        tlbInfo = patchInfo[0].find_all(string=re.compile("tlb_"))
        if(len(tlbInfo)!=0):
            fname = response.url.split('/')[-2]
            fpath = "ans/"+fname
            with open(fpath, 'w') as f:
                f.write(response.body)
                f.close()
            with open("myurl", 'a') as uf:
                uf.write(response.url+"\n")
                uf.close()
        self.log(tlbInfo)
        self.log("444444444444444444444")
        #patchInfo = response.css('.patch')
        #self.log(patchInfo)
        #self.log("222222222222222222222222222222%s\n" % (patchInfo[0]))
       # tlbInfo = patchInfo[0].css(re.compile("blk_"))
       # if len(tlbInfo)==0:
       #     return
       # useful_url = response.url
       # self.log("the url is:%s" % (useful_url))
       # test = "hahhahhah"
       # yield test
        #yield useful_url


#    def parse(self, response):
#        fname = response.url.split('/')[-1]
#        with open(fname, 'wb') as f:
#            f.write(response.body)
#            self.log("saved file")

