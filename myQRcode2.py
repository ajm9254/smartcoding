import qrcode

file_path = 'QRcode\\qrList.txt'

f = open(file_path, 'r',encoding='UTF8')
lines = f.readlines()

for line in lines :
    line = line.strip()
    print(line)
    qr_img = qrcode.make(line)
    save_path = '\\' +  + '.png'
    qr_img.save(save_path)


f.close()