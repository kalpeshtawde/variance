import dropbox
import os
import time
from os import listdir
from os.path import isfile, join

dbx = dropbox.Dropbox("O8tHMaacfEAAAAAAAAAAMUdtwFltXBBYlNgmm_9NyKkw9aCDowCJX30kimSp7V5g")

mypath = "/home/ubuntu/data/electoral"

flag = True

while flag:
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if not files:
        time.sleep(600)
    else:
        for file in files:
            try:
                print("Uploading file {0}".format(file))

                with open("{0}/{1}".format(mypath, file), 'rb') as f:
                    dbx.files_upload(f.read(), "/ENGLISH_PDF/{0}".format(file))
            except Exception as e:
                print("Upload failed for file {0} with error {1}".format(file, str(e)))
            else:
                os.unlink("{0}/{1}".format(mypath, file))


#f = open('working-draft.txt', 'rb')
#response = client.put_file('/magnum-opus.txt', f)
#print 'uploaded: ', response

#folder_metadata = client.metadata('/')
#print 'metadata: ', folder_metadata

#f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
#out = open('magnum-opus.txt', 'wb')
#out.write(f.read())
#out.close()
#print metadata
