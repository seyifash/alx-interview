#!/usr/bin/node

const request = require('request');

function sendRequest (movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const film = JSON.parse(body);
      const charactersUrls = film.characters;

      charactersUrls.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

const movieId = process.argv[2];
sendRequest(movieId);
