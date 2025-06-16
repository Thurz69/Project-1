import random
import time
import csv
from pin_checker import checker

file_path = 'user.csv'

def spin_row():
    symbols = ['🍒', '🍉', '⭐', '🍋', '💰']
    result = []

    print('Spinning...')
    for symbol in range(3):
        result.append(random.choice(symbols))
        print("**************")
        print(" | ".join(result))
        print("**************")
        time.sleep(0.5)
    return result

def print_row(row):
    pass
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 20
        elif row[0] == '🍉':
            return bet * 25
        elif row[0] == '⭐':
            return bet * 40
        elif row[0] == '🍋':
            return bet * 50
        elif row[0] == '💰':
            return bet * 100
    else:
        return 0


def title(user):
        print('*'*30)
        print(f"Selamat datang {user} di Slot Machine")
        print("Symbols : 🍒 🍉 ⭐ 🍋 💰")
        print("Semoga beruntung !!")
        print("*"*30)

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
    print(f"Selamat datang di slot machine")
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
            time.sleep(2)
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
            acc_obj = user_balance(username).controler()
            acc_balance = acc_obj.balance
            USERS = acc_obj.user
            print('Berhasil Login')
            print('Loading....')
            time.sleep(2)
            title(USERS)
            main(USERS, acc_balance)

        else:
            print('Username atau pin tidak ditemukan')
            print('Silahkan masukan username dan pin dengan benar')
            print('Jika belum mempunyai akun, silahkan registrasi terlebih dahulu')
            print('Kembali ke beranda.....')
            time.sleep(2)
            welcomer()

class user_balance:
    def __init__(self, user):
        self.user = user
        self.balance = 0

    def controler(self):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3 and row[0] == self.user:
                    self.balance += int(row[2])
        return self



def main(user, acc_balance):
    username = user
    balance = acc_balance

    while balance >= 0:
        print(f"Saldo mu saat ini : Rp.{balance}")
        print('1) Deposit')
        print('2) Taruhan')
        print('3) Exit')
        print('*'*30)
        pilihan = int(input('Masukan pilihan mu: '))

        if pilihan == 1:
            depo = input('Masukan nominal deposit: ')
            if depo.isdigit():
                depo = int(depo)

                list_user = []

                with open(file_path, 'r', newline="") as file:
                    reader = csv.reader(file)
                    for item in reader:
                        list_user.append(item)

                
                found = False
                for i, users in enumerate(list_user):
                    if len(users) >= 3 and users[0] == username:
                        balance_index = int(users[2])
                        new_balance = balance_index + depo
                        list_user[i][2] = str(new_balance)
                        balance = new_balance
                        found = True
                        break

                if found:
                    
                    with open(file_path, 'w', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(list_user)
                    print(f"Deposit berhasil! Saldo baru: Rp.{balance}")
                else:
                    print("User tidak ditemukan.")
            elif '-' in depo:
                print('*'*30)
                print('Masa depo negatif !!')
            else: 
                print('*'*30)
                print('Masukan angka saja!!!')

        elif pilihan == 2:
            if balance <= 0:
                print('Saldo mu 0 kocak!, depo dulu lah')
                continue
            else:
                while balance > 0:
                    bet = input('Ingin taruhan berapa: ')
                    if not bet.isdigit():
                        print('Masukan digit valid')
                        continue
                    elif bet.isdigit():
                        bet = int(bet)
                        if bet < 1000:
                            print('Bet minimal adalah Rp.1000')
                            break
                        elif bet > balance:
                            print('Saldo tidak mencukupi')
                            break
                        else:
                            how_many_spin = input('Ingin melakukan berapa kali spin :')
                            for spin in range(1, int(how_many_spin) + 1):
                                if balance - bet < 0:
                                    print('Saldo tidak mencukupi')
                                    break
                                else:
                                    pass
                                list_user = []

                                with open(file_path, 'r', newline="") as file:
                                    reader = csv.reader(file)
                                    for item in reader:
                                        list_user.append(item)

                                    
                                found = False
                                for i, users in enumerate(list_user):
                                    if len(users) >= 3 and users[0] == username:
                                        balance_index = int(users[2])
                                        new_balance = balance_index - bet
                                        list_user[i][2] = str(new_balance)
                                        balance = new_balance
                                        found = True
                                        break

                                if found:
                                        
                                    with open(file_path, 'w', newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerows(list_user)
                                    print(f"Bet Berhasil!! Saldo baru: Rp.{balance}")
                                else:
                                    print("User tidak ditemukan.")
                                
                                row = list(spin_row())
                                print_row(row)
                                #get_payout(row, bet)
                                jackpot = int(get_payout(row, bet))

                                list_user = []

                                with open(file_path, 'r', newline="") as file:
                                    reader = csv.reader(file)
                                    for item in reader:
                                        list_user.append(item)

                                    
                                found = False
                                for i, users in enumerate(list_user):
                                    if len(users) >= 3 and users[0] == username:
                                        balance_index = int(users[2])
                                        new_balance = balance_index + jackpot
                                        list_user[i][2] = str(new_balance)
                                        balance = new_balance
                                        found = True
                                        break

                                if found:
                                        
                                    with open(file_path, 'w', newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerows(list_user)
                                else:
                                    print("User tidak ditemukan.")
                                    
                                if jackpot > 0:
                                    print('JAAACKKKPOOOTT!!!!')
                                    print(f"Selamat kamu mendapatkan Rp{jackpot}")
                                    
                                else:
                                    print('Maaf kamu belum beruntung')
                            
                                print(f"Balance saat ini Rp.{balance}")
                                next_no = input('Masih ingin main? (y/n) ')
                                next = ['y']
                                no = ['n']
                                
                                if next_no.lower() in next:
                                    continue
                                elif next_no.lower() in no:
                                    break
            
        elif pilihan == 3:
            print('Terima kasih sudah bermain')
            break
        else:
            print('Masukan angka 1 - 3 saja!!')
            continue
if __name__ == '__main__':
    welcomer()
    time.sleep(3)