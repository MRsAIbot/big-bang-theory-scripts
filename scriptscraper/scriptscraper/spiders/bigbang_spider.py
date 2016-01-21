import scrapy

from scriptscraper.items import BigbangItem

class BigbangSpider(scrapy.Spider):
	"""docstring for BigbangSpider"""
	name = "bigbang"
	allowed_domains = ["bigbangtrans.wordpress.com"]
	start_urls = ["https://bigbangtrans.wordpress.com/"]

	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		episode_urls = response.xpath('//div[@id="pages-2"]/ul/li/a/@href').extract()
		with open(filename, 'wb') as f:
			f.write(response.body)
		for href in episode_urls:
			url = response.urljoin(href)
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		pass
		item = BigbangItem()
