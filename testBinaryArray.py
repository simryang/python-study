binArrayAscii = 'hello'.encode()
binArrayEuckr = '방가방가'.encode('euc-kr')
binArrayUtf8 = '방가방가'.encode('utf-8')
bytesEuckr = bytes('방가방가', encoding='euc-kr')
byteArrayUtf8 = bytearray('방가방가', encoding='utf-8')
print(binArrayAscii.decode(), binArrayAscii)            # 변경 불가
print(binArrayEuckr.decode('euc-kr'), binArrayEuckr)    # 변경 불가
print(binArrayUtf8.decode('utf-8'), binArrayUtf8)       # 변경 불가
print(bytesEuckr.decode('euc-kr'), bytesEuckr)          # 변경 불가
print(byteArrayUtf8.decode('utf-8'), byteArrayUtf8)     # 변경 가능
