// funcion reducer
// const reducer = (collector, valueNow) => newCollector
//

// const redu = [1, 2].reduce((acc, el) => acc + el, 0)

const numbers = [1, 2, 3, 4, 5]
const res = numbers.reduce((acc, el) => acc + el, 0)

const pets = [
	{name: 'mumiqui', age: 13, race: 'dog'},
	{name: 'puquini', age: 10, race: 'pig'},
	{name: 'unquini', age: 11, race: 'cat'},
	{name: 'manini', age: 13, race: 'chicken'},
];

const indexed = pets.reduce((acc, el) => ({
	...acc,
	[el.name]: el,
}), {})

const nested = [1, [2, 3], 4, [5]]
const plane = nested.reduce((acc, el) => acc.concat(el), [])
console.log(plane)
