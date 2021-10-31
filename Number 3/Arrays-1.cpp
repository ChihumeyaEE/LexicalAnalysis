#include <iostream>
using namespace std;

const int ARRAY_SIZE = 50000;

void arrayStatic();
void arrayStackDyanmic();
void arrayHeapDyanmic();

int main() {
 clock_t st = clock(); 
 arrayStatic();
 st = clock() - st;
 cout << " Static Array -> " << (float)st/CLOCKS_PER_SEC << " seconds" << endl;
 
 clock_t st1 = clock(); 
 arrayStackDyanmic();
 st1 = clock() - st1;
cout << " Stack Dynamic Array -> " << (float)st1/CLOCKS_PER_SEC << " seconds" << endl;

 clock_t st2 = clock(); 
 arrayHeapDyanmic();
 cout << " Heap Dynamic Array -> " << (float)st2/CLOCKS_PER_SEC << " seconds" << endl;

}

void arrayStatic(){
  static int arr[ARRAY_SIZE];
  //init array
}

void arrayStackDyanmic(){
  int arr[ARRAY_SIZE];
   //init array
}

void arrayHeapDyanmic(){
  int* arr = new int[ARRAY_SIZE];
   //init array
}