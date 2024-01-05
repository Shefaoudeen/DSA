#include <iostream>
using namespace std;

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    int Cookies = 0;
    int feed = 0;
    int index = 0;
    int isCookieNotZero = 0;
    int isFeedNotFull = 0;

    for(int i=0;i<sSize;i++){
      Cookies+=s[i];
    }

    while((isCookieNotZero==0) && (isFeedNotFull==0)){
      if(g[index]>0){
        g[index]--;
        Cookies--;
        if(g[index] == 0){
          feed++;
        }
      }
      if((index+1) != gSize){
        index++;
      }
      if(feed == gSize){
        return feed;
        isFeedNotFull++;
      }
      if(Cookies == 0){
        return feed;
        isCookieNotZero++;
      }
    }
    return feed;
}

int main(){
  int gSize;
  cin >> gSize;
  int g[gSize];
  for(int i=0;i<gSize;i++){
    cin>>g[i];
  }
  int sSize;
  cin >> sSize;
  int s[sSize];
  for(int i=0;i<sSize;i++){
    cin>>s[i];
  }
  cout << findContentChildren(g, gSize,s,sSize);
  return 0;
}