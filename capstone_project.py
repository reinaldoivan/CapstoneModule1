#==================================================================================
#CAPSTONE PROJECT
#Academic Scores - Data Nilai Siswa

#by: Ivan Reinaldo
#==================================================================================

from time import sleep
import os
import sys

#region List Data

#list data mahasiswa
listMahasiswa = [
    {
        'NIM': '08010001',      #nomor induk mahasiswa - unique key [immutable]
        'nama':'Alek',          #nama
        'gender':'Pria',        #gender
        'fakultas': 'Teknik',   #fakultas [immutable]
        'tahun':'2008',         #tahun mendaftar [immutable]
        'IPK': 3.8,             #IPK 
        'grade':'A',            #grade [ikut berubah ketika IPK diganti]
        'shown':True            #apakah data baru ditambah/diupdate [hanya diganti di sistem]
    },
    {
        'NIM': '12030002', 'nama':'Thomas', 'gender':'Pria',
        'fakultas': 'Desain', 'tahun':'2012',
        'IPK': 2.67, 'grade':'C',
        'shown':True
    },
    {
        'NIM': '11010003', 'nama':'Dhimas','gender':'Pria',
        'fakultas': 'Teknik','tahun':'2011',
        'IPK': 3.00,'grade':'B',
        'shown':True
    },
    {
        'NIM': '15040004','nama':'Joanna','gender':'Wanita',
        'fakultas': 'Bisnis','tahun':'2015',
        'IPK': 3.97,'grade':'A',
        'shown':True
    },
]

#NOTE
#NIM merupakan unique key sehingga tidak bisa diganti
#Fakultas dan tahun mendaftar juga tidak bisa diganti
#karena NIM tersusun dari kedua variable tersebut (akan dijelaskan lebih lanjut)

#list fakultas
listFakultas = ['Teknik', 'Ekonomi', 'Desain', 'Bisnis', 'Humaniora']

#endregion

#region Additional Functions

#mengecek apakah data berupa angka sudah sesuai ketentuan
def checkDataAngka(angka, batasKiri, batasKanan):
    #cek apakah input hanya mengandung angka
    if(angka.isnumeric()):
        if(int(angka) >= batasKiri and int(angka) <= batasKanan):
            return True
        else:
            return False
    else:
        return False

#mengecek apakah inputan user berbentuk float
def checkFloat(angka):
    try:
        float(angka)
        return True
    except ValueError:
        return False

#mengecek apakah IPK sudah sesuai ketentuan
def checkIPK(IPK):
    if(checkFloat(IPK) == True):
        roundedIPK = round(float(IPK), 2)
        if(roundedIPK >= 0 and roundedIPK <= 4):
            return True
        else:
            return False
    else:
        return False

#mengecek apakah NIM ada di dalam list dan mengebalikkan index NIM
def checkNIM(angkaNIM):
    for i in range(len(listMahasiswa)):
        if(angkaNIM == listMahasiswa[i]['NIM']):
            return i
    return -1   #jika tidak ada di dalam index, return -1

#input NIM, pengecekkan, serta print informasi
def checkNIM_withPrint():
    nomorMhs = input('Masukkan NIM: ')
    index = checkNIM(nomorMhs)

    if(index != -1):
        print(f'\nData Mahasiswa dengan NIM {nomorMhs}')
        reportData(index, False)
        print('')
        return index
    else:
        print('\n***Data Mahasiswa tidak ditemukan***\n')
        return -1

#merubah penulisan nomor belakang untuk NIM
def convertNomor(nomor):
    temp = int(nomor)

    if(temp < 10):
        return '000'+str(temp)
    elif(temp < 100):
        return '00'+str(temp)
    elif(temp < 1000):
        return '0'+str(temp)
    else:
        return str(temp)

#assign grade berdasarkan inputan IPK
def assignGrade(IPK):
    if(IPK >= 3.30):
        return 'A'
    elif(IPK >= 2.70):
        return 'B'
    elif(IPK >= 1.70):
        return 'C'
    elif(IPK >= 1.00):
        return 'D'
    else:
        return 'E'

