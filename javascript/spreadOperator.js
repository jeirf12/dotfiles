const cat = {
	name: 'chanchito',
	age: 15,
}

// los tres puntos indica una copia del arreglo en este caso
// si se hace de la forma asignacion como se muestra abajo
// modificaria los dos arreglos en este caso con el nombre lala
const cat2 = { ...cat }

// version asignacion a referencia
// const cat2 = cat

cat2.name = 'lala'

const cats = [cat, cat2]

console.log(cats)
