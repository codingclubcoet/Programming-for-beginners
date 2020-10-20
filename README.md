# Programming for beginners

This repo intends to make materials and codes that will be count for the beginner programming enthusiasts to learn programing languages.

## Contribution guidelines

- [x] Don't spam
- [x] For what to do in this repo, refer <a href="https://github.com/codingclubcoet/Python-for-beginners/projects/1">here</a>

/*PROGRAM TO SWAP TWO VARIABLES USING FUNCTIONS HAVING SAME NAME BUT WITH DIFFERENT PARAMETERS*/
#include<conio.h>

#include<iostream.h>

class swap

{

int a,b;

float m,n,temp;

public:

void input();

void display(int,int);

void display(float,float);

};

void swap::input()

{

cout<<“Enter any two integers: “;

cin>>a>>b;

cout<<“Before swapping integer values are: a= “<<a<<” b= “<<b<<endl;

display(a,b);

cout<<“Enter any two float values: “;

cin>>m>>n;

cout<<“Before swapping float values are: m= “<<m<<” n= “<<n<<endl;

display(m,n);

}

void swap::display(int a,int b)

{

a=a+b;

b=a-b;

a=a-b;

cout<<“After swapping integer values are: a= “<<a<<” b= “<<b<<endl;

}

void swap::display(float m,float n)

{

temp=m;

m=n;

n=temp;

cout<<“After swapping float values are:  m= “<<m<<” n= “<<n;

}

 

void main()

{

swap s1;

clrscr();

s1.input();

getch();

}

