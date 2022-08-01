#!/usr/bin/node

const input = process.argv;

if (input[2] === undefined) {
  console.log('No argument');
} else {
  console.log(input[2]);
}
