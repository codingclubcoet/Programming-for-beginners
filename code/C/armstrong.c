/*
Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers
*/

#include<stdio.h>
#include "armstrong.h"

int main()
{
	int n;
	printf("Enter a number: ");
	scanf("%d",&n);
	armstrong(n);
	return 0;
}