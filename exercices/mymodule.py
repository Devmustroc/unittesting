def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)


def newUrl(protocol, host, domain, sub):
    url = f'{protocol}://{host}.{domain}/{sub}'
    print(url)


def new_link(host, domain, sub):
    url = f"{host}.{domain}/{sub}"
    print(url)


def pass_wrd(**name):
    for key, value in name.items():
        print(f"{key} : {value}")


name = {"first": "John", "second": "Jason", "third": "Jules", "fourth": "Jude"}
pass_wrd(**name)
