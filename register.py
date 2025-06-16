import csv
import time
from pin_checker import checker

file_path = 'user.csv'

class User:
    user_logined = 0

    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.balance = 0
        User.user_logined += 1

    def to_list(self):
        return [self.username, self.pin, self.balance]

def save_user(user):
    with open(file_path, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(user.to_list())


def welcomer():
    print('Selamat datang di Thurz Slot')
    print('****************************')
    print('Register untuk membuat akun')
    print('Login jika sudah mempunyai akun')
    print('****************************')
    print('1) Register')
    print('2) Login')
    while True:
        pilihan = input('Pilih salah satu : ')
        if "-" in pilihan:
            print('Pilih angka 1 atau 2 saja !')
        elif not pilihan.isdigit():
            print('Masukan angka 1 atau 2 saja')
            continue
        else:
            pilihan = int(pilihan)
            if pilihan != 1 and pilihan != 2:
                print('Pilih angka 1 atau 2 saja !')
                continue
            else:
                break

    if pilihan == 1:
        while True:
            username = input('Masukan nama : ')
            if username.isdigit():
                print('Masukan Username dengan benar!')
                continue
            elif '-' in username:
                print("Username tidak bisa mengandung symbol '-' ")
                continue
            else:
                username = username.capitalize()
                break
            
        while True:
            pin = input('Masukan pin : ')
            if not pin.isdigit():
                print('Masukan angka saja !')
                continue
            else:
                break
            
        Found = False
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if username in row:
                    Found = True
                    print("Username sudah terdaftar")
                    print('************************')
                    print('1) Kembali ke beranda')
                    print('2) Lihat Pin')
                    while True:
                        pilihan2 = input('Pilih salah satu : ')
                        if "-" in pilihan2:
                            print('Pilih angka 1 atau 2 saja !')
                        elif not pilihan2.isdigit():
                            print('Masukan angka 1 atau 2 saja')
                            continue
                        else:
                            pilihan2 = int(pilihan2)
                            if pilihan2 != 1 and pilihan2 != 2:
                                print('Pilih angka 1 atau 2 saja !')
                            elif pilihan2 == 1:
                                welcomer()
                                return
                            elif pilihan2 == 2:
                                checker()
                                print('Kembali ke beranda.....')
                                time.sleep(5)
                                welcomer()
                                return
                elif not username in row:
                    Found = False
        if not Found:
            user = User(username, pin)
            save_user(user)
            print("Registrasi berhasil!")
            print('Kembali ke beranda.....')
            time.sleep(5)
            welcomer()
    else:
        while True:
            username = input('Masukan nama : ')
            if username.isdigit():
                print('Masukan Username dengan benar!')
                continue
            elif '-' in username:
                print("Username tidak bisa mengandung symbol '-' ")
                continue
            else:
                username = username.capitalize()
                break
            
        while True:
            pin = input('Masukan pin : ')
            if not pin.isdigit():
                print('Masukan angka saja !')
                continue
            else:
                break
        
        Found = False
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2 and row[0] == username and row[1] == pin:
                    Found = True
                    break

        if Found:
            acc_balance = balance_controler(username)
            print('Berhasil Login')
            print('Loading....')

        else:
            print('Username atau pin tidak ditemukan')
            print('Silahkan masukan username dan pin dengan benar')
            print('Jika belum mempunyai akun, silahkan registrasi terlebih dahulu')
            print('Kembali ke beranda.....')
            time.sleep(5)
            welcomer()




def balance_controler(*args):
    for arg in args:
        user = arg

    balance = 0

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3 and row[0] == user:
                balance += int(row[2])
    return balance

if __name__ == '__main__':
    welcomer()

