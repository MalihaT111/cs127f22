//Name:  Maliha Tasnim
//Email: MALIHA.TASNIM64@myhunter.cuny.edu
//Date:  November 21, 2022
/*Write a C++ program that asks the user for a whole number between -128 and 127 and prints out the number in "two's complement" notation.
*/
#include <iostream>
using namespace std;

int main() {
    string result ;
    result = " " ;
    int rem ;
    cout << "Enter an int in [-128, 127]: " ;
    int n ;
    cin >> n ;
    int num = n ;
    if(num < 0){
        num = -num-1;
    }
    
    int size = 8 ;
    int len = result.length() ;
    for (int i = 0; i < size - len; i++) {
        result = "0" + result;
    }
    
    for(int i = result.length()-1; i <result.length(); i--){
        rem = num % 2;
        result.replace(i,1,to_string(rem));
        num /= 2;
    }

    
    if (n < 0) {
        for (int i = 0; i < 8; i++) {
            if (result[i] == '0') {
                result[i] = '1' ;
            }
            else {
                result[i] = '0' ;
            }
        }
    }
    
    cout << "binary string: " ;
    cout << result ;


}

