def suhu(convert):
    convert [celtokel, celtofa, fatokel, fatokel]:
  celtokel = float (input ('Masukan nilai Celcius-Kelvin : '))
  celtofa  = float (input ('Masukan Nilai Celcius-Fahrenhait : '))
  fatocel  = float (input ('Masukan Nilai Fahrenhait-celcius  : '))
  fatokel  = float (input ('Masukan Nilai Fahrenhait-kelvin: '))
  totalinput = int (input ('total Input : '))

if totalinput ==1:
    return celtokel + 273.15
elif totalinput ==2:
    return celtofa (9/5) * 32
elif totalinput ==3:
    return (fatocel -32) * 5/9
elif operasi ==41:
    return ((fatokel - 32) / 1.8 ) + 273.15
(suhu('convert'))