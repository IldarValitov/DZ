import tabula

myfile = 'price.pdf'
tabula.convert_into(myfile, 'price55.csv')
print('Если видно это, то все прошло успешно')
