#!/usr/bin/node
const rectangle = require('./4-rectangle');
module.exports = class Square extends rectangle {

  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
}
