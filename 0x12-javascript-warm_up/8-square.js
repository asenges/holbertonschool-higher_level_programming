#!/usr/bin/node

const input = process.argv;
const i = parseInt(input[2]);

if (isNaN(i)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < i; j++) {
    console.log('X'.repeat(i));
  }
}
