#include <stdio.h>
int main()
{
     int num1, num2;
     printf("Enter 2 integers");
     scanf("%d%d" , &num1 ,&num2);
     if (num1 > num2)
     {
        printf ("largest no. is %d", num1);
     }
     else 
     {
          printf("largest no. is %d", num2);
     }
       
       return 0;
       
      }
