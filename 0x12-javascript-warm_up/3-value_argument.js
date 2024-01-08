#!/usr/bin/node
/*
the first argument passed to it
is printed
*/
const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
