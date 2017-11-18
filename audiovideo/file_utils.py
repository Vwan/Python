import os, shutil, datetime
"""
copy wechat .amr files and group by year and month
"""

def copy_files(src, target, filetype=None):
    id = 1
    for dirname, subdirlist, filelist in os.walk(src):
        for fname in filelist:
            if filetype:
                if filetype in fname:
                    mtime = os.stat(os.path.join(dirname, fname)).st_mtime
                    dtime = datetime.datetime.fromtimestamp(mtime)
                    month = str(dtime.month)
                    year = str(dtime.year)
                    if not os.path.exists(os.path.join(target, year, month)):
                        os.makedirs(os.path.join(target, year, month))
                    newtime = str(dtime).replace(":", "-")
                    newfilename = newtime + "_"+ fname
                    print("src----", os.path.join(dirname, fname))
                    print("target---", os.path.join(os.path.join(target, year, month), str(id) + "_" + newfilename))
                    shutil.copy(os.path.join(dirname, fname), os.path.join(os.path.join(target, year, month), str(id) + "_" + newfilename))
                    id += 1

src = r"c:\temp\voice2"
if not os.path.exists(r"c:\temp\amrfiles_20171117_by_month"):
    os.mkdir(r"c:\temp\amrfiles_20171117_by_month")
target = r"c:\temp\amrfiles_20171117_by_month"
copy_files(src, target, '.amr')