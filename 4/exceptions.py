dictionary = {"dog": "Bazyli"}
#  "cat": "Stefan"
try:
    del dictionary["cat"]
except:
    print("Poleciał wyjątek i go złapaliśmy")
else:
    print("Wszystko działa")
finally:
    print("Mimo wszystko robię rzeczy")

try:
    #del dictionary[x]
    del dictionary["cat"]
except KeyError:
    print("Brak kotka w słowniku")
except NameError:
    print("Nie ustawiłeś zmiennej")

x = input("Podaj cyfrę: ")
if not x.isdigit():
    raise TypeError("Miała być cyfra cymbale!")
