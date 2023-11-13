#!/usr/bin/node

// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

const [, , myNumber] = process.argv;

if (typeof myNumber === 'string' && !isNaN(myNumber)) {
  const number = Number(myNumber);
  console.log('My number: ' + number);
} else {
  console.log('Not a Number');
}
