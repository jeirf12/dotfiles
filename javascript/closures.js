// const x = 'cuquini'

// const f = () =>{
// 	console.log(x)
// }

// f()

require('isomorphic-fetch')

const crudder = domain => recurso =>{
	const url = `${domain}/${recurso}`

	return ({
		create: (x) => fetch(url, {
			method: 'POST',
			body: JSON.stringify(x),
		}).then(x => x.json()),
		get: () => fetch(url).then(x => x.json())
	})
}

const base = crudder('https://jsonplaceholder.typicode.com')

const todos = base('todos')
const users = base('users')

todos.get().then(x => console.log(x[0]))
users.get().then(x => console.log(x[0]))
