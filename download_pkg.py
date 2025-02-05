import lbuild
import urllib.request

def download(filename):
    ldata=lbuild.lbuild_file(filename)
    url=ldata.src_url
    local_filename=ldata.src
    try:
        with urllib.request.urlopen(url) as response:
            with open(local_filename, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
        print(f"文件 {local_filename} 下载成功！")
    except Exception as e:
        print(f"下载过程中出现错误: {e}")



