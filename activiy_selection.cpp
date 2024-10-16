#include <iostream>
#include <vector>

using namespace std;

// {1, 8, 3, 2, 6}, E[] = {5, 10, 6, 5, 9}
bool cmp(const vector<int> &a, const vector<int> &b)
{
    return a[1] <= b[1];
}

int main()
{

    int rows, cols;
    cout << "Enter the number of rows and columns for the 2D array: ";
    cin >> rows >> cols;

    vector<vector<int>> v(rows, vector<int>(cols));
    vector<int>::iterator iter;

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {
            cout << "Enter array element in " << i << " " << j << " position.\n";
            cin >> v[i][j];
        }
    }
    sort(v.begin(), v.end(), cmp);

    cout << "Printing the data\n";

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < v[i].size(); j++)
        {

            cout << v[i][j] << " ";
        }
        cout << endl;
    }

    int var = 0;
    int count = 0;
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i][0] >= var)
        {
            count++;
            var = v[i][1];
        }
    }
    cout << count << endl;
}