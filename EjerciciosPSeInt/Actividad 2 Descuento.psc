Algoritmo ACTIVIDAD2
	
 //En una fábrica de computadoras se planea ofrecer a los clientes un descuento que 
//dependerá del número de computadoras que compre. Si las computadoras son menos de 
//cinco se les dará un 10% de descuento sobre el total de la compra; si el número de 
//computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20% de descuento; 
	//y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $11,000
	
 		Definir compus Como Entero
		Definir totalcompra Como Real
		
		// Ingresa la cantidad de computadoras a comprar
		
		Escribir 'Ingrese cantidad de computadoras a comprar: '
		Leer compus
		
		Si (compus >= 10) Entonces
			Escribir "40 % de descuento"
			totalcompra = compus * 11000 * 0.6
			Escribir "Total: "
			Escribir totalcompra
		
		SiNo
			Si (compus >= 5) Entonces
				Escribir "20 % de descuento"
				totalcompra = compus * 11000 * 0.8
				Escribir "Total: "
				Escribir totalcompra
			SiNo
				Escribir "10 % de descuento"
				totalcompra = compus * 11000 * 0.9
				Escribir "Total: "
				Escribir totalcompra
			FinSi
		FinSi	
	
FinAlgoritmo
