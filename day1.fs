let readLines filePath = System.IO.File.ReadLines filePath

let lines = readLines "inputs/day1.txt"
let mutable dial = 50
let mutable zeros = 0

for line in lines do
    let dir = line[0]
    let amnt = int line[1..]
    let amnt = if dir = 'L' then -amnt else amnt
    dial <- dial + amnt
    if dial % 100 = 0 then
        zeros <- zeros + 1

printfn "%d" zeros
