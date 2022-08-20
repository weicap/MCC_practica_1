// Insertion sort in C++

#include <iostream>
using namespace std;

// Function to print an array
void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    cout << array[i] << " ";
  }
  cout << endl;
}

void insertionSort(int array[], int size) {
  for (int step = 1; step < size; step++) {
    int key = array[step];
    int j = step - 1;

    // Compare key with each element on the left of it until an element smaller than
    // it is found.
    // For descending order, change key<array[j] to key>array[j].
    while (key < array[j] && j >= 0) {
      array[j + 1] = array[j];
      --j;
    }
    array[j + 1] = key;
  }
}

// Driver code
int main() {
  //Tamaño de la lista ejemplo 13
  int numsArr[] = {44057, 518, 60141, 88312, 11531, 79944, 16161, 54577, 71326, 21757, 99883, 6260, 37222}; 
  //Tamaño de lista a PROCESAR
  int len = 10; 
  int nums[len];
  for (int i=0; i < len; i++) {
    nums[i] = numsArr[i];
  }
  insertionSort(nums, len);
  cout << "Sorted array in ascending order:\n";
  printArray(nums, len);
}