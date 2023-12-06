import requests, re

def get_latest_version():
    stable_page=requests.get('https://www.sublimemerge.com/download').text
    dev_page=requests.get('https://www.sublimemerge.com/dev').text
    matched_stable=re.findall('Build *[0-9]+',stable_page)
    stable_version=matched_stable[0].split(' ')[1]
    matched_dev=re.findall('Build *[0-9]+',dev_page)
    dev_version=matched_dev[0].split(' ')[1]
    isDev=True if stable_version < dev_version else False
    return dev_version, str(isDev).lower() if isDev else stable_version


if __name__ == '__main__':
    print(' '.join(get_latest_version()))
