package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	will_solve := 0

	var p1, p2, p3 int

	for _ = range n {
		fmt.Scanln(&p1, &p2, &p3)

		if p1+p2+p3 >= 2 {
			will_solve += 1
		}
	}

	fmt.Println(will_solve)
}
