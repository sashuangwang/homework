import  xlwt
def xlwt_excel(filename,xlsxname):
    f = open(filename,'r',encoding = 'utf-8')
    fs = f.read()
    x = 0
    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workbook.add_sheet('库存状态')
    while True:
            lone = f.readline()
            print(type(lone))
            if not lone:
                   break
            for i in range(len(lone.split('， '))):
                   item = lone.split('， ')[i] 
                   sheet.write(x,i,item)
            x += 1  
               
    f.close()
    workbook.save(xlsxname)
if __name__ == '__main__':
    filename = ('/home/user/1.csv')
    xlsxname = ('/home/user/1.xlsx')
    xlwt_excel(filename,xlsxname) 
