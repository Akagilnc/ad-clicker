import requests
import json


def get_ip_address(num=300, regions='us', n_type=0, ip_type=1, data_type=2, lb=1):
    # resp = requests.get(
    #     'https://www.sharedproxies.com/api.php?m=akagilnc%40gmail.com&s=faaf62382cfd1a3e19c53e955469efceb91cef9b&do=getall')
    with open('ip.txt', encoding='utf_8') as file:
        data_file = open('./ip.json', 'w', encoding='utf-8')
        ip_list = []
        for info in file:
            ip, port = info.strip().split(':')
            ip_list.append({'ip': ip, 'port': port})
    json.dump(ip_list, data_file, indent=4, ensure_ascii=False)

