#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('ERROR:', error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrl = movieData.characters;
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