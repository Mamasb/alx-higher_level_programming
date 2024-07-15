#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status using urllib"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Create a request object with the specified URL and headers
    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print(f'HTTP Error: {e.code} {e.reason}')
    except urllib.error.URLError as e:
        print(f'URL Error: {e.reason}')
