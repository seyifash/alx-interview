#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('ERROR:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log('Error fetching data:', response.statusCode);
  }

  const movieData = JSON.parse(body);
  const charactersUrl = movieData.characters;

  charactersUrl.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data, status code:', response.statusCode);
        process.exit(1);
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
