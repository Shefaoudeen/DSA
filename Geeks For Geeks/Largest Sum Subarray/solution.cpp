#include <iostream>
using namespace std;

long long int maxSumWithK(long long int a[], long long int n, long long int k) 
    {
      long long int maxTerm = -9999;
      for(int i=0;i<n;i++){
        for(int j=i+k-1;j<n;i++){
          long long int Total = 0;
            for(int x=i;i<=j;i++){
              Total += a[x];
            }
            if(Total > maxTerm){
              maxTerm = Total;
            }
        }
      }
      return maxTerm;
    }

int main(){
  long long int n;
  cin >> n;
  long long int a[n];
  for (int i=0;i<n;i++){
    cin>>a[i];
  }
  long long int k;
  cin>>k;
  cout << maxSumWithK(a,n,k);
}