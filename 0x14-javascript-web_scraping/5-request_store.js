#!/usr/bin/node
// 5. Loripsum
const request = require('request');
const fs = require('fs');
const process = require('process');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, (err, response, body) => {
  if (err === null) {
    fs.writeFile(file, body, 'utf8', (fileError) => {
      if (fileError !== null) {
        console.log(fileError);
      }
    });
  } else {
    console.log(err);
  }
});
