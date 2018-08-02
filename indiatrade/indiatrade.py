import re
import urllib3

baseurl = "https://www.tradeindia.com"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()


def get_seller_details(seller_url):
    try:
        print("Processing for seller " + seller_url)

        r = http.request('GET', seller_url)
        data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace("\t", "")

        address = website = emp = certification = ""
        add_re = re.search('<span class="add">(.*?)<\/span>', data)
        if add_re:
            address = add_re.group(1)

        website_re = re.search('<span class="bold">Catalog -<\/span>.*?<a href="(.*?)".*?<\/a>', data)
        if website_re:
            website = website_re.group(1)

        emp_re = re.search(
            '<dt class="bold">Number of Employess:<\/dt>.*?<dd>(.*?)<\/dd>', data)
        if emp_re:
            emp = str(emp_re.group(1))

        certification_re = re.search(
            '<dt class="bold">Standard Certification:<\/dt>.*?<dd>(.*?)<\/dd>', data)
        if certification_re:
            certification = certification_re.group(1)

        return(address + "|" + website + "|" + emp + "|" + certification)

    except Exception as e:
        print("Seller page download failed " + str(e))

def get_mfgs(url, category, type):
    flag = True
    page = 1
    while flag:
        print("Page " + str(page))

        mainurl = url + '&page_no=' + str(page)
        r = http.request('GET', mainurl)
        data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
            "\t", "")
        mfgs = re.findall('<li>(.*?)<\/li>', data)
        if not mfgs:
            flag = False
        for mfg in mfgs:
            mfg_url = mfg_name = mfg_phone = mfg_certified = ""
            mfg_re = re.search('.*<a href="(.*?)" target="_blank" ><span>(.*?)'
                               '<\/span><\/a>', mfg)
            if mfg_re:
                mfg_url = baseurl + mfg_re.group(1)
                mfg_name = mfg_re.group(2)

            mfg_re = re.search('<span class="mob">(.*?)<\/span>', mfg)
            if mfg_re:
                mfg_phone = mfg_re.group(1)

            mfg_rating = str(len(re.findall('thumbs-up', mfg)))

            mfg_re = re.search('t-stump', mfg)
            if mfg_re:
                mfg_certified = "Yes"

            details = get_seller_details(mfg_url)

            fh = open("output.txt", "a")
            fh.write(mfg_url + "|" + mfg_name + "|" + category + "|" + category
                  + "|" + type + "|" + mfg_phone + "|" + details + "|" +
                  mfg_rating + "|" + mfg_certified + "\n")
            fh.close()

        page += 1

get_mfgs('https://www.tradeindia.com/design2017/products/components'
          '/leaf_categories_product_listing_grid_list.html?keyword=toy%20'
         '&sort_filter_applied=1&nobs=ifmanu&es_city_stat=1&%20games'
         '&design_2017=1&categories=1139&premium_membership=1&cat_id'
         '=&business_kw_id=&show_other_components=0', 'Toys', 'Manufacturer')


# def get_mfgs(url, category):
#     print("Processing for url " + url)
#     r = http.request('GET', baseurl + url)
#     data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace("\t", "")
#     id_re = re.search('<input type="hidden" name="pagination_qs" '
#                             'id="pagination_qs" value="(.*?)"', data)
#     if id_re:
#         mfgs_url = ("https://www.tradeindia.com/design2017/products/components"
#                "/leaf_categories_product_listing_grid_list.html?" +
#                     id_re.group(1) + "&show_other_components=0&page_no=1")
#         print("Processing Manufacturer " + mfgs_url)
#         r = http.request('GET', mfgs_url)
#         data = (" ".join(r.data.decode('ISO-8859-1').splitlines())).replace(
#             "\t", "")
#         sellers = re.findall('<a href="(\/Seller-.*?\/)" target="_blank" '
#                              '><span>(.*?)<\/span><\/a>', data)
#         for seller_url, seller_name in sellers:
#             get_seller_details(seller_url, seller_name, category)
#     exit()
#
# def get_alphalist(url):
#     try:
#         r = http.request('GET', url)
#         data = r.data.decode('ISO-8859-1')
#         cats_re = re.findall('<a href="(\/manufacturers\/.*?)">', data)
#         for link in cats_re:
#             category = link.split('/')[2].split('.')[0].replace("-", " ").upper()
#             get_mfgs(link, category)
#     except Exception as e:
#         print("Get page failed for url " + str(e))
#
# get_alphalist("https://www.tradeindia.com/design2017/manufacturers"
#                "/components/keywords.html?from=a&&show_other_components=0"
#               "&page_no=1")

#https: // www.tradeindia.com / design2017 / manufacturers / components / keywords.html?from=b & & show_other_components = 0 & page_no = 1
# for category in categories:
#     page = baseurl + '/' + category
#     get_page(page)
