// const p1 = Promise.resolve(1)
// console.log(p1)

// p1.then(x => x + 6)
// 	.then(x => Promise.resolve(x+6))
// 	.then(x => Promise.reject('ERROR! algo sucedio'))
// 	.then(x => console.log('Esto no se llama'))
// 	.catch(e => console.log(e))

const delayed = x => new Promise((resolve, reject) => setTimeout(() => resolve(x), 900))

delayed(7)
	.then(x => {
		console.log(x)
		return delayed(x+7)
	})
	.then(x => console.log(x))
	.then(x => Promise.reject('ERROR'))
	.catch(e => console.log(e))
