#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.


const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (response) {
    const movie = JSON.parse(body);
    console.log(`${movie.title}`);
  } else {
    console.log(error);
  }
});
