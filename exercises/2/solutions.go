package main

import (
	"fmt"
)

func main() {
	a := 1
	b := 2
	c := 0
 	sum := 0
	for b <= 4000000 {
		if b%2 == 0 {
			sum += b
		}
		c = a + b
		a = b
		b = c
	}
	fmt.Println(sum)
}
