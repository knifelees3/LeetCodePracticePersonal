#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <queue>
#include <unordered_set>

using namespace std;

int main()
{
    int n, roomA, roomB;
    unordered_map<int, vector<int> > graph;

    cin >> roomA >> roomB;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;

        if (graph.find(a) == graph.end())
        {
            graph[a] = vector<int>();
        }
        if (graph.find(b) == graph.end())
        {
            graph[b] = vector<int>();
        }

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    queue<int> v;
    v.push(roomA);
    int doors = 0;

    unordered_set<int> visited;
    visited.insert(roomA);

    while (!v.empty())
    {
        int m = v.size();
        doors++;
        int cur = v.front();
        for (int i = 0; i < m; i++)
        {          
            for (int j = 0; j < graph[cur].size(); j++)
            {
                int next = graph[cur][j];
                if (next == roomB)
                {
                    cout << doors;
                    return 0;
                }

                if (visited.find(next) == visited.end())
                {
                    visited.insert(next);
                    v.push(next);
                }
            }
            v.pop();
        }
    }

    cout << doors;
    return 0;
}