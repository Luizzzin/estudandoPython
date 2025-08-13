eng2sp = dict()

eng2sp['one'] = 'uno'
#isso funciona tambem:

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}
print(eng2sp)

print('one' in eng2sp)

valores = eng2sp.values()
print('uno' in valores)

print(len(eng2sp))

