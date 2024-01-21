if __name__ == '__main__':
    import os
    import time
    import sys
    from AES import AES
    from threading import *
    while True:
        print('Please select usage mode AES (encryption or decryption)')
        user_input = input()
        if user_input not in ['encryption', 'decryption']:
            print('Action denied')
            continue
        else:
            break
    print()

    while True:
        print('Enter full name of file')
        input_path = os.path.abspath(input())

        if os.path.isfile(input_path):
            break
        else:
            print('This is not a file')
            continue
    print()

    while True:
        print(
            'Enter your Key for encryption/decryption. The Key must be less than 16 symbols.')
        key = input()

        if len(key) > 16:
            print('Too long Key. Imagine another one')
            continue

        for symbol in key:
            if ord(symbol) > 0xff:
                print('That key won\'t work. Try another using only latin alphabet and numbers')
                continue

        break
    def loading():
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                     "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.36)
            sys.stdout.write("\r" "Loading:" + animation[i % len(animation)])
            sys.stdout.flush()
        print()

    def co():

        with open(input_path, 'rb') as f:
            data = f.read()

        if user_input == 'encryption':
            crypted_data = []
            temp = []
            for byte in data:
                temp.append(byte)
                if len(temp) == 16:
                    crypted_part = AES().encrypt(temp, key)
                    crypted_data.extend(crypted_part)
                    del temp[:]
            else:
                if 0 < len(temp) < 16:
                    empty_spaces = 16 - len(temp)
                    for i in range(empty_spaces - 1):
                     temp.append(0)
                    temp.append(1)
                    crypted_part = AES().encrypt(temp, key)
                    crypted_data.extend(crypted_part)

            out_path = os.path.join(os.path.dirname(input_path), 'encrypt_' + os.path.basename(input_path))

            with open(out_path, 'xb') as ff:
                ff.write(bytes(crypted_data))

        else:
            decrypted_data = []
            temp = []
            for byte in data:
                temp.append(byte)
                if len(temp) == 16:
                    decrypted_part = AES().decrypt(temp, key)
                    decrypted_data.extend(decrypted_part)
                    del temp[:]
            else:
                if 0 < len(temp) < 16:
                    empty_spaces = 16 - len(temp)
                    for i in range(empty_spaces - 1):
                        temp.append(0)
                    temp.append(1)
                    decrypted_part = AES().encrypt(temp, key)

            out_path = os.path.join(os.path.dirname(input_path), 'decrypt_' + os.path.basename(input_path))


            with open(out_path, 'xb') as ff:
                ff.write(bytes(decrypted_data))

        print('New file here:', out_path)


    t1 = Thread(target=loading)
    t2 = Thread(target=co)
    t1.start()
    t2.start()
