package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	palindromes := []int{}
	for a := 1; a <= 999; a++ {
		for b := 1; b <= 999; b++ {
			product = a*b
			if palindromeCheck(product) {
				palindromes = append(palindromes, product)
			}
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(palindromes)))
	fmt.Println(palindromes[0])
}

func palindromeCheck(product) {
	product = strconv.Itoa(product)
	productReversed = // TODO: reverse(product)
	if product == productReversed {
		return true
	} else {
		return false
	}
}
