#!/usr/bin/node
// function that increments and calls a function.

const addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};

module.exports.addMeMaybe = addMeMaybe;
