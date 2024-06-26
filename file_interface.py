import os
import json
import base64
from glob import glob

class FileInterface:
    def __init__(self):
        os.makedirs('files/', exist_ok=True)
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if filename == '':
                return None
            with open(filename, 'rb') as fp:
                isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def upload(self, params=[]):
        try:
            filename = params[0]
            filedata = params[1]
            mode = 'ab' if os.path.exists(filename) else 'wb'  # Append if file exists
            with open(filename, mode) as fp:
                fp.write(base64.b64decode(filedata))
            return dict(status='OK')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def delete(self, params=[]):
        try:
            filename = params[0]
            os.remove(filename)
            return dict(status='OK')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
    print(f.upload(['test_upload.jpg', base64.b64encode(b"test content").decode()]))
    print(f.delete(['test_upload.jpg']))
