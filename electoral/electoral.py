import os
import time
import urllib3
import dropbox
from os import listdir
from os.path import isfile, join

dbx = dropbox.Dropbox("O8tHMaacfEAAAAAAAAAAMUdtwFltXBBYlNgmm_9NyKkw9aCDowCJX30kimSp7V5g")

mypath = "/home/ec2-user/data/electoral"

http = urllib3.PoolManager()

outdir = "/home/ec2-user/data/electoral"

mapping = [
#    "1:10-10"
#   "2:11-19",
#   "3:20-34",
   "4:36-53",
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

def dropbox_upload(filename):
    try:
        print("Uploading file {0}".format(filename))

        with open("{0}/{1}".format(mypath, filename), 'rb') as f:
            dbx.files_upload(f.read(), "/ENGLISH_PDF/{0}".format(filename))
    except Exception as e:
        print("Upload failed for file {0} with error {1}".format(filename, str(e)))
    else:
        os.unlink("{0}/{1}".format(mypath, filename))

def dropbox_exists(filename):
    flag = False
    try:
        dbx.files_get_metadata('/ENGLISH_PDF/{0}'.format(filename))
    except Exception as e:
        print("File {0} not present.".format(filename))
        flag = False
    else:
        print("File {0} already present.".format(filename))
        flag = True
    return flag

def get_free_size():
    st = os.statvfs("/home/ec2-user/data/electoral/")
    free = st.f_bavail * st.f_frsize
    return free

for val in mapping:
    district, consts = val.split(":")
    from_consts, to_consts = consts.split("-")
    for const in range(int(from_consts), int(to_consts) + 1):
        const = str(const)
        page = 1
        while page > 0:
            space = get_free_size()
            if space < 1000000000:
                print("Space full sleeping for 20 minutes")
                time.sleep(1200)
            url = ("http://ceoaperms1.ap.gov.in/Electoral_Rolls/PDFGeneration"
               ".aspx?urlPath=F:\RUNNING_APPLICATIONS_23012018"
               "\FINALROLLS_SSR_2018\AC_{0}\English\S01A{0}P{"
               "1}.PDF".format(const.zfill(3), str(page).zfill(3)))

            exists = dropbox_exists("S01A{0}P{1}.PDF".format(const.zfill(3), str(page).zfill(3)))

            if not exists:
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
                            dropbox_upload("S01A{0}P{1}.PDF".format(const.zfill(3), str(page).zfill(3)))                     
                            page += 1
                except Exception as e:
                    print("Download failed for url {0} Error {1}".format(
                        url,str(e))
                    )
            else:
                page += 1
