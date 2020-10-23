import webbrowser
#importing required library

def map1(latitude, longitude):
      webbrowser.open(f'https://www.google.com/maps/place/{latitude} {longitude}')
      print("You are being redirected to Google Maps")

def map2(address):
      webbrowser.open(f'https://www.google.com/maps/place/{address}')
      print("You are being redirected to Google Maps")

#defined required functions

print('''
Select any option:
      1.Address
      2.Latitude and Longitude
''')
#question output

selection = int(input('>>   '))
if selection == 1 :
      address = input("Give the address [with spaces] >> ")
      map2(address)

elif selection == 2 :
      latitude = input("Latitude >>  ")
      longitude = input("Longitude >>  ")
      map1(latitude, longitude)

else :
      print("That was a wrong input.Try again!")
#program ends
