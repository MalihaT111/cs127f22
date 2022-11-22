//Name:  Maliha Tasnim
//Email: MALIHA.TASNIM64@myhunter.cuny.edu
//Date:  November 16, 2022
//Enter two integers as bound, print all even ints in [start, end]

#include <iostream>
using namespace std;

int main() {
    cout << "Enter start: " ;
    int srange ;
    cin >> srange ;
    cout << "Enter end: " ;
    int erange ;
    cin >> erange ;
    for (int i=srange; i < erange + 1; i++) {
        if (i%2 == 0){
            cout << i << endl ;
        }
    }
    

}

