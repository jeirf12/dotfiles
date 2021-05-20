require('isomorphic-fetch')

fetch('https://jsonplaceholder.typicode.com/users')
	.then(x => x.json())
	.then(x => console.log(x))
