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

  rotate () {
    const j = this.width;
    this.width = this.height;
    this.height = j;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
