import csv


row=['name','price','iter','data','offer']
data = ['http:toolsberger.com',
'ertertertretert','234234324234234','324234234324','wwwwwwwwwwwwwww']


def write_csv(data, row):
    i = 0
    with open('berger.csv', 'w') as f:
        if i == 0:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(row)
            i += 1
        writer = csv.writer(f, delimiter=';')
        writer.writerow(  data  )



write_csv(data,row)
