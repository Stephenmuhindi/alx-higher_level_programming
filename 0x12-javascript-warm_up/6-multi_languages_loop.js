#!/usr/bin/node
/*
 prints 3 lines: (like 1-multi_languages.js)
but by using an array of string and a loop
*/
const args = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const arg in args) {
  console.log(args[arg]);
}
