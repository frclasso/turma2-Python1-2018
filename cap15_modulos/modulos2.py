import urllib.request


def main():

    page = urllib.request.urlopen('https://docs.python.org/3/tutorial/index.html')
    print(page)
    print()
    for line in page:
        print(str(line, encoding='utf-8'), end='')


if __name__=="__main__":main()