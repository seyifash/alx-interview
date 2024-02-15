#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/';

function sendRequest (array, i) {
  if (i === array.length) {
    return;
  }

  request(array[i], function (err, response1, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      sendRequest(array, i + 1);
    }
  });
}

request(url + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const url2 = JSON.parse(body).characters;
    sendRequest(url2, 0);
  }
});
