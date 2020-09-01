import os, sys
import shutil

"""
=======================
dir[-1] = '/' (deve terminar com '/')

move arquivos que contenham o formato:
 "name_ddmm2020.formato"
para pastas no diretório:
 dir + "ddmm2020"

=======================
"""
def numerico(s):
 try:
  float(s)
  return True
 except:
  return False

def encontra_datas(dir):
 datas = []
 for arq in arqs:
  if '2020' in arq: 
   s = arq.split('2020')[0].split('_')[-1]
   if len(s) == 4 and numerico(s):
    if s+'2020' not in datas:
     datas.append(s+'2020')
 # cria as pastas no formato: dir + "ddmm2020"
 for d in datas:
  diretorio = os.path.join(dir, d)
  os.mkdir(diretorio)
 
 return datas

def move(dir, newdir, arq):
 d_ = dir+newdir+'/'
 i = dir+arq
 f = d_ + arq
 print("d_ = {}, i = {}, f = {}, ({})".format(d_,i,f,arq))

def encontra_arqs(dir):
 arqs = []
 for f in os.listdir(dir):
  if '.' in f:
   arqs.append(f)
 return arqs

def main(dir):
 arqs = encontra_aqrs(dir)
 datas = encontra_datas(dir)
 
 for arq in arqs:
  if '2020' in arq:
   s= arq.split('2020')[0].split("_")[-1]
   d_ = dir+ arq
   try: 
    if len(s)==4 and arq in d_: # |ddmm|=4
     move(s+'2020', arq)
     print(f" (SUCESS) ({arq}) in {dir+s+'/'}")import os, sys
import shutil
import argparse

"""
=======================
dir[-1] = '/' (deve terminar com '/')

move arquivos que contenham o formato:
 "name_ddmm2020.formato"
para pastas no diretório:
 dir + "ddmm2020"

=======================
"""
def numerico(s):
 try:
  float(s)
  return True
 except:
  return False

def encontra_datas(dir, arqs):
 datas = []
 for arq in arqs:
  if '2020' in arq: 
   s = arq.split('2020')[0].split('_')[-1]
   if len(s) == 4 and numerico(s):
    if s+'2020' not in datas:
     datas.append(s+'2020')
 # cria as pastas no formato: dir + "ddmm2020"
 for d in datas:
  diretorio = os.path.join(dir, d)
  os.mkdir(diretorio)
 
 return datas

def move(dir, newdir, arq):
 d_ = dir+newdir+'/'
 i = dir+arq
 f = d_ + arq
 print("d_ = {}, i = {}, f = {}, ({})".format(d_,i,f,arq))
 os.rename(i,f)
 shutil.move(i,f)
 os.replace(i,f)

def encontra_arqs(dir):
 arqs = []
 for f in os.listdir(dir):
  if '.' in f:
   arqs.append(f)
 return arqs

def main(dir):
 arqs = encontra_arqs(dir)
 datas = encontra_datas(dir, arqs)
 
 for arq in arqs:
  if '2020' in arq:
   s= arq.split('2020')[0].split("_")[-1]
   d_ = dir+ arq
   try: 
    if len(s)==4 and arq in d_: # |ddmm|=4
     move(dir, s+'2020', arq)
     print(f" (SUCESS) ({arq}) in {dir+s+'/'}")
   except Exception as e:
    print(f" (failed) (arq {arq} ) com erro {e}")
if __name__ == "__main__":
 parser = argparse.ArgumentParser(description='input')
 parser.add_argument('Path', metavar='path', type=str, help='diretório de input, deve terminar com barra')
 arqs = parser.parse_args()
 path_input = arqs.Path

 if not os.path.isdir(path_input):
  print('Diretório inexistente!')

 main(path_input)
 
