#!/usr/bin/node
// this script return the title of the starwars movie

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, res, bd) => {
  if (err) return err;
  console.log(JSON.parse(bd).title);
});
