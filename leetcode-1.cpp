#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <queue>
#include <unordered_set>

using namespace std;



int main()
{
    int n = 3;
    int A[3] = {3, 1, 10}, B[3] = {3,1, 10}, C[3] = {3, 1, 10};

    vector<int> dp(1001, 0);
    for (int i = 0; i < n; i++)
    {
        int v, t, d;
        v = A[i], t = B[i], d = C[i];
        dp[t] = max(dp[t], v);
        for (int j = t + 1; j <= d; j++)
        {
            dp[j] = max(dp[j], dp[j - t] + v);
        }
    }

    int maxV = 0;
    for (int i = 0; i < 1001; i++)
    {
        maxV = max(maxV, dp[i]);
    }

    cout << maxV;
}