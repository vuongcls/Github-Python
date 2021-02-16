def NamSv(x):
        switcher={
                17:'Bạn là sv năm Tư',
                18:'Bạn là sv năm Ba',
                19:'Bạn là sv năm Hai',
                20:'Bạn là sv năm Nhất',
                16:'Bạn là sv năm NĂM',
                15:'Bạn là sv năm Sáu',
                14:'Bạn là sv năm Bảy'
             }
        return switcher.get(x, "haizzzz")
def NganhSv(x):
        switcher={
                119:'Bạn học ngành Kỹ Thuật Máy Tính',
                141:'Bạn học viễn thông',
                151:'Bạn học điện điện tử',
                153:'Bạn học tự động hóa',
                155:'BẠN học Y sinh',
                160:'Bạn học IOTS',
             }
        return switcher.get(x, "nothing")

mssv = int(input("Nhập mã số sinh viên của bạn: "))
maso = str(mssv)
khoaSV = int(maso[0])*10+int(maso[1])
nganhSV = int(maso[2])*100+int(maso[3])*10 +int(maso[4])
print("Bạn khóa ",str(khoaSV))
hoten = input("Nhập họ & tên của bạn: ")
arr = hoten.split()
sizeMax = len(arr)
print("Hello: ",arr[sizeMax-1]+" "+ arr[0])

print(NamSv(khoaSV))
print(NganhSv(nganhSV))
for i in range(0,40):
    print("_",end='')

