import scrapy
from scrapy_playwright.page import PageMethod

class FlipkartLaptopsSpider(scrapy.Spider):
    name = "flipkart_laptops"
    allowed_domains = ["flipkart.com"]

    def start_requests(self):
        url = "https://www.flipkart.com/search?q=laptops&page=1"
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "no-cache",
                "DNT": "1",  # Do Not Track header
            },
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", 'div.DOjaWF.gdgoEp', timeout=20000)
                ],
            }
        )

    def parse(self, response):
        # Extract laptop links
        links = response.xpath("//a[contains(@class, 'CGtC98')]/@href").getall()
        for link in links:
            full_url = response.urljoin(link)
            yield scrapy.Request(
                url=full_url,
                callback=self.parse_laptops,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "no-cache",
                    "DNT": "1",  # Do Not Track header
                },
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_selector", 'div.cPHDOP.col-12-12', timeout=20000)
                    ],
                },
            )

        # Handle pagination using the "next page" URL
        next_page = response.xpath("//a[contains(@class, '_1LKTO3') and contains(@rel, 'next')]/@href").get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Cache-Control": "no-cache",
                    "DNT": "1",  # Do Not Track header
                },
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_selector", 'div.DOjaWF.gdgoEp', timeout=20000)
                    ],
                },
            )

    def parse_laptops(self, response):
        yield {
            "Name": response.css('div.cPHDOP.col-12-12 span.VU-ZEz ::text').get(default='Not Available'),
            "Price": response.css('div.Nx9bqj CxhGGd ::text').get(default='Not Available')  # Correct selector for price
        }
