import re
import urllib3

baseurl = "http://www.yellowpagesofafrica.com"

http = urllib3.PoolManager()


def parse_data(url, category, country):
    try:
        print("Processing for url " + url)

        name = address = ville = contact = email = website = ""

        r = http.request('GET', url)
        data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
            "\t", "")
        match = re.search('<input name="nom" type="text" value="(.*?)"', data)
        if match:
            name = match.group(1)

        match = re.search('<input name="adresse" type="text" value="(.*?)"', data)
        if match:
            address = match.group(1)

        match = re.search('<input name="ville" type="text" value="(.*?)"', data)
        if match:
            ville = match.group(1)

        match = re.search('<input name="tel" type="text" value="(.*?)"', data)
        if match:
            contact = match.group(1)

        match = re.search('<input name="email" type="text" value="(.*?)"', data)
        if match:
            email = match.group(1)

        match = re.search('<input name="website" type="text" value="(.*?)"', data)
        if match:
            website = match.group(1)

        fh = open("output.txt", "a")
        fh.write(url + "|" + country + "|" + name + "|" + address + "|" +
                 ville + "|" + category.capitalize() + "|" + contact + "|" +
                 email + "|" + website + "\n")
        fh.close()
        exit()
    except Exception:
        print("Data url download failed")

def get_page(page, category, country):
    r = http.request('GET', page)
    data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
        "\t", "")
    values = re.findall('<a href="(\/submit\/change\/.*?\/)" '
                            'style="cursor: pointer;">', data)
    for value in values:
        parse_data(baseurl + value, category)

def get_categories(url, country):
    flag = 0
    try:
        r = http.request('GET', url)
        data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
            "\t", "")
        categories = re.findall('\/" title="(.*?) - RDC"', data)
        print(categories)
        for category in categories:
            print("Processing for category " + category)
            if flag == 1:
                get_page(baseurl + "/companies/" + country + "/" +
                      category.lower().replace(" ", "-"), category, country)
            elif category == "vocational training centers":
                flag = 1
    except Exception:
        print("Categories download failed")

def get_countries():
    r = http.request(
        'GET',
        'http://www.yellowpagesofafrica.com')
    data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
        "\t", "")
    countries = re.findall('<a href="(/country/(.*?)/)">', data)
    for url, country in countries:
        print("Processing for country " + country)
        get_categories(baseurl + url, country)

get_countries()