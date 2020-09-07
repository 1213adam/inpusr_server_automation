#include<stdio.h>
#include<malloc.h>

//no parameter , no return type 
void  hello()
{
	printf("Hello,NEU!\n");
}

//with parameter£¬with return type
 
int  add(int a, int b)
{
	return a + b;
}

//with parameter
//need modify parameter value£¬use  Pointer
int  inc(int *a)
{
	return (*a)++;
}

//with parameter
//pass Arrary£¬use  Pointer
void  printArr(int *a, int n)
{
	int i;
	for (i = 0; i < n; i++)
	{
		printf("%d ", *a++);
	}
}

//return type is ArraryList
// pass ArraryList , using Pointer 
int*  getArr()
{
	int *p, *q;
	q = p = (int*)malloc(sizeof(int) * 4);
	int i;
	for (i = 0; i < 4; i++)
	{
		*p++ = i;
	}
	return q;
}

//call other sub functions
void heiheihei()
{
	printf("Hello,NEU!!!!");
}

void  callFunc()
{
	heiheihei();
}



