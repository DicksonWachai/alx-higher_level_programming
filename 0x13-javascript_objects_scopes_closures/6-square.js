#!/usr/bin/node

const PreviousSquare = require('./5-square');

class Square extends PreviousSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      if (this.width && this.height) {
        for (let i = 0; i < this.height; i++) {
          console.log(`${c.repeat(this.width)}`);
        }
      }
    }
  }
}
module.exports = Square;
