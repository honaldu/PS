const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let number = Number(input[0]);
let sum = 0;

for (let i = 0; i <= number; i++) {
  sum += i;
}
console.log(sum);
