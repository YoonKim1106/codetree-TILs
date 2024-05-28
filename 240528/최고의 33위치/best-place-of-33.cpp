#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> grid(n, vector<int>(n));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> grid[i][j];
        }
    }
    
    int max_coins = 0;
    
    for (int i = 0; i <= n - 3; ++i) {
        for (int j = 0; j <= n - 3; ++j) {
            int current_coins = 0;
            for (int x = i; x < i + 3; ++x) {
                for (int y = j; y < j + 3; ++y) {
                    current_coins += grid[x][y];
                }
            }
            max_coins = max(max_coins, current_coins);
        }
    }
    
    cout << max_coins << endl;
    
    return 0;
}