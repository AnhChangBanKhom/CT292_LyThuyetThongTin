# cau 1:

class Human:
    def __init__(self, hoten={}, namsinh={}, quequan={}, nghenghiep={}):
        self.hoten = hoten
        self.namsinh = namsinh
        self.quequan = quequan
        self.nghenghiep = nghenghiep

    def live(self, noicutru):
        print('Ten :{}'.format(self.hoten),
              '\nNoi cu tru: {}'.format(noicutru))

    def work(self, diachicoquan):
        v = self.nhap()
        print('\nTen: {}\nNghe nghiep: {}\nDia chi co quan: {}'.format(
            v.hoten, v.nghenghiep, diachicoquan))

    def getwork(self, n):
        for i in range(n):
            print('nhap dia chi co quan người thứ', i+1, ':')
            n = input()
            result = self.work(diachicoquan=n)

    def nhap(self):
        self.hoten = (input('Nhập họ tên :'))
        self.namsinh = (input('Nam sinh'':'))
        self.quequan = (input('Quê quán'':'))
        self.nghenghiep = (input('nghề nghiệp'':'))
        return self

    def inds(self):
        ls = ''
        ls += 'Họ tên: {0}\nnăm sinh: {1}\nQuê quán: {2}\nNghề nghiệp: {3}\n'.format(
            self.hoten, self.namsinh, self.quequan, self.nghenghiep)
        print(ls)
        return ls

    def getnhap(self, n):
        ds = []
        for i in range(1, n+1):
            result = self.nhap()
            ds.append(result.inds())
        return ds


    def getinds(self, n):
        ds = self.getnhap(n)
        for i in range(len(ds)):
            print('----------------------------')
            print('\tSinh viên thứ', i+1)
            print('----------------------------\n')
            print(ds[i])
            print('----------------------------')


class Student(Human):
    def __init__(self, hoten={}, namsinh={}, quequan={}, nghenghiep={}, MSSV={}, nganhhoc={}, diemTB={}):
        super().__init__(hoten={}, namsinh={}, quequan={})
        self.nghenghiep = 'student'
        self.MSSV = MSSV
        self.nganhhoc = nganhhoc
        self.diemTB = diemTB

    def study(self, Class):
        print('Ten: {}\nMSSV: {}\nNganh: {}\nPhong hoc: {}'.format(
            self.hoten, self.MSSV, self.nganhhoc, Class))

    def getnhap(self):
        super().nhap()
        self.nghenghiep = 'student'
        self.MSSV = input('MSSV')
        self.nganhhoc = input('nganh hoc')
        self.diemTB = float(input('diemTB'))
        return self

    def rank(self):
        xeploai = ''
        diemTB = self.diemTB
        if (diemTB <= 10.0 and diemTB >= 0.0):
            if (diemTB < 4):
                xeploai = 'Loại Yếu'
            elif (diemTB >= 4 and diemTB < 6):
                xeploai = 'Loại Trung Bình'
            elif (diemTB >= 6 and diemTB < 8):
                xeploai = 'Loại Khá'
            else:
                xeploai = 'Loại Giỏi'
        else:
            print('lỗi nhập điểm!!!')
        print('Tên: {}, MSSV: {},diemTB: {} xeploai: {}'.format(
            self.hoten, self.MSSV, self.diemTB, xeploai))


SV1 = Student(hoten='Lê Văn An', namsinh='2005', quequan='Vĩnh Long',
              nghenghiep={}, MSSV='12345', nganhhoc='CNTT', diemTB=7.6)
SV2 = Student(hoten='Trần Văn Bình', namsinh='2007', quequan='Trà Vinh',
              nghenghiep={}, MSSV='56789', nganhhoc='Tài chính ngan hàng', diemTB=4.5)
# Student().getnhap().rank()


n = int(input('nhap so luong:'))

# Human().getnhap(n)
# Student().rank()
# Human().getinds(n)
Human().nhap().inds()
