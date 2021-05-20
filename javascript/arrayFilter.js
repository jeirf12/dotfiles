const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

const pets = [
	{name: 'mumiqui', age: 13, race: 'dog'},
	{name: 'puquini', age: 10, race: 'pig'},
	{name: 'unquini', age: 13, race: 'cat'},
	{name: 'manini', age: 13, race: 'chicken'},
];

const dogsFiltered = pets.filter(x => x.race == 'dog')
console.log(dogsFiltered)
