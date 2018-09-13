

from scrapy import Spider

class GitHubRankSpider(Spider):
    name = "gtrank"
    allowed_domains = ["githubrank.com"]
    start_urls = [
        "http://githubrank.com/"
    ]

    def parse(self, response):
        trs = response.xpath("//tr")
        for i in range(2, len(trs)):
            tds = trs[i].xpath(".//td")
            print(tds[0])
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

