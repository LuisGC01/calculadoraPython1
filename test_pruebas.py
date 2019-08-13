from calculadora import calculadora
c=calculadora()
def test_suma():
	assert c.sumar(1,3)==4

def test_resta():
	assert c.restar(3,1)==2

def test_multiplicacion():
	assert c.multiplicar(1,4)==4

def test_division():
	assert c.dividir(4,4)==1
