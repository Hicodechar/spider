# spider

该脚本文件有两个项目：SPatch 和 filtpath

## SPatch
主要代码在：[代码](https://github.com/Hicodechar/spider/blob/master/SPatch/SPatch/spiders/patch.py) 中。
SPatch用于对所有的[Linux patch网](https://patchwork.kernel.org/project/LKML/list/?page=1)进行爬取，查找所有patch中包含`tlb_`字段的所有patch连接；符合的连接保存在文件 **myurl** 中.对符合的网页下载到文件夹 **ans**中。
首先进入到文件夹：SPatch/SPatch/spiders
#### SPatch爬虫运行方式
```python
scrapy crawl patch
```


## filtpath
主要代码在：[代码](https://github.com/Hicodechar/spider/blob/master/filtpatch/filtpatch/spiders/filt.py) 中。
filtpath用于读取文件 **myurl** 中的连接地址，从相应的网页中找到包含字符串 **(空格)TLB(空格)** 的所有链接，链接保存在文件 **TLB_url**中，所有网页下载保存在文件夹 **ans**中。
#### filtpath爬虫运行方式
首先进入到文件夹：filtpatch/filtpatch/spiders
```python
scrapy crawl filt
```