#prompt konfirmasi apakah data akan diupdate
def updateConfirmation(namaKey, valueBaru, nomorIndex):
    while True:
        konfirmasi = input('Apakah Data akan di Update? (Y/N): ')

        if(konfirmasi.lower() == 'y'):
            listMahasiswa[nomorIndex][namaKey] = valueBaru
            listMahasiswa[nomorIndex]['shown'] = False  #untuk menandakan data baru di update

            #khusus key IPK, maka grade juga akan di update
            if(namaKey == 'IPK'):
                gradeBaru = assignGrade(valueBaru)
                listMahasiswa[nomorIndex]['grade'] = gradeBaru

            print('Data berhasil di Update!\n')
            print(f'Data Mahasiswa dengan NIM {listMahasiswa[nomorIndex]["NIM"]} setelah update:')
            reportData(nomorIndex, False)
            print('')
            holdPrint()
            break

        elif(konfirmasi.lower() == 'n'):
            print('Data batal di Update\n')
            break

#print main menu
def showMainMenu():
    #List di sort berdasarkan NIM setiap masuk ke main menu
    if(len(listMahasiswa) > 0):
        listMahasiswa.sort(key=lambda d: d['NIM'])

    os.system('cls') #clear screen setiap ganti menu/sub menu
    print('''==========Data Mahasiswa Kampus Efexers===========
    
1. Report Data Mahasiswa
2. Menambahkan Data Mahasiswa
3. Mengubah Data Mahasiswa
4. Menghapus Data Mahasiswa
5. Exit''')

#print list fakultas
def showFacultyList():
    print('\nList Fakultas:')
    for i in range(len(listFakultas)):
        print(f'0{i+1}: {listFakultas[i]}', end='\t| ')
    print()

#prompt konfirmasi setelah print data dan sebelum user melanjutkan aplikasi
def holdPrint():
    input('Tekan key apapun untuk melanjutkan...')
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

#endregion

#region Main Functions

#membaca data mahasiswa dari list [FITUR READ]
def reportData(index, penomoran = True, checkShown = False):
    #cek apakah data yang di print baru ditambah/diupdate
    star = ''
    if(checkShown):
        if (listMahasiswa[index]['shown'] == False):
            listMahasiswa[index]['shown'] = True
            star = '*'

    #tambahkan penomoran di depan jika diperlukan
    if(penomoran):
        print(f'{star}{index+1}. ', end='')

    print(f"NIM: {listMahasiswa[index]['NIM']} \t| Nama: {listMahasiswa[index]['nama']}" +
    f" \t| Gender: {listMahasiswa[index]['gender']}  \t| Fakultas: {listMahasiswa[index]['fakultas']}" + 
    f" \t| IPK: {listMahasiswa[index]['IPK']:.2f}  \t| Grade: {listMahasiswa[index]['grade']}")

#menambah data mahasiswa ke dalam list [FITUR CREATE]
def createData():
    #NIM terlebih dahulu disusun dari input user, baru kemudian dicek apakah sudah terdaftar
    print('\nData-data berikut digunakan untuk penyusunan NIM')
    
    #Input data tahun pendaftaran [numeric]
    while True:
        tahun = input('Masukkan tahun mahasiswa terdaftar [2000-2021]: ')
        if(checkDataAngka(tahun, 2000, 2021) == True):
            break

    #Input data fakultas [numeric]
    showFacultyList()
    while True:
        kodeFakultas = input('Masukkan kode Fakultas [angka di sebelah kiri]: ')
        if(checkDataAngka(kodeFakultas, 1, (len(listFakultas))) == True):
            fakultas = listFakultas[int(kodeFakultas)-1]
            break
    
    #Input data 4 angka di belakang NIM [numeric]
    #Penyusunan NIM: 2 angka belakang tahun mendaftar + kode fakultas + 4 angka berdasarkan input user
    #Contoh: 2025, Teknik, 103 --> 25010103
    while True:
        angkaBelakang = input('Masukkan nomor mahasiswa [1-9999]: ')
        if(checkDataAngka(angkaBelakang, 1, 9999) == True):
            NIM_baru = tahun[-2:] + (str(0) + kodeFakultas) + convertNomor(angkaBelakang)
            print(f'\nNIM baru: {NIM_baru}')

            #cek apakah NIM sudah terdaftar
            if(checkNIM(NIM_baru) == -1):
                print('NIM berhasil dibuat! Silahkan lanjutkan mengisi data selanjutnya\n')
                break
            else:
                print('NIM sudah terdaftar. Masukkan ulang nomor mahasiswa')

    #Input data nama [alphabet]
    while True:
        nama = input('Masukkan nama [hanya text]: ')
        if(nama.replace(' ','').isalpha()):
            nama = nama.lower().title()
            break

    #Input data gender [alphabet - Pria/Wanita]
    while True:
        gender = input('Masukkan gender [Pria/Wanita]: ')
        if(gender.lower() == 'pria' or gender.lower() == 'wanita'):
            gender = gender.lower().capitalize()
            break

    #Input data IPK [decimal]
    while True:
        IPK = input('Masukkan IPK [0.00-4.00]: ')
        if(checkIPK(IPK) == True):
            break
    IPK = round(float(IPK), 2)

    #Assign grade berdasarkan IPK yang telah diinput [char]
    grade = assignGrade(IPK)

    #tampilkan inputan user
    print(f"\nData mahasiswa baru:\nNIM: {NIM_baru} \t| Nama: {nama}" +
    f" \t| Gender: {gender}  \t| Fakultas: {fakultas}" + 
    f" \t| IPK: {IPK:.2f}  \t| Grade: {grade}\n")

    while True:
        konfirmasi = input('Apakah Data baru sudah sesuai dan akan disimpan? (Y/N): ')

        if(konfirmasi.lower() == 'y'):
            listMahasiswa.append({'NIM': NIM_baru, 'nama': nama, 'gender': gender,
                                  'fakultas': fakultas, 'tahun': tahun,
                                  'IPK': IPK, 'grade': grade,
                                  'shown': False
                                 })
                                 
            print('Data berhasil disimpan!\n')
            #holdPrint()
            break
        elif(konfirmasi.lower() == 'n'):
            print('Data batal disimpan\n')
            #holdPrint()
            break

