#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/`;

function logchars (array, i){
  if (i == array.length) {
    return;
  }

  request.get(array[i], function (err, response1, body1) {
    if (!err) {
      console.log(JSON.parse(body1).name);
      logchars(array, i + 1);
    }
  });
}

request.get(url + movieId, function (error, response, body) {
  if (!error) {
    const cha = JSON.parse(body).characters;
    logchars(cha, 0);
  }
});
  