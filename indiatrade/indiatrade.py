import re
import urllib3

baseurl = "https://www.tradeindia.com"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()


def get_seller_details(seller_url, seller_name, category):
    r = http.request('GET', baseurl + seller_url)
    data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace("\t", "")

    add_re = re.search('<span class="add">(.*?)<\/span>', data)
    if add_re:
        address = add_re.group(1)
    print(data)

    print(baseurl + seller_url + "|" + seller_name + "|" + category + "|" +
          address + "|Manufacturer|" )
    exit()

def get_mfgs(url, category):
    print("Processing for url " + url)
    r = http.request('GET', baseurl + url)
    data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace("\t", "")
    id_re = re.search('<input type="hidden" name="pagination_qs" '
                            'id="pagination_qs" value="(.*?)"', data)
    if id_re:
        mfgs_url = ("https://www.tradeindia.com/design2017/products/components"
               "/leaf_categories_product_listing_grid_list.html?" +
                    id_re.group(1) + "&show_other_components=0&page_no=1")
        print("Processing Manufacturer " + mfgs_url)
        r = http.request('GET', mfgs_url)
        data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
            "\t", "")
        sellers = re.findall('<a href="(\/Seller-.*?\/)" target="_blank" '
                             '><span>(.*?)<\/span><\/a>', data)
        for seller_url, seller_name in sellers:
            get_seller_details(seller_url, seller_name, category)
    exit()

def get_alphalist(url):
    try:
        r = http.request('GET', url)
        data = r.data.decode('ISO-8859-1')
        cats_re = re.findall('<a href="(\/manufacturers\/.*?)">', data)
        for link in cats_re:
            category = link.split('/')[2].split('.')[0].replace("-", " ").upper()
            get_mfgs(link, category)
    except Exception as e:
        print("Get page failed for url " + str(e))

get_alphalist("https://www.tradeindia.com/design2017/manufacturers"
               "/components/keywords.html?from=a&&show_other_components=0"
              "&page_no=1")

#https: // www.tradeindia.com / design2017 / manufacturers / components / keywords.html?from=b & & show_other_components = 0 & page_no = 1
# for category in categories:
#     page = baseurl + '/' + category
#     get_page(page)
