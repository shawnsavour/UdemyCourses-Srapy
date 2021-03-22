import scrapy
from ..items import HowtoItem

class QuoteSpider(scrapy.Spider):
    name= 'UdemyCourses'
    start_urls= [
        'https://app.real.discount/free-courses/?page=1/'
    ]

    def parse(self, response):

        items = HowtoItem()

        courses = response.css(".col-sm-12.col-md-6.col-lg-4.col-xl-4")
        for course in courses:
            Icourse = course.css(".card-title::text").extract()
            Iexcerpt = course.css(".card-text::text").extract()
            Icategory = course.css(".card-cat::text").extract()
            Ibottomhtml = course.css(".card-bottom").extract()
            Iimgurl = course.css(".card-img-top::attr('src')").extract()
            Iurl = course.css("a::attr('href')").extract()
            
            items['course'] = Icourse
            items['excerpt'] = Iexcerpt
            items['category'] = Icategory
            items['bottomhtml'] = Ibottomhtml
            items['imgurl'] = Iimgurl
            items['url'] = Iurl

            yield items