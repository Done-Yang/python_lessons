# chang word and count file
"""
# To count how many word or how many white space in the file
with open('FILE Folder\Ater text.txt', 'r') as f:
    data = f.read()
    tmp = data.split()
    print('words count: [%d]' % len(tmp))


# to change something in ready-file
t1 = input('which word ? : ')
t2 = input('change to ? : ')

with open('FILE Folder\Ater text.txt', 'r') as r:
    with open('FILE Folder\Ater text.txt', 'w') as w:
        text = r.read()
        text = text.replace(t1, t2)
        w.write(text)
print('[%s] change to [%s]' % (t1, t2))
"""


# print the domain name from the url
"""
from urllib.request import urlopen
url = 'http://lkclaos.org/department-of-korean-language/'
with urlopen(url) as f:
    dom = url.split('/')
    
    print(dom[3])   # print(domain name)

"""


# hint meaning
"""
     hint: use to split the function parameter(it just a comment that help editor and explain. not status type
     example:
     def my_function(a: str, b: int)
"""


# Count 'IATER' text in the file


# count 'IATER' in the ATER file
"""
ip = input('which word')
with open('FILE Folder\iATER text.txt') as f:
    read = f.read()
    print(read.count(ip))

"""


from urllib.request import urlopen

imghdr = ''
img_name = imghdr.split('/')[-1]
print(img_name)
try:
    with urlopen(imghdr) as f:
        with open(img_name, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)

