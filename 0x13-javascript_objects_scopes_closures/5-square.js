#!/usr/bin/node
// import the 4-recatngle
const Rectangle = require('./4-rectangle');

// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
