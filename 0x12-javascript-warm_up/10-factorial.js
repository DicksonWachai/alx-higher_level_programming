#!/usr/bin/node
if (process.argv.length > 2) {
  const x = parseInt(process.argv[2]);
  function factorial (n) {
    if (n === 0 || n === 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }
  const result = factorial(x);
  console.log(result);
} else {
  console.log(1);
}
