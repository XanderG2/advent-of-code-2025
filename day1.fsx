let readLines filePath = System.IO.File.ReadLines filePath

let lines = readLines "day1.txt"
let partone =
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

let parttwo =
    let mutable dial = 50
    let mutable zeros = 0

    for line in lines do
        let dir = line[0]
        let amnt = int line[1..]
        let i = if dir = 'L' then -1 else 1
        for x in [1..amnt] do
            dial <- dial + i
            if dial % 100 = 0 then
                zeros <- zeros + 1

    printfn "%d" zeros

partone
parttwo