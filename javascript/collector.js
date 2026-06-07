// pattern collector local without framework or package for javascript

if(!Array.prototype.collect) {
	Array.prototype.collect = function(partial) {
		const valuesFn = Object.values(partial);
		if (valuesFn.length !== 2) 
			return []

		return this.flatMap(_ => valuesFn[0](_) 
			? [valuesFn[1](_)] 
			: []
		)
	}
}

const partialFunction = {
	isDefinedAt: (a) => a % 2 == 0,
	apply: (b) => b * b,
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8];

var fooParcial = numbers.collect(partialFunction)

console.log(fooParcial)
