#!/usr/bin/node

// script that prints the first argument passed to it:
const [, , firstArg] = process.argv;

if (!firstArg) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
