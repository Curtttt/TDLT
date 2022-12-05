from math import floor


def doi(a):
    a = float(a)
    if a % floor(a) == 0:
        return int(a)
    else: return a


def nhapten():
    while True:
        try:
            name = input("Họ và tên: ")
            if name.strip() == "":
                raise Exception
        except:
            print("Không được để trống!!!")
        else:
            return name


def nhap_tcdiem(k):
    j, tg = 1, []
    while j != k+1:
        try:
            tam = tuple(map(doi, input(f"Số tín chỉ và điểm tương ứng môn {j}: ").split()))
            if tam[1] < 0 or tam[1] > 10:
                raise Exception
            elif tam[0] not in (2, 3, 4):
                raise ValueError
            else:
                tg.append(tam)
                j += 1
        except ValueError:
            print("Tín chỉ nhập không hợp lệ!!!")
        except:
            print("Điểm nhập không hợp lệ!!!")
    return tg


def nhapdrl():
    while True:
        try:
            tam = int(input("Điểm rèn luyện: "))
            if tam < 0:
                raise Exception
            else: break
        except:
            print("Điểm nhập không hợp lệ!!!")
    return tam


def xephb(ten_, diem_, drl_):
    pass


n = 0
while True:
    try:
        while n == 0:
            n = int(input("Số sinh viên cần xét: "))
            if n < 2: raise Exception
        m = int(input("Số môn học cần xét: "))
        if m < 2: raise Exception
    except ValueError:
        print("Định dạng không hợp lệ!!!")
    except:
        print("Số lượng phải ít nhất là 2!!!")
    else: break

sv = []
for i in range(n):
    print('*' * 21)
    sv.append({'ten': nhapten(),
               'drl': nhapdrl(),
               'tcdiem': nhap_tcdiem(m)})

print(sv)
