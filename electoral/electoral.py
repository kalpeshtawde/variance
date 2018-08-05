import os
import time
import urllib3

http = urllib3.PoolManager()

outdir = "/home/ubuntu/data/electoral"

mapping = [
    "1:4-10"
#   "2:11-19",
#   "3:20-34",
#   "4:35-53",
#   "5:54-68",
#   "6:69-84",
#   "7:85-101",
#   "8:102-113",
#   "9:114-123",
#   "10:124-133",
#   "11:134-147",
#   "12:148-161",
#   "13:162-175"
]

def get_free_size():
    st = os.statvfs("/home/ubuntu/data/electoral/")
    free = st.f_bavail * st.f_frsize
    return free

for val in mapping:
    district, consts = val.split(":")
    from_consts, to_consts = consts.split("-")
    for const in range(int(from_consts), int(to_consts)):
        space = get_free_size()
        if space < 1000000000:
            time.sleep(1200)
        const = str(const)
        page = 1 
        while page > 0:
            url = ("http://ceoaperms1.ap.gov.in/Electoral_Rolls/PDFGeneration"
               ".aspx?urlPath=F:\RUNNING_APPLICATIONS_23012018"
               "\FINALROLLS_SSR_2018\AC_{0}\English\S01A{0}P{"
               "1}.PDF".format(const.zfill(3), str(page).zfill(3)))

            filename = ("{2}/S01A{0}P{1}.PDF".format(const.zfill(3), str(page).zfill(3), outdir))
            print("Processing for page {0} district {1} and url {2}".format(page, district, url))
            try:
                r = http.request('GET', url)
                if r.status != 200:
                    page = 0
                else:
                    with open(filename, "wb") as fh:
                        fh.write(r.data)
                    fsize = os.path.getsize(filename)
                    if fsize < 2000:
                        page = 0
                        os.unlink(filename)
                    else:
                        page += 1
            except Exception as e:
                print("Download failed for url {0} Error {1}".format(
                    url,str(e))
                )
