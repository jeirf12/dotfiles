import java.util.List;

public class programacionFuncional{
	public static void main(String[] args) {
		List<Integer> numbers = List.of(18, 6, 4, 15, 55, 78, 12, 9, 8);

		/** Función filter: Sirve para filtrar elementos de una lista con condicionales 
		 * en la mayoria de los casos devuelve una lista mas pequeña que la anterior*/
		Long result = numbers.stream().filter(num -> num > 10).count();
		System.out.println("la cantidad de numeros mayores que 10 son: "+result);

		/** Función reduce: Sirve para hacer operaciones basicas de aritmetica como sumas, restas o concatenaciones en String 
		 * esta devuelve el valor ya sea numerico, flotante o cadenas*/
		int result2 = numbers.stream().reduce(0, (acum, num) -> acum + num);
		System.out.println("Suma es: "+result2);

		/** Funcion map: Sirve para modificar cada uno de los elementos de la lista, permitiendo devolver una de igual o menor tamaño
		 * dependiendo de otras operaciones aplicadas, en este caso utilice reduce al igual que las filter, se puede concatenar estos dos tipos de operaciones anteriores*/
		int result3 = numbers.stream().map( x -> x * 2 ).reduce(0, (acum, num) -> acum + num);
		System.out.println("La suma de todo multiplicado por 2 es: "+result3);
	}
}

