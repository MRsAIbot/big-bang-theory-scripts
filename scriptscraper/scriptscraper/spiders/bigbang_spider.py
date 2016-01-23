import scrapy

from scriptscraper.items import BigbangItem

class BigbangSpider(scrapy.Spider):
	"""docstring for BigbangSpider"""
	name = "bigbang"
	allowed_domains = ["bigbangtrans.wordpress.com"]
	start_urls = ["https://bigbangtrans.wordpress.com/"]

	def parse(self, response):
		episode_urls = response.xpath('//div[@id="pages-2"]/ul/li/a/@href').extract()
		for href in episode_urls:
			url = response.urljoin(href)
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = BigbangItem()
		item['episode'] = response.xpath('//h2[@class="title"]/text()').extract()[0]
		content = []
		for text in response.xpath('//div[@class="entrytext"]/p/descendant-or-self::text()').extract():
			content.append(text)
		item['content'] = content
		yield item
