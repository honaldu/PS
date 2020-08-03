const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const hour = Number(input[0]); // 숫자를 몇 시간으로 바꿔야 함
const min = Number(input[1]); // 숫자를 몇 분으로 바꿔야 함
const plusHour = hour - 1;
const plusMin = min - 45;
const minusMin = 60 + min - 45;

if (plusMin < 0) {
  if (hour < 1) {
    console.log(`23 ${minusMin}`);
  } else {
    console.log(`${plusHour} ${minusMin}`);
  }
} else {
  console.log(`${hour} ${plusMin}`);
}
