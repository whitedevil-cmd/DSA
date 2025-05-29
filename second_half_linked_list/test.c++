
#include <iostream>
#include <vector>
#include <algorithm>
// #include <bits/std++.h>

using namespace std;

int main() {
   vector<int> nums={1,2,3,4,5,-3,-6,-6,-1,4,3};
    int sum=0;
        sort(nums.begin(),nums.end());
        auto it=unique(nums.begin(),nums.end());
        nums.erase(it,nums.end());
        for(int num :nums){
            if(num>0) sum=sum+num;
            cout<<num<<",";
        }
        cout<<sum;
    return 0;
}