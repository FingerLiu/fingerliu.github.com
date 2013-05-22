#include<iostream>
using namespace std;
int main()
{
	int i=2;
	int n=0;
	float f=0;
	float sum=0;
	while(cin>>f)
	{
		if(f==0.00)break;
		while(f>sum)
		{sum+=(float)1/i;i++;}
		cout<<i-2<<"card(s)"<<endl;
	}
	system("pause");
	return 0;
}