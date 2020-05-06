#!/usr/bin/node
// print multilenguages

let argv = process.argv.slice(2);

if (argv[0] == null){
  console.log('No argument');
} else if (argv[1] == null) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
