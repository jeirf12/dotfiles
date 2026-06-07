const users = [
	{id: 1, name: 'jhonfer', lastName: 'ruiz'},
	{id: 2, name: 'pamela', lastName: 'rosero'},
	{id: 2},
]

const compose = (...fns) => x => fns.reduceRight((y, f) => f(y), x)

const capitalize = (data) => data.charAt(0).toUpperCase() + data.slice(1)

// const head = x => x[0]
const completedFieldsRequired = x => {
	let fieldsNew = {
		name: '',
		lastName: '',
	};

	if (x.name && x.lastName)
		return x;

	if (x.name) {
		fieldsNew = {
			name: x.name,
			lastName: '',
		}
	} 

	if (x.lastName) {
		fieldsNew = {
			name: '',
			lastName: x.lastName,
		}
	}

	return fieldsNew;
}
const capitalizeNameFull = x => ({
	name: capitalize(x.name),
	lastName: capitalize(x.lastName),
})
const resultNameFull = x => `${x.name} ${x.lastName}`

//point free
const getNameFull = compose(resultNameFull, capitalizeNameFull, completedFieldsRequired)

const x = users.map(getNameFull)
console.log(x.join('\n'))
