#!/usr/bin/node

// class Rectangle that defines a rectangle:

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
  // instance method called print() that prints the rectangle using the character X

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Create an instance method called rotate() that exchanges the width and the height of the rectangl

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  // Create an instance method called double() that multiples the width and the height of the rectangle by 2

  double () {
    [this.height, this.width] = [this.height * 2, this.width * 2];
  }
}

module.exports = Rectangle;
