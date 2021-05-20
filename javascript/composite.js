const _ = require('lodash')

const users = [
	{id: 1, name: 'jhonfer', lastName: 'ruiz'}
]

const compose = (...fns) => x => fns.reduceRight((y, f) => f(y), x)

const head = x => x[0]
const capitalizeNameFull = x => ({
	name: _.upperFirst(x.name),
	lastName: _.upperFirst(x.lastName),
})
const resultNameFull = x => `${x.name} ${x.lastName}`

//point free
const getNameFull = compose(resultNameFull, capitalizeNameFull, head)

const x = getNameFull(users)
console.log(x)
