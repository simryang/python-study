a1 = b'\x02'
b1 = 'AB'
c1 = 'EF'
c2 = None
d1 = b'\x03'

bb = a1 + bytes(b1.encode()) + bytes(c1.encode()) + d1
bb2 = a1 + bytes(b1.encode()) + bytes(c2.encode()) + d1
print(type(bb), bb)