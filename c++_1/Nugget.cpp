#include <iostream>
#include <string>
using namespace std;

//This is the function I'm using with a conditional function inside it
void checking( int nuggets ) {
    if (nuggets == 8) {
            cout << "You have the correct amount of nuggets!!";
        } 
    else {
            cout << "You don't have the correct amount of nuggets. Your public sacrifice will be in 2 weeks.";
        }  
}

int main () {
    // This is a function in the code.
    cout << "you are given a specific amount of nuggets. You look inside to see how many you have...";
 // integer for number of nuggets
    int nuggets = 8;
    string employee = "Jonah";

if (employee == "Jonah") {
    // What happens when the boolaean expression (question) is true
    // Write your code below
    cout << "Yes";


} else {
    // What happens when the boolaean expression (question) is false
    // Write your code below
        cout << "No";
        checking(8); //calling the function in main    

}