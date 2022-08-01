#!/usr/bin/node

const input = process.argv;
const orderArray = [];
let checkVal;

function searchSecBig () {
  const j = orderArray.length;
  orderArray.sort(function (a, b) {
    return a - b;
  });
  console.log(orderArray[j - 2]);
}
if (input.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < input.length; i++) {
    checkVal = parseInt(input[i]);
    if (isNaN(checkVal)) {
      continue;
    } else {
      orderArray.push(checkVal);
    }
  }
  searchSecBig();
}
