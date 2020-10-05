import requests
import re

url = 'https://wiki.52poke.com/zh-hant/%E7%89%B9%E6%80%A7%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89'

def save(url, file='urltemp.text'):
    with open('file', 'w', encoding='utf8') as writer:
        content = requests.post(url)
        print(content.text, file=writer)


def get_content(url):
    #with open('urltemp.text', 'r', encoding='utf8') as reader:
        #return reader.read()
    return requests.post(url).text
    


regex1 = '(?<=D8D8D8;width:110px;"><a href=")/wiki/%E.*\"\stitle'
regex2 = '(?<=href=\")/wiki/File\:\d+[A-Za-z]+\.png\"\sclass'
regex3 = '/wiki/\w+/\w+/\d+\w+\.png\"\>'

def get_data(url, regex, base):
    text = get_content(url)
    lst = []
    result = re.findall(regex, text)
    for each in result:
        if (base + each[:each.find('"')]) in lst:
            continue
        else:
            lst.append(base + each[:each.find('"')])
    return lst


def save_img(url):
    filename = url.split('/')[-1]
    with open (filename, 'wb') as writer:
        writer.write(requests.get(url).content)


b1 = 'https://wiki.52poke.com'
b2 = 'https://media.52poke.com'
for i in get_data(url, regex1, b1):
    #print(i)
    url = i
    #get_data(url, regex2)
    for j in get_data(url, regex2, b1):
        #print(j)
        url = j
        #get_data(url, regex3)
        for k in get_data(url, regex3, b2):
            print(k)
            url = k
            save_img(url)


#===================================================================
'''


def save_img(url):
    filename = url.split('/')[-1]
    with open (filename, 'wb') as writer:
        writer.write(requests.get(url).content)

url = 'https://media.52poke.com/wiki/2/21/001Bulbasaur.png'

save_img(url)

'''





#https://wiki.52poke.com/wiki/File:040Wigglytuff.png

#https://media.52poke.com/wiki/2/21/001Bulbasaur.png
    

    
