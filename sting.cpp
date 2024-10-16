// # Implement Check if it is possible to transform one
// # string to another.
// # Statement Given two strings s1 and s2 (all letters in uppercase).
// # Check if it is possible to convert s1 to s2 by performing following
// # operations.
// # 1. Make some lowercase letters uppercase.
// # 2. Delete all the lowercase letters.
// # Input: s1 = daBcd s2 = ABC Output: yes
// # Input: s1 = argaju s2 = RAJ Output: yes


#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int main(void)
{
    vector<int> v1;
    vector<char> v2;
    string str1 = "daBcd";

    string str2 = "ABC";
    int size1 = str1.size();
    int size2 = str2.size();
    int count = 0;
    for (int i = 0; i < size1; i++)
    {
        bool flag = false;
        for (int j = 0; j < size2; j++)
        {
            if (tolower(str1[i]) == tolower(str2[j]))
            {
                // cout << (char)tolower(str1[i]) << endl;
                v2.push_back(char(tolower(str1[i])));
                flag = true;
                break;
            }
        }
        if (flag == true)
            count++;
    }

    if (count == size2)
        cout << "Yes\n";
    else
        cout << "No\n";
}