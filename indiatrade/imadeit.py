import re
import urllib2

baseurl = "https://imadeit.in"
categories = ['bakery', 'food', 'design', 'gifts', 'beauty', 'invitations',
              'corporate-gifts']

http = urllib2.PoolManager()

def get_contents(url):
    print("Processing for url " + url)

    vendor = ""
    vendor_url = ""
    overview = ""

    r = http.request('GET', baseurl + url)
    data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace("\t", "")

    match = re.search('By <a href="(\/user\/.*?)">(.*?)<\/a>', data)
    if match:
        vendor_url = baseurl + match.group(1)
        vendor = (str(match.group(2))).strip()

    match = re.search('Overview <\/span> <p class="cprdi-dscr">(.*?)<\/p>',
                      data)
    if match:
        overview = (match.group(1)).strip()

    fh = open("output.txt", "a")
    fh.write(baseurl + url + "|" + vendor + "|" + vendor_url + "|" +
           category.title() + "|" + overview + "\n")
    fh.close()

def parse_data(data):
    urllist = re.findall('<a href="(.*?)" class="cpb-nl"', data)
    for url in urllist:
        try:
            get_contents(url)
        except Exception:
            print("Contents failed for url")


def get_page(page):
    try:
        r = http.request('GET', page)
        data = r.data.decode('ISO-8859-1')
        parse_data(data)
        nextre = re.compile('.*<a href="(.*?)" rel="next">')
        next = nextre.search(data)
        if next:
            nexturl = next.group(1)
            print(nexturl)
            get_page(nexturl)
    except Exception:
        print("Get page failed for url")

#
for category in categories:
    page = baseurl + '/' + category
    get_page(page)
