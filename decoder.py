import quopri

#s = '=D0=9D=D0=90=D0=98=D0=9C. =D0=9F=D0=A0.'
#s1 = bytes(s, 'UTF-8')
#s2 = quopri.decodestring(s1)
#print(s2.decode('UTF-8'))

def decode_str(str):
    str_byte = bytes(str, 'UTF-8')
    str_decode = quopri.decodestring(str_byte)
    return str_decode.decode('UTF-8')

#s = '=09=09=09=09=09=D0=94=D0=9E=D0=91=D0=A0=D0=9E=D0=A4=D0=9B=D0=9E=D0=A2=D0=A1=D0=B0=D0=BB=D0=B0=D1=82'
#s1 = bytes(s, 'UTF-8')
#s2 = quopri.decodestring(s1)
#print(s2.decode('UTF-8'))
