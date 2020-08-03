const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const number = Number(input[0]); // 숫자를 몇 시간으로 바꿔야 함

for (let i = 1; i < 10; i++) {
  console.log(`${number} * ${i} = ${number * i}`);
}
