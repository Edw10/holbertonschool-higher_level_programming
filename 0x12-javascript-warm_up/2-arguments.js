#!/usr/bin/node
// print multilenguages

const argv = process.argv;

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
