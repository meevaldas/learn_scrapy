import scrapy
from scrapy import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse_login(self, response):
        ret = FormRequest.from_response(response, formdata={"username":"ariel", "password":"password"})
        self.log("Sent:" + str(ret.body))
        return ret

    def start_requests(self):
        return [Request("http://quotes.toscrape.com/login", callback=self.parse_login)]

    def parse(self, response, **kwargs):
        pass
