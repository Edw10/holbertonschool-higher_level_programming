#!/usr/bin/node
// this script store the request
const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, res, bd) => {
  if (err) return err;
  fs.writeFile(process.argv[3], bd, 'utf8');
  console.log(JSON.parse(bd).title);
});
