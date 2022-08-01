#!/usr/bin/node

const input = process.argv;
const i = parseInt(input[2]);

if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
