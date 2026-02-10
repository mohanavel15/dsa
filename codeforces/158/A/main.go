package main

import "fmt"

func main() {
	var n, k int

	fmt.Scanln(&n, &k)

	scores := []int{}

	var s int

	for _ = range n {
		fmt.Scan(&s)
		scores = append(scores, s)
	}

	t := scores[k-1]
	sd := 0

	for i := range n {
		if scores[i] <= 0 || scores[i] < t {
			break
		}

		sd += 1
	}

	fmt.Println(sd)
}
