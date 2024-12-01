// Implement Subset Sum Problem.
// Statement Given a set of non-negative integers and a
// value sum, the task is to check if there is a subset of the
// given set whose sum is equal to the given sum.
// Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
// Output: True
// Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
// Output: False

#include <iostream>
#include <vector>
using namespace std;

bool search(int a, int b)
{
    vector<int> store;
    int s1 = 0, s2 = 0;
    for (int i = 0; i < store.size(); i++)
    {
        if (store[i] == a)
            s1 = 1;

        else if (store[i] == b)
            s2 = 1;
    }

    if (s1 && s2 == 1)
        return true;

    else
    {
        store.push_back(a);
        store.push_back(b);
        return false;
    }
}

int main(void)
{
    vector<int> arr;
    int number, sum;
    string ans;
    string output = "false";

    do
    {
        cout << "\nEnter a number in array : ";
        cin >> number;
        arr.push_back(number);
        cout << endl;
        cout << "Enter more numbers (y/n): ";
        cin >> ans;
        cout << endl;

    } while (ans == "y");

    cout << "Enter a Sum : ";
    cin >> sum;

    for (int i = 0; i < arr.size(); i++)
    {
        for (int j = 0; j < arr.size(); j++)
        {
            if (arr[i] + arr[j] == sum)
            {
                int result = search(arr[i], arr[j]);
                if (result == true)
                    break;
                else
                {
                    output = "true";
                    break;
                }
                // cout << "True for :" << arr[i] << " and " << arr[j] << endl;
            }
        }
    }

    cout << output << endl;
}
