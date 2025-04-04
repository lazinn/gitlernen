git checkout -b feature/time

def begruessung(name:str):
	print("Hallo", name, "!")

def tschuess(name:str):
	print("Auf Wiedersehen,", name, "!")

def saytime():
print("Es ist "+str(datetime.datetime.now().strftime('%H:%M:%S')))

name = input("Bitte geben Sie unbedingt Namen ein: ")
begruessung(name)
saytime()
tschuess(name)

