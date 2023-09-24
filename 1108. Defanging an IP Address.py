def defangIPaddr(address):
    return address.replace('.', '[.]')


print(defangIPaddr(address = "255.100.50.0"))