const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let i = 0;
const num = input[i].split(" ");
const result = "";

while (num[0] + num[1] === 0) {
  result += `${num[0] + num[1]}\n`;
  i++;
}
console.log(result);
