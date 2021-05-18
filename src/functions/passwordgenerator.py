import os

class PasswordGenerator:
    def __init__(self, passtr):
        self.passtr = passtr

    def parse_passtr(self):
        tempstr = self.passtr
        passwargs = []
        charstrings = tempstr.split("|")
        for charstring in charstrings:
            concatchars = (charstring.replace(',', '').replace(' ', ''))
            passwargs.append(concatchars)
        return tuple(passwargs)


    def convert_tuple(self, tup):
        str =  ''.join(tup)
        return str

    def product(self, txtfle):
        passwstrs = self.parse_passtr()
        with open(os.getcwd()+'\\dictionaries\\'+txtfle+'.txt', 'w') as pswd:
            pools = [tuple(pool) for pool in passwstrs]
            result = [[]]
            for pool in pools:
                if pool == ():
                    continue
                result = [x+[y] for x in result for y in pool]
            for prod in result:
                print(prod)
                pswd.write(self.convert_tuple(tuple(prod))+'\n')

# tempstr = "Z|d|1,2,3|1,2,3|1,2,3|1,2,3|1,2,3|!|||||"

# passgen = PasswordGenerator(tempstr)
# passgen.product()