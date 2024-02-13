#!/usr/bin/node
/*
 * commandline n js is mde possible using the process.argv
 * which is an array that all arguments of the CLI.
 *
 * process.argv[0] contains the absolute path to the node bnary file
 *
 * process.argv[1] comntains the absolute file path to the .js file in which the engine runs.
 *
 * so the process.argv[2] .... contains user passed arguments.
 */

if (process.argv.length < 3) {
	console.log('No argument');

} else if (process.argv.length > 3) {
	console.log('Arguments found');
} else {
	console.log('Argument found');
}
