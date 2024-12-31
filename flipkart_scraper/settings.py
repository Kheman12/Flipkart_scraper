# Scrapy settings for flipkart_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "flipkart_scraper"

SPIDER_MODULES = ["flipkart_scraper.spiders"]
NEWSPIDER_MODULE = "flipkart_scraper.spiders"
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",

}

# ScrapeOps Proxy Configuration

SCRAPEOPS_API_KEY = 'YOUR SCRAPEOPS API KEY'
PROXY_URL = f'http://scrapeops:{SCRAPEOPS_API_KEY}@residential-proxy.scrapeops.io:8181'
IMAGES_ENABLED = False



# Configure the Proxy URL for all requests
HTTPPROXY_ENABLED = True
HTTP_PROXY = PROXY_URL  # Use for all HTTP/HTTPS requests

PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 20000

# DOWNLOADER_MIDDLEWARES = {
#     'flipkart_scraper.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
#     'flipkart_scraper.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
#     'flipkart_scraper.middlewares.ScrapeOpsProxyMiddleware': 350,


# }


TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
DOWNLOAD_DELAY: 2
PLAYWRIGHT_BROWSER_TYPE = 'chromium'  # or 'firefox' or 'webkit'
PLAYWRIGHT_LAUNCH_OPTIONS = {
    'headless': False,
    'args': ['--disable-web-security'],
      # Optional: run in headless mode (without UI)
}
SCRAPEOPS_API_KEY = '852c514d-15ea-4afb-991e-53088aaaeab1'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_FAKE_HEADERS_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50
SCRAPEOPS_PROXY_ENABLED = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "flipkart_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "flipkart_scraper.middlewares.FlipkartScraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "flipkart_scraper.middlewares.FlipkartScraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "flipkart_scraper.pipelines.FlipkartScraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
