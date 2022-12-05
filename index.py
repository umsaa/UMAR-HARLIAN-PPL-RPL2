# Belajar pewarisan (interitance)
# 3 objek = orang , pelajar , pekerja 
# masing masing mempunyai nama , asal , kemampuan untuk introduce ur selp
# pelajar  disekolah , pekerja di kantor

class orang :
   def __init__(self , nama , asal):
    self.nama = nama
    self.asal = asal

   def perkenalan(self):
       print( 'perkenalkan nama saya (self.nama dari { self.asal})' )

class pelajar (orang):
      #sekolahnha Dimana
      def__init__(self , nama , asal )
      orang.__init__(self, nama, asal)
      self.sekolah = sekolah
pass

class pekerja (orang):
    pass

rafi = orang('rafi','medan')
rafi.perkenalan()

arya = pekerja
arya.perkenalan()
print("saya bekerja di .arya    ")