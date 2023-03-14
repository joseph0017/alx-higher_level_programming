#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (string = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(string.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
