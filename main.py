def zpracuj_rc(rc):
    '''vrátí zjištěné hodnoty jako n-tici ve formátu (rok, měsíc, den, pohlaví'''
    
    if len(rc) != 10: #10 znaku
        raise ValueError('nespravne zadane rc, rc musi mit 10 znaku') 
    
    if int(rc) % 11 != 0:     #delitelne 11
        raise ValueError('nespravne zadane rc / neni delitelne 11')
       
    rok = int(rc[0:2])
    if rok >= 54:
        rok += 1900
    else:
        rok += 2000
    
    mesic = int(rc[2:4])
    #měsíc je v rozsahu 1-12 nebo 51-62 x Error:
    if not (1<= mesic <= 12) and not (51<= mesic <= 62):
        raise ValueError('nespravne zadane rc / mesic') 
    elif mesic > 50:
        mesic = mesic - 50

    den = int(rc[4:6])
    #den je v rozsahu 1-31
    if not (1<= den <= 31):
        raise ValueError('nespravne zadane rc / den')

    pohlavi = rc[2]
    if rc[2] in ['5', '6']:
        pohlavi ='zena'
    else:
        pohlavi = 'muz'

    return rok, mesic, den, pohlavi
    

class Clovek:
    def __init__(self, jmeno, prijmeni, rc):
        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()
        self.inicialy = self.jmeno[0] + self.prijmeni[0]
        self.rc = zpracuj_rc(rc)
        self.rok, self.mesic, self.den, self.pohlavi = self.rc
        
    def kdo_jsi(self):
        print(f'Ahoj, jmenuju se {self.jmeno} {self.prijmeni}, me inicialy jsou {self.inicialy} a jsem {self.pohlavi}, rok meho narozeni je {self.rok} a narozeniny mam {self.den}. {self.mesic}.')

osoba = Clovek('AnnA', 'novacKOVa','9057121238')
#osoba = Clovek('jan', 'mAlý', '0007021234')
(osoba.kdo_jsi())
