
# importing module from different folders (modules are .py files )
import sys
sys.path.append(r"/home/dai/Documents/test/modules")

import module3 as m3 # import module as alis name 

m3.f3()
m3.f4()

import module # import module 
module.f2()
module.f1()

import module as m1

m1.f2()
m1.f1()

from module import f1 # importin particular function from module 
f1()
import package.pakmodule as modpak # calling module from within a package 

#import package.pakmodule

modpak.f1pak()
modpak.f2pak()

dir(modpak)

