def esconde(msg):
  s = ''
  for c in msg: s = s + chr(ord(c) + 30000)
  return s

def mostra(msg):
  s = ''
  for c in msg: s = s + chr(ord(c) - 30000)
  return s
