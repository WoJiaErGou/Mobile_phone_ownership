import scrapy
import json
from bs4 import BeautifulSoup as bs
from haoma.settings import unicom,mobile1,mobile2,telecom
from haoma.items import HaomaItem
'''
中国联通号码：130、131、132、145（无线上网卡）、155、156、185（iPhone5上市后开放）、186、176（4G号段）、175（2015年9月10日正式启用，暂只对北京、上海和广东投放办理）
中国移动号码：134、135、136、137、138、139、147（无线上网卡）、150、151、152、157、158、159、182、183、187、188、178
中国电信号码：133、153、180、181、189、177、173、149
虚拟运营商：170、1718、1719
unicom = ['130','131','132','145','155','156','185','186','176','175','166']
mobile = ['134','135','136','137','138','147','150','151','152','157','158','159','182','183','187','188','178','198']
telecom = ['133','153','180','181','189','177','173','149','199']
'''
class HMspider(scrapy.Spider):
    name = 'haoma1'
    def start_requests(self):
        #分运营商获取号码归属地
        for each in telecom:
            for i in range(0,10000):
                head = each
                middle = str(i).zfill(4)
                number = head + middle +'0000'
                item = HaomaItem(number=number)
                headers = {
                    'Host': 'www.ip138.com:8080',
                    'Referer': 'http://www.ip138.com:8080/search.asp?action=mobile&mobile=%s' % number,
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
                }
                re_url = 'http://www.ip138.com:8080/search.asp?action=mobile&mobile=' + number
                # url = 'http://www.ip138.com:8080/search.asp?action=mobile&mobile=13300040000'
                yield scrapy.Request(url=re_url,callback=self.parse,meta={'item':item},headers=headers)
    def parse(self, response):
        item = response.meta['item']
        number = item['number']
        soup = bs(response.text, 'lxml')
        # {"Mobile":"13329470000","QueryResult":"True","TO":"中国电信","Corp":"中国电信","Province":"黑龙江","City":"大庆","AreaCode":"0459","PostCode":"163000","VNO":"","Card":""}
        try:
            table = soup.find('table', attrs={'style': 'border-collapse: collapse'})
            tr = table.find_all('tr', class_='tdc')
            Mobile = number
            Corp = '中国电信'
            Province = tr[1].find_all('td')[1].text.split(' ')[0]
            City = tr[1].find_all('td')[1].text.split(' ')[1]
            AreaCode = tr[3].find_all('td')[1].text
            PostCode = tr[4].find_all('td')[1].text.split(' ')[0]
            json_dict = {"Mobile": Mobile, "Corp": Corp, "Province": Province, "City": City, "AreaCode": AreaCode,
                         "PostCode": PostCode}
            Json_data = json.dumps(json_dict, ensure_ascii=False)
        except:
            Json_data = None
            Province = None
            City = None
            Corp = None
            AreaCode = None
        if Province == '':
            Province = None
        if City == '':
            City = None
        item['Json_data'] = Json_data
        item['Corp'] = Corp
        item['Province'] = Province
        item['City'] = City
        item['AreaCode'] = AreaCode
        if City == None and Province == None:
            yield None
            print('该数据为空！')
        else:
            yield item