#!/usr/bin/node
// 4. Star wars Wedge Antilles
const request = require('request');
const url = process.argv[2];
const search = 18;

request.get(url, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    let movies = data.results;
    movies = movies.filter(
      movie => movie.characters.find(
        character => character.match(search)
      )
    );
    console.log(movies.length);
  } else {
    console.log(err);
  }
});
