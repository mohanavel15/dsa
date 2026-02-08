package main

import "fmt"

func main() {
	var n int = 0
	var x int = 0
	var op string

	fmt.Scanln(&n)

	for _ = range n {
		fmt.Scanln(&op)

		if op == "++X" || op == "X++" {
			x += 1
		} else if op == "--X" || op == "X--" {
			x -= 1
		} else {
			panic("Invalid Input")
		}
	}

	fmt.Println(x)
}
