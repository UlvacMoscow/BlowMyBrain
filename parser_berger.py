import requests
from bs4 import BeautifulSoup
import time
import csv

# выяснить коль-во страниц
# сформировать список урлов на страницы выдачи
# собрать данные

urls = []
another_urls = []
finish_urls = []
katalog_url = "http://toolsberger.com/katalog/"
request = requests.get(katalog_url)
major_url = 'http://toolsberger.com'


# генерируем все урлы в случае если страниц больше чем одна
def get_total_pages(html):
    time.sleep(1.5)
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find_all('a', class_ ='vc_single_image-wrapper')
    # сгенерировали первую часть урлов на подкаталоги в разде catalog
    for page in pages:
        if page.get('href').startswith(major_url):
            urls.append(page.get('href'))
        else:
            urls.append(major_url + page.get('href'))

        # теперь нужно сгенерировать часть урлов из которых можно тащить инфу, но будут подразделы где будет еще вложения и там еще группа урлов
    for other_url in urls:
        time.sleep(1.5)
        request2 = requests.get(other_url).text
        soup2 = BeautifulSoup(request2, 'lxml')
        another_pages = soup2.find_all('div', class_="product-element-top")
        # здесь записываются сразу готовые урлы под группы нет
        if another_pages != []:
            for tag in another_pages:
                print(tag.find('a').get('href'))
                try:
                    finish_urls.append(tag.find('a').get('href'))
                except:
                    continue
        else:
            print('Глубже надо копать')
            other_pages = soup2.find_all('a', class_='vc_single_image-wrapper')
            # подготавливаем урлы которые накопали и по ним делаем еще один реквест в поисках урлов на товары
            for other in other_pages:
                if other.get('href').startswith(major_url):
                    another_urls.append(other.get('href'))
                else:
                    another_urls.append(major_url + other.get('href'))
            # теперь requests пройтись по урлам и записать их в finish_urls
            for another in another_urls:
                time.sleep(1.5)
                request3 = requests.get(another).text
                soup3 = BeautifulSoup(request3, 'lxml')
                last_pages = soup3.find_all('div', class_="product-element-top")
                print('Смотри не ли чего пустого', last_pages)
                for last in last_pages:
                    try:
                        finish_urls.append(last.find('a').get('href'))
                    except:
                        print('error')


def write_csv(data):
    with open('berger.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( 'ссылка на изделие' )

# get_total_pages(request.text)


print('---------------- finish_urls---------------------' )
# print(finish_urls)
# print(len(finish_urls))


write_csv(finish_urls)

test = ['http://toolsberger.com/product/nabor-instrumentov-dlya-zameny-koles-5-predmetov/','http://toolsberger.com/product/golovka-tortsevaya-udlinennaya-superlock-12-berger/', 'http://toolsberger.com/product/napilniki-s-dvuhkomponentnoj-ruchkoj/']
# теперь пройдемся requests по списку нашиш finish_urls и записать все xls файл

for url in test:
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')
    name = soup.find('h1', class_='product_title').text.strip()
    image = soup.find('img', class_='attachment-shop_single size-shop_single wp-post-image').get('src').strip()
    option = soup.find_all('div', class_='woocommerce-product-details__short-description')
    temp = soup.find('div', class_='woocommerce-product-details__short-description').find_all_next('span')
    # articul = temp[0].find('span').text
    # price = temp[1].find('span').text
    # print(name)
    # print(option)
    # print(image)
    # print(dir(soup))
    print(temp)
    print('-----------------------')
    # print(temp.find_all('span')[1])
    # print(temp)
    # print(articul)
    # print(price)
    time.sleep(1.5)
