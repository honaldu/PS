const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const year = Number(input[0]);
const four = year % 4;
const hundred = year % 100;
const fourHundred = year % 400;

if (fourHundred === 0) {
  console.log(1);
} else if (four === 0 && hundred !== 0) {
  console.log(1);
} else {
  console.log(0);
}
