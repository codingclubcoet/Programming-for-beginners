#include <stdio.h>
#include <stdlib.h>

int main()

{
int i, n;
printf(“random numbers between 1 and 100000\n”);

for (i = 1; i <= 5; i++)
{
n = rand()%100000 + 1;

printf(“%d\n”, n);

}
return 0;
}
