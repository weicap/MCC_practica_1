// Insertion sort in Go

package main

import (
	"fmt"
)

func insertionsort(items []int) {
	var n = len(items)
	for i := 1; i < n; i++ {
		j := i
		for j > 0 {
			if items[j-1] > items[j] {
				items[j-1], items[j] = items[j], items[j-1]
			}
			j = j - 1
		}
	}
}

func main() {
	//Tamaño de la lista ejemplo = 12
	slice0 := []int{44057, 518, 60141, 88312, 11531, 79944, 16161, 54577, 71326, 21757, 39317, 5336}
	//Tamaño de lista a PROCESAR
	var siz = 10
	var slice = slice0[:siz]
	fmt.Println("\n--- Unsorted --- \n\n", slice)
	insertionsort(slice)
	fmt.Println("\n--- Sorted ---\n\n", slice, "\n")
}
