# grace donath

def encoder(password):
    new_pass = ''
    for num in password:
        new_num = int(num) + 3
        new_pass += str(new_num)
    return new_pass

def decoder(password):
    new_pass = ''
    for num in password:
        new_num = int(num) - 3
        new_pass += str(new_num)
    return new_pass
