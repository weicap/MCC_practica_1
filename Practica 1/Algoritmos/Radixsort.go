package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
)

const digit = 4
const maxbit = -1 << 31

func radixsort(data []int32) {
	buf := bytes.NewBuffer(nil)
	ds := make([][]byte, len(data))
	for i, e := range data {
		binary.Write(buf, binary.LittleEndian, e^maxbit)
		b := make([]byte, digit)
		buf.Read(b)
		ds[i] = b
	}
	countingSort := make([][][]byte, 256)
	for i := 0; i < digit; i++ {
		for _, b := range ds {
			countingSort[b[i]] = append(countingSort[b[i]], b)
		}
		j := 0
		for k, bs := range countingSort {
			copy(ds[j:], bs)
			j += len(bs)
			countingSort[k] = bs[:0]
		}
	}
	var w int32
	for i, b := range ds {
		buf.Write(b)
		binary.Read(buf, binary.LittleEndian, &w)
		data[i] = w ^ maxbit
	}
}

func main() {

	var data = []int32{44057, 518, 60141, 88312, 11531, 79944, 16161, 54577, 71326, 21757, 39317, 5336}
	var siz = 10
	var data2 = data[:siz]
	fmt.Println("\n--- Unsorted --- \n\n", data2)
	radixsort(data2)
	fmt.Println("\n--- Sorted ---\n\n", data2)
}
