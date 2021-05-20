const sum = (ns) => { let acum= 0; for(i=0; i<ns.length; i++){acum += ns[i];} return acum};
 
const numbers = [1, 2, 3, 4, 5]
//multiplicar por dos
// const mult = numbers.map(x => x * 2)
// a pares
// const pairs = numbers.map(x => [x, x])

const pets = [
	{name: 'mumiqui', age: 13, race: 'dog'},
	{name: 'puquini', age: 10, race: 'pig'},
	{name: 'unquini', age: 11, race: 'cat'},
	{name: 'manini', age: 13, race: 'chicken'},
];
//edad promedio
const ages = pets.map(x => x.age)
const res = sum(ages)

