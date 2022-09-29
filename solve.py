crypt = 'cb57ba706aae5f275d6d8941b7c7706fe261b7c74d3384390b691c3d982941ac4931c6a4394a1a7b7a336bc3662fd0edab3ff8b31b96d112a026f93fff07e61b'

def key1_mod_func(a):
  return ((a ^ ((a << 1) | (a & 1))) & 0xff)

def key2_mod_func(a):
  return ((a ^ ((a >> 5) | (a << 3))) & 0xff)

values = [0xcb]
for byte in [crypt[126-x: 128-x] for x in range(0, len(crypt), 2)]:
  for key1 in range(0x80):
    if (key1_mod_func(key1) + key2_mod_func(values[-1])) % 256 == int(byte, 16):
      values.append(key1)
      break

string = ''.join([chr(a) for a in values[::-1]][:-1])
print(string)
