# License: MIT (c) GitLab Inc.
import requests

# ruleid: python_requests_rule-request-without-timeout
requests.get('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.get('https://gmail.com', timeout=None)
requests.get('https://gmail.com', timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.get('https://gmail.com', timeout=None, headers={'authorization': f'token 8675309'})
requests.get('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
# ruleid: python_requests_rule-request-without-timeout
requests.get('https://gmail.com', headers={'authorization': f'token 8675309'})
# ruleid: python_requests_rule-request-without-timeout
requests.get('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=None)
requests.get('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.post('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.post('https://gmail.com', timeout=None)
requests.post('https://gmail.com', timeout=5)
requests.post('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
requests.post('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.put('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.put('https://gmail.com', timeout=None)
requests.put('https://gmail.com', timeout=5)
requests.put('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
requests.put('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.delete('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.delete('https://gmail.com', timeout=None)
requests.delete('https://gmail.com', timeout=5)
requests.delete('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
requests.delete('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.patch('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.patch('https://gmail.com', timeout=None)
requests.patch('https://gmail.com', timeout=5)
requests.patch('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
requests.patch('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.options('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.options('https://gmail.com', timeout=None)
requests.options('https://gmail.com', timeout=5)
requests.options('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
requests.options('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)
# ruleid: python_requests_rule-request-without-timeout
requests.head('https://gmail.com')
# ruleid: python_requests_rule-request-without-timeout
requests.head('https://gmail.com', timeout=None)
requests.head('https://gmail.com', timeout=5)
requests.head('https://gmail.com', timeout=5, headers={'authorization': f'token 8675309'})
requests.head('https://gmail.com', headers={'authorization': f'token 8675309'}, timeout=5)


def get(url):
    # ruleid: python_requests_rule-request-without-timeout
    return requests.get(url)


def get(url, timeout=10):
    return requests.get(url, timeout=timeout)
