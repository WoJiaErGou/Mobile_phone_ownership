from bs4 import BeautifulSoup as bs
import json
with open('get.txt','r',encoding='utf-8') as file:
    text = file.read()
    soup = bs(text,'lxml')
    #{"Mobile":"13329470000","QueryResult":"True","TO":"中国电信","Corp":"中国电信","Province":"黑龙江","City":"大庆","AreaCode":"0459","PostCode":"163000","VNO":"","Card":""}
    table = soup.find('table',attrs={'style':'border-collapse: collapse'})
    tr = table.find_all('tr',class_='tdc')
    Mobile = tr[0].find_all('td')[1].text.split(' ')[0]
    Corp = '中国移动'
    Province = tr[1].find_all('td')[1].text.split(' ')[0]
    City = tr[1].find_all('td')[1].text.split(' ')[1]
    AreaCode = tr[3].find_all('td')[1].text
    PostCode = tr[4].find_all('td')[1].text.split(' ')[0]
    json_dict = {"Mobile":Mobile,"Corp":Corp,"Province":Province,"City":City,"AreaCode":AreaCode,"PostCode":PostCode}
    json_data = json.dumps(json_dict,ensure_ascii=False)
