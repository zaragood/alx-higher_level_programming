#!/usr/bin/node

// class Rectangle that defines a rectangle:

class Rectangle {
  constructor (w, h) {
  if (w === undefined || h === undefined || w <= 0 || h <= 0) {
    this.width;
    this.height;
  } else {
    this.width = w;
    this.height = h;
  }
  }
}

module.exports = Rectangle;
