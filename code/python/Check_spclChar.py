// C++ program to check if a string 
// contains any special character 

// import required packages 
#include <iostream> 
#include <regex> 
using namespace std; 

// Function checks if the string 
// contains any special character 
void run(string str) 
{ 
	
	// Make own character set 
	regex regx("[@_!#$%^&*()<>?/|}{~:]"); 

	// Pass the string in regex_search 
	// method 
	if(regex_search(str, regx) == 0) 
		cout << "String is accepted"; 
	else
		cout << "String is not accepted."; 
} 

// Driver Code 
int main() 
{ 
	
	// Enter the string 
	string str = "Geeks$For$Geeks"; 
	
	// Calling run function 
	run(str); 

	return 0; 
} 

// This code is contributed by Yash_R 
