#!/usr/bin/node
// this script return the status of a request

const request = require('request');

request(process.argv[2], (err, res) => {
  if (err) return err;
  console.log('code: ' + res.statusCode);
});