#mengupdate data mahasiswa di dalam list [FITUR UPDATE]
def updateData():
    print()
    indexNIM = checkNIM_withPrint()

    if(indexNIM != -1):
        #cek apakah user ingin melanjutkan update data
        while True:
            exit = False
            konfirmasi = input('Tekan Y jika ingin lanjut Update data atau N jika ingin cancel Update (Y/N): ')

            if(konfirmasi.lower() == 'y'):
                while True:
                    keterangan = input('Masukkan keterangan yang ingin di Update [Nama/Gender/IPK]: ')
                    temp = keterangan.lower()

                    if(temp == 'nim' or temp == 'fakultas' or temp == 'tahun' or temp == 'grade'):
                        print('Keterangan yang dipilih tidak dapat diubah. Silahkan pilih keterangan lain')
                    elif(temp == 'nama'):
                        #Input data nama baru [alphabet]
                        while True:
                            namaBaru = input('Masukkan nama baru [hanya text]: ')
                            if(namaBaru.replace(' ','').isalpha()):
                                namaBaru = namaBaru.lower().title()
                                updateConfirmation('nama',namaBaru,indexNIM)
                                exit = True
                                break
                    elif(temp == 'gender'):
                        #Input data gender baru [alphabet - Pria/Wanita]
                        while True:
                            genderBaru = input('Masukkan gender baru [Pria/Wanita]: ')
                            if(genderBaru.lower() == 'pria' or genderBaru.lower() == 'wanita'):
                                genderBaru = genderBaru.lower().capitalize()
                                updateConfirmation('gender',genderBaru,indexNIM)
                                exit = True
                                break
                    elif(temp == 'ipk'):
                        #Input data IPK baru [decimal]
                        while True:
                            IPK_baru = input('Masukkan IPK baru[0.00-4.00]: ')
                            if(checkIPK(IPK_baru) == True):
                                IPK_baru = round(float(IPK_baru), 2)
                                updateConfirmation('IPK',IPK_baru,indexNIM)
                                exit = True
                                break
                    
                    if(exit):
                        break
            elif(konfirmasi.lower() == 'n'):
                print('Data batal di Update\n')
                break

#menghapus data mahasiswa di dalam list [FITUR DELETE]
def deleteData():
    print()
    indexNIM = checkNIM_withPrint()

    if(indexNIM != -1):
        #cek apakah user ingin menghapus data
        while True:
            konfirmasi = input('Apakah Data akan di Delete? (Y/N): ')
            if(konfirmasi.lower() == 'y'):
                listMahasiswa.pop(indexNIM)
                print('Data berhasil di Delete!\n')
                break
            elif(konfirmasi.lower() == 'n'):
                print('Data batal di Delete')
                break

