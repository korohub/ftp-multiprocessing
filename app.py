import os
from multiprocessing import Pool


liste=[]
for root, dirs, files in os.walk("/u01/datapump_exports/xxx"):
    for file in files:
       liste.append(os.path.join(root, file))


def upload(file): 
    ftp = ftplib.FTP('ftp.xxxxx.fr')
    ftp.login("<ftpuser>","<ftppassword>")
    f = open(x,'rb')
    ftp.storbinary('STOR %s' %x, f)
    f.close()
    ftp.quit()


infiles = liste

pool = Pool(3) # submit 10 at once
pool.map(upload,infiles)