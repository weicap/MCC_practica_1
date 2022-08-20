#include <iostream>
#include <vector>
using namespace std;

void swap(int &a,int &b){
    int aux = a;
    a = b;
    b = aux;
}

int particion(vector<int>&array,int inicio, int fin){
    int pivote = array[inicio];
    int i = inicio + 1;
    for(int j = i; j <= fin; j++){
        if(array[j] < pivote){
            swap(array[i],array[j]);
            i++;
        }
    }
    swap(array[inicio],array[i-1]);
    return i-1;
}

void quickSort(vector<int>&array, int inicio, int fin){
    if(inicio < fin){
        int pivote = particion(array,inicio,fin);
        quickSort(array,inicio,pivote-1);
        quickSort(array,pivote+1,fin);
    }
}

void imprimirArreglo(vector<int>array){  
    for(int i = 0; i < array.size(); i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

int main(){
    int numsArr[] = {44057, 518, 60141, 88312, 11531, 79944, 16161, 54577, 71326, 21757, 39317, 5336};
    int len = 10;
    vector<int> nums;
    for (int i=0; i < len; i++) {
      nums.push_back(numsArr[i]);
    }
    quickSort(nums,0,len-1);
    imprimirArreglo(nums);
}