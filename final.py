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


def tinhdiem(lst):
    tu, mau = 0, 0
    for j in range(len(lst)):
        tu += lst[j][0] * lst[j][1]
        mau += lst[j][0]
    # tu = sum(lst[j][0] * lst[j][1] for j in range(len(lst)))
    # mau = sum(lst[j][0] for j in range(len(lst)))
    return round(tu/mau, 2)


def xephocluc(diem_):
    if 10 >= diem_ >= 9:
        return "Xuất sắc"
    if 9 > diem_ >= 8:
        return "Giỏi"
    if 8 > diem_ >= 7:
        return "Khá"
    else: return "Không đạt"


def xepdrl(drl_):
    if 90 <= drl_:
        return "Xuất sắc"
    elif 80 <= drl_ <= 89:
        return "Giỏi"
    elif 65 <= drl_ <= 79:
        return "Khá"
    else: return "Không đạt"


def xephb(dic):
    match dic['hocluc']:
        case 'Xuất sắc':
            match dic['drl']:
                case 'Xuất sắc': return 1
                case 'Giỏi': return 2
                case 'Khá': return 3
                case _: return 4
        case 'Giỏi':
            if dic['drl'] == 'Xuất sắc' or dic['drl'] == 'Giỏi':
                return 2
            elif dic['drl'] == 'Khá': return 3
            else: return 4
        case 'Khá':
            if dic['drl'] != 'Không đạt': return 3
        case _: return 4


n = 0
while True:
    try:
        while n < 2:
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
    print('*' * 40)
    sv.append({'ten': nhapten(),
               'drl': xepdrl(nhapdrl())})
    tcdiem = nhap_tcdiem(m)
    sv[i]['diem'] = tinhdiem(tcdiem)
    sv[i]['hocluc'] = xephocluc(sv[i]['diem'])
    sv[i]['hocbong'] = xephb(sv[i])

print('-'*50, '\nSinh viên đủ điều kiện đạt học bổng loại:')
for i, hb in enumerate(('Xuất sắc', 'Giỏi', 'Khá', 'Không đạt'), 1):
    kq = ''
    for x in sv:
        if x['hocbong'] == i:
            kq += f" {x['ten']}({str(x['diem'])}),"
    print(f"{hb}:", kq[:-1])
