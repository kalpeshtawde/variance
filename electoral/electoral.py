import urllib3

http = urllib3.PoolManager()

mapping = [
    "1:1-10",
    "2:11-19",
    "3:20-34",
    "4:35-53",
    "5:54-68",
    "6:69-84",
    "7:85-101",
    "8:102-113",
    "9:114-123",
    "10:124-133",
    "11:134-147",
    "12:148-161",
    "13:162-175"
]

for val in mapping:
    district, consts = val.split(":")
    from_consts, to_consts = consts.split("-")
    for const in range(int(from_consts), int(to_consts)):
        const = str(const)
        page = 1
        while page < 5:
            url = ("http://ceoaperms1.ap.gov.in/Electoral_Rolls/PDFGeneration"
               ".aspx?urlPath=F:\RUNNING_APPLICATIONS_23012018"
               "\FINALROLLS_SSR_2018\AC_{0}\English\S01A{0}P{"
               "1}.PDF".format(const.zfill(3), str(page).zfill(3)))

            filename = ("S01A{0}P{1}.PDF".format(const.zfill(3), str(page).zfill(3)))
            print(url)
            try:
                r = http.request('GET', url)
                if r.status != 200:
                    page = 0
                else:
                    with open(filename, "wb") as fh:
                        fh.write(r.data)
            except Exception as e:
                print("Download failed for url {0} Error {1}".format(
                    url,str(e))
                )
            page += 1
