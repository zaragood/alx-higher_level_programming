#!/usr/bin/node

// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

const [, , x] = process.argv;
let i = 0;

if (typeof x === 'string' && !isNaN(x)) {
  const number = Number(x);
  while (number > i) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
