//Name:  Maliha Tasnim
//Email: MALIHA.TASNIM64@myhunter.cuny.edu
//Date:  November 16, 2022
//triangle

#include <iostream>
using namespace std;

int main() {
    cout << "Enter an int: " ;
    int number ;
    cin >> number ;
    cout << "Enter a symbol other than space: " ;
    string symbol;
    cin >> symbol ;
    string s = " " ;
    for(int i = 0; i < number ; i++) {
//        for(int i = 0; i < number - 1 ; i++) {
//            s+= " " ;
//        }
//        //s+= " " ;
        s+= symbol ;
        cout << s << endl ;
    }

}



