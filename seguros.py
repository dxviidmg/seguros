#!/usr/bin/env python3

def preguntas():
	pregunta = input("")
	return pregunta

def calculo(plan, alcohol, lentes, enfermedad, edad):
	if (plan == "A" or plan == "B") and edad >= 0:
		if plan == "A":
			cuotaBase = 950
		else:
			cuotaBase = 1200

		if alcohol == "n" and lentes == "n" and enfermedad == "n" and edad < 40:
			cuotaTotal = cuotaBase * 1.1
		else: 
			if alcohol == "s":
				cAlcohol = cuotaBase * 0.1
			else:
				cAlcohol = 0
			if lentes == "s":
				cLentes = cuotaBase * 0.05
			else:
				cLentes = 0
			if enfermedad == "s":
				cEnfermedad = cuotaBase * 0.05
			else:
				cEnfermedad = 0
			if edad > 40:
				cEdad = cuotaBase * 0.2
			else:
				cEdad = 0
			cuotaTotal = cuotaBase + cAlcohol + cLentes + cEnfermedad + cEdad
		print(cuotaTotal)
	else:
		print("Error al insertar datos")

def main():
	print("Plan: A. Cuota base: 950")
	print("Plan: B. Cuota base: 1200")
	print("¿Indique el plan de seguro que desea?")
	plan = preguntas()

	print("¿Ingiere alcohol? s/n")
	alcohol = preguntas()
	print("¿Usa lentes? s/n")
	lentes = preguntas()
	print("¿Padece de alguna enfermedad degenerativa? s/n")
	enfermedad = preguntas()
	print("Edad: ")
	edad = int(preguntas())

	calculo(plan, alcohol, lentes, enfermedad, edad)

main()