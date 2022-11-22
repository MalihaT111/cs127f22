//Name:  Maliha Tasnim
//Email: MALIHA.TASNIM64@myhunter.cuny.edu
//Date:  November 16, 2022
//academic standing

#include <iostream>
using namespace std;

int main() {
    cout << "Enter number of credit hours taken: " ;
    int credithours ;
    cin >> credithours ;
    if (credithours < 28) {
        cout << "freshman" ;
    }
    else if (credithours >= 28 && credithours < 61) {
        cout << "sophmore" ;
    }
    else if (credithours >= 61 && credithours < 94) {
        cout << "junior" ;
    }
    else if (credithours >= 94){
        cout << "senior" ;
    }
}


