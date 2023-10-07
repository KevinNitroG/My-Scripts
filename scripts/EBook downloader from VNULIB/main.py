import requests
import os
import ssl 

ssl._create_default_https_context = ssl._create_unverified_context

# url = input('Input URL of the first page: ')
# pages_number = int(input('Input amount of pages: '))

url = r'https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=119407993845809379459430067212192785232&format=jpg&page=109&subfolder=11/94/07/'
pages_number = 235

os.chdir('./downloaded')

for i in range(1, pages_number + 1):
    changed_url = url.replace('page=1', f'page{i}')
    response = requests.get(changed_url, verify='C:/Users/trann/AppData/Local/.certifi/cacert.pem')
    # if response.status_code == 200:
    img = response.content
    file_name = f'{i}.jpg'
    with open(file_name, 'wb') as f:
        f.write(img)