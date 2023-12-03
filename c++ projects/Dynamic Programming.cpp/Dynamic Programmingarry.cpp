#include <iostream>
using namespace std;

// Returns maximum sum in a subarray of size n

int max_Sum(int arr[], int m, int n)
{
    // n must be smaller than m
    if (m < n)
    {
       cout << "Invalid";
       return -1;
    }
 
    // Compute sum of first window of size n
    int res = 0;
    for (int i=0; i<n; i++)
       res += arr[i];
 
    
    int curr_sum = res;
    for (int i=n; i<m; i++)
    {
       curr_sum += arr[i] - arr[i-m];
       res = max(res, curr_sum);
    }
 
    return res;
}
  
int main()
{
    int arr[] = {2, 12, 7, 32, 15, 10, 8};
    int n = 3;
    int m = sizeof(arr)/sizeof(arr[0]);
    cout << max_Sum(arr, m, n);
    return 0;
}