import scrapy


class CovidScrapySpider(scrapy.Spider):
    name = 'covid_scrapy'
    allowed_domains = ['https://www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/']

    def parse(self, response):
        for row in response.xpath("//tr"):
            name = row.xpath(".//td[1]/text()").get()
            number_of_cases = row.xpath(".//td[2]/text()").get()
            number_of_deaths = row.xpath(".//td[3]/text()").get()
            regions = row.xpath(".//td[4]/text()").get()

            yield {
                'Country name': name,
                'Number of cases': number_of_cases,
                'Number of deaths': number_of_deaths,
                'Region': regions
            }