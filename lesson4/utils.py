from requests import get, utils
def currency_rates(url,valute):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    valute = input('Введите код валюты: ')
    valute1 = valute.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    val = content.split('<CharCode>')
    for allcur in val:
        valutaa = allcur.split('</CharCode>')
        if valute1 ==valutaa[0]:
            currency = valutaa[1].split('</Value>')
            currency1 = currency[0][-7:]
            return url,currency1
        else: None
