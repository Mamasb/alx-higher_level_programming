#!/usr/bin/node
/*
 This script prints two arguments passed to it still using the 
 concept of procedd.argv

 const firstArg = process.argv[2],  secondArg = process.argv[3];
 if (firstArgv === undefined || secondArg === undefined) {
 console.log(first + ' is secondArg);
 } else {
 console.log(firstArg + 'is ' +secondArg);
 }
 */

console.log(process.argv[2]+ ' is ' + process.argv[3]);
