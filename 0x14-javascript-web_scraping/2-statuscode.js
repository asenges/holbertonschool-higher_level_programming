#!/usr/bin/node
// 2. Status code
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response) {
  if (error == null) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(error);
  }
});
