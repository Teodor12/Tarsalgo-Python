data_list = []
id_list = []


def feladat_1():
    file = open('lib/ajto.txt')
    for line in file:
        data_list.append(line.strip())


def feladat_2():
    print('2. feladat')
    last_id = ''
    print('Az elso belepo: ' + data_list[0].split(' ')[2])
    for data in data_list:
        db = data.split(' ')
        if db[3] == 'ki':
            last_id = db[2]
    print('Az utolso belepo: ' + last_id)
    print()


def feladat_3():
    output_file = open('athaladas.txt', 'w')
    id_list = [i for i in range(1, 101, 1)]
    for id in id_list:
        counter = 0
        for data in data_list:
            db = data.split(' ')
            if db[2] == str(id):
                counter += 1
        if counter == 0:
            continue
        output_file.write(str(id) + ' ' + str(counter) + '\n')
    output_file.close()


def feladat_4():
    print('4. feladat')
    crossings = open('athaladas.txt', 'r')
    print('A vegen a tarsalgoban voltak: ', end='')
    for i in crossings:
        db = i.split(' ')
        if int(db[1]) % 2 != 0:
            print(db[0], end=' ')
    print('\n')


def feladat_5():
        print('5. feladat')
        hour = '9'
        min = '0'
        max = 0
        is_in = 0
        for i in data_list:
            db = i.split(' ')
            if db[3] == 'be':
                is_in += 1
            else:
                is_in -= 1
            if is_in > max:
                max = is_in
                hour = db[0]
                min = db[1]

        print('Peldaul ' + hour + ':' + min + '-kor voltak legtobben a tarsalgoban.')
        print()


def feladat_6_7_8():
    print('6.feladat')
    id = input('Adja meg a személy azonosítóját! ')
    print()

    print('7. feladat')
    for i in data_list:
        db = i.split(' ')
        if db[2] == id and db[3] == 'be':
            print(db[0] + ':' + db[1],end='-')
        elif db[2] == id and db[3] == 'ki':
            print(db[0] + ':' + db[1],end='\n')

    print()
    print('8. feladat')
    sum_min, in_min, out_min = 0,0,0
    is_in = False
    for i in data_list:
        db = i.split(' ')
        if db[2] == id:
            if db[3] == 'be':
                is_in = True
                in_min = int(db[0]) * 60 + int(db[1])
            else:
                is_in = False
                out_min = int(db[0]) * 60 + int(db[1])
                sum_min += (out_min-in_min)
    if is_in == True:
       sum_min += 15*60 - in_min
       print('A(z) ' + id + '. szemely osszesen ' + str(sum_min) + ' percet volt bent, a megfigyeles vegen a tarsalgoban volt.')
    else:
        print(
            'A(z) ' + id + '. szemely osszesen ' + str(sum_min) + ' percet volt bent, a megfigyeles vegen nem volt a tarsalgoban.')


















feladat_1()
feladat_2()
feladat_3()
feladat_4()
feladat_5()
feladat_6_7_8()
