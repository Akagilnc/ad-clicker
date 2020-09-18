import requests
import json


def get_ip_address(num=200, regions='us', n_type=0, ip_type=1, data_type=2, lb=1):
    resp = requests.get('http://tiqu.linksocket.com:81/abroad?num={}&type={}&regions={}&lb={}&flow=1'.format(
        num, data_type, regions, lb
    ))

    data_file = open('./ip.json', 'w', encoding='utf-8')
    json.dump(resp.json(), data_file, indent=4, ensure_ascii=False)

