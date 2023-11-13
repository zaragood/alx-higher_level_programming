#!/usr/bin/node

// script that prints the addition of 2 integers

function add(a, b) {
  return a + b;
}

const [, , ...args] = process.argv;
let sum = 0;

if (args.length < 2) {
  console.log('NaN');
} else {
  for (let i = 0; i < args.length; i++) {
    if (typeof args[i] === 'string' && !isNaN(args[i])) {
      let num = Number(args[i]);
      sum = add(sum, num); 
    }
  }
  console.log(sum);
}

