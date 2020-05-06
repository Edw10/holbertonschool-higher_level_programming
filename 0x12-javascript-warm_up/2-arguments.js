#!/usr/bin/node
// print multilenguages

let argv = process.argv;

if (argv[2] === undefined){
  console.log('No argument');
} else if (argv[3] === undefined) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
