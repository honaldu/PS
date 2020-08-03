const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let inputs = input[0].split(" ");

const total = Number(inputs[0]);
const limit = Number(inputs[1]);

let numbers = input[1].split(" ");

let result = "";

for (let i = 0; i < total; i++) {
  if (Number(numbers[i]) < limit) {
    result += numbers[i] + " ";
  }
}
console.log(result);
