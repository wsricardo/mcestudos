# Seletiva Hackaton Facebook 2013 (45min)
# Dado dois números inteiros n e k positivos
# Gerar os inteiros binários entre 0 e 2**n - 1, inclusive
# Ordenar em ordem descrescente de acordo com o número
# de 1s existentes e retornar o k-ésimo elemento da lista
# Exemplo, para n = 3 e k = 5
# ['0b111', '0b11', '0b101', '0b110', '0b1', '0b10', '0b100', '0b0']
# O quinto elemento é '0b1'
def hack(n, k):
  def uns(s): return s.count('1')
  b = []
  for x in range(2**n): b.append(bin(x))
  b.sort(key=uns, reverse=True)
  return b[k-1]

def hack1(n, k):
  return sorted(
    [bin(x) for x in range(2**n)],
    key=lambda s: s.count('1'),
    reverse=True)[k-1]
print (hack1(3, 5))
