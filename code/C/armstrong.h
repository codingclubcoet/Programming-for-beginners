/*
Armstrong number is a number that is equal to the sum of cubes of its digits.
 For example 0, 1, 153, 370 etc.
*/

void armstrong(int n)
{
	int num,rmdr,res=0;
	num = n;
	while(num != 0)
	{
		rmdr = num % 10;
		res += rmdr*rmdr*rmdr;
		num /= 10;
	}
	if(res == n){

		printf("%d is an armstrong number\n", n);
	}
	else{
		printf("%d is not an armstrong number\n", n);
	}
}