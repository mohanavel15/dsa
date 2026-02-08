package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	fmt.Print("I hate ")

	for idx := range n - 1 {
		if idx%2 == 0 {
			fmt.Print("that I love ")
		} else {
			fmt.Print("that I hate ")
		}
	}

	fmt.Println("it")
}
