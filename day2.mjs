import { readFile } from "node:fs/promises";
const INPUT = await readFile("inputs/day2.txt", "utf-8");

function partone() {
  const ranges = INPUT.split(",");
  let invalidIDsum = 0;
  for (const rangeStr of ranges) {
    const twonums = rangeStr.split("-").map(Number);
    for (let numberInt = twonums[0]; numberInt <= twonums[1]; numberInt++) {
      const numberStr = String(numberInt);
      const l = Math.floor(numberStr.length / 2);
      const num1 = numberStr.slice(0, l);
      const num2 = numberStr.slice(l);
      if (num1 == num2) invalidIDsum += numberInt;
    }
  }
  console.log(invalidIDsum);
}

partone();
