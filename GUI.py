import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

 
qtCreatorFile = "GUI.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 


def inv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        print("Chyba")
    else:
        return x % m


symboly = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""   
   


def Sifruj(znak, klucA, klucB):

    sifra_text = ''
    znak_index = symboly.index(znak.upper())

    sifra_text = symboly[(znak_index * klucA + klucB) % len(symboly)]

    return sifra_text
              

def spaces (sifra, length):
    return ' '.join(sifra[i:i+length] for i in range(0,len(sifra),length)) 


def Desifruj(znak,klucA, klucB):
    modinv = inv(klucA,len(symboly))
    cisty_text = '' 
    znak_index = symboly.index(znak.upper())
    cisty_text = symboly[((znak_index - klucB) * modinv) % len(symboly)]
    return cisty_text




class Sifra(QMainWindow, Ui_MainWindow):
       
    
    def sifruj(self):
        
           text = self.user_text.text()
           
           text = text.replace("Ř","R")
           text = text.replace("Ě","E")
           text = text.replace("Š","S")
           text = text.replace("Ž","Z")
           text = text.replace("Ý","Y")
           text = text.replace("Á","A")
           text = text.replace("Č","C")
           text = text.replace("Í","I")
           text = text.replace("É","E")
           text = text.replace("Ť","T")
           text = text.replace("Ď","D")
           text = text.replace("Ň","N")
           text = text.replace("Ú","U")
           text = text.replace("Ů","U")
           text = text.replace("ř","r")
           text = text.replace("ě","e")
           text = text.replace("š","s")
           text = text.replace("ž","z")
           text = text.replace("ý","y")
           text = text.replace("á","a")
           text = text.replace("č","c")
           text = text.replace("í","i")
           text = text.replace("é","e")
           text = text.replace("ť","t")
           text = text.replace("ď","d")
           text = text.replace("ň","n")
           text = text.replace("ú","u")
           text = text.replace("ů","u")
           text = text.replace(" ","XMEZERAX")
           text = text.replace("0","AA")
           text = text.replace("1","BB")
           text = text.replace("2","CC")
           text = text.replace("3","DD")
           text = text.replace("4","EE")
           text = text.replace("5","FF")
           text = text.replace("6","GG")
           text = text.replace("7","HH")
           text = text.replace("8","ZZ")
           text = text.replace("9","JJ")
    
           text = text.replace("!","")
           text = text.replace("*","")
           text = text.replace("/","")
           text = text.replace("-","")
           text = text.replace(".","")
           text = text.replace(":","")
           text = text.replace("_","")
           text = text.replace("?","")
           text = text.replace("#","")
           text = text.replace(",","")
           text = text.replace("<","")
           text = text.replace(">","")
           
           a = int(self.a_entry.text())
           b = int(self.b_entry.text())

           z = []
           s
           for i in range(0, len(text)):

               if(inv(a,b)):

                    ST = Sifruj(text[i], a, b)
                    z.append(ST)

               else:
                    print("Zadal jsí soudelna cisla")
                    break

           sifra = "" .join(z) 

           self.vstup_text.setText(str(text))
           self.sifra_text.setText(str(spaces(sifra,5)))
        
        
    def desifruj(self):
        
       
            desifrovany_text = self.sifra_text.text()
            desifrovany_text = desifrovany_text.replace(" ","")
            
            
            a = int(self.a_entry.text())
            b = int(self.b_entry.text())
            
            g = []

            for i in range(0,len(desifrovany_text)):
                 OT = Desifruj(desifrovany_text[i],a,b)
                 g.append(OT)
                
            desif_text = "".join(g)

            desif_text = desif_text.replace("XMEZERAX", " ")
            desif_text = desif_text.replace("AA", "0")
            desif_text = desif_text.replace("BB", "1")
            desif_text = desif_text.replace("CC", "2")
            desif_text = desif_text.replace("DD", "3")
            desif_text = desif_text.replace("EE", "4")
            desif_text = desif_text.replace("FF", "5")
            desif_text = desif_text.replace("GG", "6")
            desif_text = desif_text.replace("HH", "7")
            desif_text = desif_text.replace("ZZ", "8")
            desif_text = desif_text.replace("JJ", "9")
            
            self.desifra_text.setText(str(desif_text))
        
        
    def vymaz(self):
         self.a_entry.clear()
         self.b_entry.clear()
         self.vstup_text.clear()
         self.sifr_text.clear()
         self.desifra_text.clear()
         self.user_text.clear()
        
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.SifrujBtn.clicked.connect(self.sifruj)
        self.DesifrujBtn.clicked.connect(self.desifruj)
        self.ClearBtn.clicked.connect(self.vymaz)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sifra()
    window.show()
    sys.exit(app.exec_())

            

    
    
 