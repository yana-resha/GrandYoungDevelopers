import requests
import json


file_path = 'TEST2.txt'

files = {'file': open(file_path, 'rb')}


header = {'Authorization' : 'введите токен'}


def upload():
  disc = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_path}', headers = header)
  href = (disc.json()['href'])
  response = requests.put(href, files=files, headers=header)
  print(f'Ваш {file_path} успешно загружен')


upload()