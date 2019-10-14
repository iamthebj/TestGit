#include <iostream>
using namespace std;

int main ()
{
    int n = 1,times=5;                    /* local variable Initialization */  

    for( n = 1; n <= times; n = n - 1 )     /* for loops execution */ 
    {
         cout << "C++ for loops: " << n <<endl;
    }
   return 0;
}
