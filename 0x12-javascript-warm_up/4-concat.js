#!/usr/bin/node

// script that prints two arguments passed to it, in the following format: “ is ”

const [, , ...args] = process.argv;

if (args.length === 2) {
  console.log(args[0] + ' is ' + args[1]);
} else if (args.length === 1) {
  console.log(args[0] + ' is ' + 'undefined');
} else {
  console.log('undefined ' + 'is ' + 'undefined');
}
