#!/usr/bin/node
// 1. Write me
const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

fs.writeFile(file, content, { flag: 'a+' }, err => {
  if (err) {
    console.error(err);
  }
});
