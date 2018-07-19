import re
import urllib3

baseurl = "http://www.yellowpagesofafrica.com"

http = urllib3.PoolManager()


def parse_data(url, category):
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
        fh.write(name + "|" + address + "|" + ville + "|" +
              category.capitalize() +
              "|" + contact + "|" + email + "|" + website + "\n")
        fh.close()
    except Exception:
        print("Data url download failed")

def get_page(page, category):
    r = http.request('GET', page)
    data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
        "\t", "")
    values = re.findall('<a href="(\/submit\/change\/.*?\/)" '
                            'style="cursor: pointer;">', data)
    for value in values:
        parse_data(baseurl + value, category)

def get_categories():
    flag = 0
    try:
        r = http.request(
            'GET',
            'http://www.yellowpagesofafrica.com/country/congo-democratic-republic-of-the/')
        data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
            "\t", "")
        categories = re.findall('\/" title="(.*?) - RDC"', data)
        for category in categories:
            print("Processing for category " + category)
            if flag == 1:
                get_page(baseurl + "/companies/congo-democratic-republic-of-the/" +
                      category.lower().replace(" ", "-"), category)
            elif category == "vocational training centers":
                flag = 1
    except Exception:
        print("Categories download failed")


get_categories()
#for category in categories:
#    page = baseurl + '/' + category
#    get_page(page)
