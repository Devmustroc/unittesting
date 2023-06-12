def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)


def newUrl(protocol, host, domain, sub):
    url = f'{protocol}://{host}.{domain}/{sub}'
    print(url)


def new_link(host, domain, sub):
    url = f"{host}.{domain}/{sub}"
    print(url)