#endregion

#=================================
#Start here
#Main Menu
showMainMenu()

while True:
    while True:
        menu = input('Silahkan Pilih Main Menu [1-5]: ')

        #Menu 1: Report Data Mahasiswa
        if menu == '1':
            os.system('cls')
            while True:
                print('=====================\nReport Data Mahasiswa\n=====================')
                print('1. Report Seluruh Data\n2. Report Data Tertentu\n3. Kembali ke Menu Utama')
                
                while True:
                    subMenu = input('Silahkan Pilih Sub Menu Read Data [1-3]: ')

                    #Sub Menu 1: Report Seluruh Data
                    if subMenu == '1':
                        if(len(listMahasiswa) > 0):
                            print('\n=================\nDaftar Mahasiswa:\n=================')
                            for i in range(len(listMahasiswa)):
                                reportData(i, checkShown=True)
                            print('\n* = Data baru ditambah/diupdate\n')
                            holdPrint()
                        else:
                            print('\n***Tidak ada Data Mahasiswa yang terdaftar***\n')
                        
                        break

                    #Sub Menu 2: Report Data Tertentu
                    elif subMenu == '2':
                        if(len(listMahasiswa) > 0):
                            print()
                            if(checkNIM_withPrint() != -1):
                                holdPrint()
                        else:
                            print('\n***Tidak ada Data Mahasiswa yang terdaftar***\n')
                        
                        break
                    
                    #Sub Menu 3: Kembali ke Menu Utama
                    elif subMenu == '3':
                        break
                
                if(subMenu == '3'):
                    showMainMenu()
                    break

        #Menu 2: Menambahkan Data Mahasiswa
        elif menu == '2':
            os.system('cls')
            while True:
                print('=======================\nMenambah Data Mahasiswa\n=======================')
                print('1. Tambah Data Mahasiswa\n2. Kembali ke Menu Utama')
                
                while True:
                    subMenu = input('Silahkan Pilih Sub Menu Create Data [1-2]: ')

                    #Sub Menu 1: Tambah Data Mahasiswa
                    if subMenu == '1':
                        createData()
                        break

                    #Sub Menu 2: Kembali ke Menu Utama
                    elif subMenu == '2':
                        break
                
                if(subMenu == '2'):
                    showMainMenu()
                    break

        #Menu 3: Mengubah Data Mahasiswa
        elif menu == '3':
            os.system('cls')
            while True:
                print('=======================\nMengubah Data Mahasiswa\n=======================')
                print('1. Ubah Data Mahasiswa\n2. Kembali ke Menu Utama')
                
                while True:
                    subMenu = input('Silahkan Pilih Sub Menu Update Data [1-2]: ')

                    #Sub Menu 1: Ubah Data Mahasiswa
                    if subMenu == '1':
                        if(len(listMahasiswa) > 0):
                            updateData()
                        else:
                            print('\n***Tidak ada Data Mahasiswa yang terdaftar***\n')
                        break

                    #Sub Menu 2: Kembali ke Menu Utama
                    elif subMenu == '2':
                        break
                
                if(subMenu == '2'):
                    showMainMenu()
                    break

        #Menu 4: Menghapus Data Mahasiswa
        elif menu == '4':
            os.system('cls')
            while True:
                print('========================\nMenghapus Data Mahasiswa\n========================')
                print('1. Hapus Data Mahasiswa\n2. Kembali ke Menu Utama')
                
                while True:
                    subMenu = input('Silahkan Pilih Sub Menu Hapus Data [1-2]: ')

                    #Sub Menu 1: Hapus Data Mahasiswa
                    if subMenu == '1':
                        if(len(listMahasiswa) > 0):
                            deleteData()
                        else:
                            print('\n***Tidak ada Data Mahasiswa yang terdaftar***\n')
                        break

                    #Sub Menu 2: Kembali ke Menu Utama
                    elif subMenu == '2':
                        break

                if(subMenu == '2'):
                    showMainMenu()
                    break

        #Menu 5: Exit
        elif menu == '5':
            print('Terimakasih dan sampai jumpa!\n\n')

            #aplikasi akan ditutup setelah 3 detik
            for i in range(3,0,-1):
                print(f'Aplikasi akan ditutup dalam {i} detik', end='\r')
                sleep(1)
            os.system('cls')
            quit()

        break