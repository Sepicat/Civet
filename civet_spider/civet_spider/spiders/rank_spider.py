

from scrapy import Spider

class GitHubRankSpider(Spider):
    name = "gtrank"
    allowed_domains = ["githubrank.com"]
    start_urls = [
        "http://githubrank.com/"
    ]

    def parse(self, response):
        trs = response.xpath("//tr")

        def fetch_text(td):
            vals = td.xpath(".//text()").extract()
            return vals[0] if len(vals) > 0 else ""

        def fetch_img(td):
            vals = td.xpath(".//img/@src").extract()
            return vals[0] if len(vals) > 0 else ""

        for i in range(2, len(trs)):
            tds = trs[i].xpath(".//td")
            if len(tds) == 9:
                vals = [fetch_text(tds[j]) if j != 1 else fetch_img(tds[j]) for j in range(0, 9)]
                print(vals)
                print("")


