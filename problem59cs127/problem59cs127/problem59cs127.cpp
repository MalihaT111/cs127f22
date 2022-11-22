//Name:  Maliha Tasnim
//Email: MALIHA.TASNIM64@myhunter.cuny.edu
//Date:  November 21, 2022
/*Suppose due to inflation, monthly expense in July to December is 15% than that in January to June.

Print out month, monthly expense, and remaining balance in the budget in the end of a month. The remaining balance can be negative, meaning a user under-estimates the expenses. If the remaining balance after a year is negative, print "need higher budget".
*/
#include <iostream>
using namespace std;

int main() {
    cout << "Input your annual budget: " ;
    double budget ;
    cin >> budget ;
    cout << "Input your month expense: " ;
    double expense;
    cin >> expense ;
    double inflation = expense * 1.15;
    for (int i = 1; i < 13; i++) {
        if (i > 6){
            budget = budget - inflation ;
            printf("%5d\t%7.2f\t%27.2f\n", i, inflation, budget);
        }
        else {
            budget = budget - expense ;
            printf("%5d\t%7.2f\t%27.2f\n", i, expense, budget);
        }
        
    }
    if (budget < 0){
        cout << "need higher budget" ;
    }

}

