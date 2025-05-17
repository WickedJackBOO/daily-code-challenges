// Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

// The binary number returned should be a string.

// Examples:(Input1, Input2 --> Output (explanation)))

// 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
// 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

function addBinary(a, b) {
    let sum = a + b
    let binary = ""
    let power = 1

    while (power <= sum) {
        power *= 2
    }
    // console.log(power)
    power /=2

    while (power >= 1) {
        if (sum >= power) {
            binary += "1"
            sum -= power
        } else {
            binary += "0"
        }
        power /= 2
        // console.log(power+" "+binary)
    }
    return binary
    
    
    
    // the internet 
    binary = sum.toString(2);
    console.log("binary: "+binary);
    return binary
}


console.log(addBinary(5, 9));