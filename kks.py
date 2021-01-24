import sys

def kks(word):
  from pykakasi import kakasi
  kakasi = kakasi()
  kakasi.setMode('H', 'a')
  kakasi.setMode('K', 'a')
  kakasi.setMode('J', 'a')
  return kakasi.getConverter().do(word)

def main():
  print(kks(sys.argv[1]))

main()  
