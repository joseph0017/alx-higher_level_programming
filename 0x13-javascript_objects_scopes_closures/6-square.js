#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    this.print(c);
  }
}

module.exports = Square;
