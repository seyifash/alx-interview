#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log('ERROR:', error);
  } else {
    const charactersUrl = JSON.parse(body).characters;
    if (charactersUrl.length === 0) {
      return;
    }

    charactersUrl.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('error:', error);
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  }
});
