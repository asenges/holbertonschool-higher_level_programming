#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w || h) <= 0 || (w || h) === undefined) { return; }
    this.width = w;
    this.height = h;
  }

  print (chr) {
    this.chr = chr;
    if (chr === undefined) {
      chr = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
