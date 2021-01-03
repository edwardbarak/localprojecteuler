var arr = Array(1,2);
var sum = 0;

function fib(arr) {
    return Array(arr[1], arr[0] + arr[1])
}

while (arr[1] < 4000000) {
    if (arr[1] % 2 === 0) {
        sum += arr[1]
    }
    arr = fib(arr)
}

console.log(sum)