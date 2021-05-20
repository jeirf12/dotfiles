const dollars = ["32$", "15$", "12$", "17$", "20$"];

//Las funciones con => se llaman arrows
// Map
// format boomer
let prices = [];
for (let i=0; i < dollars.length; i++){
	prices[i] = Number(dollars[i].slice(0, dollars[i].length-1));
}

//format zoomer
prices = [];
for(const dollar of dollars){
	prices.push(Number(dollar.slice(0, dollar.length-1)));
}

//format 2021
prices = dollars.map((dollar) => Number(dollar.slice(0, dollar.length-1)));

// Filter
let expensive = [];
for(const price of prices){
	if(price>=20){
		expensive.push(price);
	}
}

expensive = prices.filter((price) => price>=20);

// Reduce
let sum = 0;
for(price of expensive){
	sum += price;
}

sum = expensive.reduce((acum, price) => acum + price);

//Todo lo anterior de una
sum = dollars
	.map(dollar => Number(dollar.slice(0, dollar.length-1)))
	.filter(price => price>=20)
	.reduce((acum, price) => acum + price);

prices.map(price => ({price, currency: '$'})).forEach(obj => obj.price += 10);

