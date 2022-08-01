#!/usr/bin/node

const input = process.argv;

if (input.length < 3) {
  console.log('No argument');
} else {
  console.log(input[2]);
}
