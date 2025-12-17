import { readFile } from "node:fs/promises";
const inp = await readFile("inputs/day1.txt", "utf-8");
const INPUT = inp.split("\r\n");

function partone() {
  let zeros = 0;
  let currentNum = 50;
  for (const instruction of INPUT) {
    const direction = instruction[0];
    let amount = parseInt(instruction.slice(1), 10);
    if (direction == "L") amount = -amount;
    currentNum += amount;
    if (currentNum % 100 == 0) zeros++;
  }
  console.log(zeros);
}

function parttwo() {
  let zeros = 0;
  let currentNum = 50;
  for (const instruction of INPUT) {
    const direction = instruction[0];
    let amount = parseInt(instruction.slice(1), 10);
    let increase = 1;
    if (direction == "L") increase = -increase;
    for (let i = 0; i < amount; i++) {
      currentNum += increase;
      if (currentNum % 100 == 0) zeros++;
    }
  }
  console.log(zeros);
}

partone();
parttwo();
