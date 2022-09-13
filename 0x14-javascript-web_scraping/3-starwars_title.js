#!/usr/bin/node
// 3. Star wars movie title
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request.get(url + id, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(err);
  }
});
