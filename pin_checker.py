import csv

file_path = 'user.csv'

def checker():
    print('Masukan username yang ingin di cek pin nya')
    while True:
        username = input('username : ')
        if username.isdigit():
            print('Masukan username dengan benar !')
        elif '-' in username:
            print('Masukan username dengan benar !')
        else:
            username = username.capitalize()
            found = False
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if username in row:
                        found = True
                        break
            if found:
                print(f"Pin mu adalah '{row[1]}' ")
                return True
            else:
                print('Username tidak ditemukan!')
                return False
            

if __name__ == '__main__':
    checker()