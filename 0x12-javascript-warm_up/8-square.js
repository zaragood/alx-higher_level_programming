#!/usr/bin/node

//  script that prints a square

const [, , x] = process.argv;
let i = 0;
let j = 0;

if (typeof x === 'string' && !isNaN(x)) {
  const number = Number(x);
  while (number > i) {
    let row = '';
    j = 0;
    while (number > j) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
