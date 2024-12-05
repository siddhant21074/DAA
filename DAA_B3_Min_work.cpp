// # Implement a problem of minimum work to be done
// # per day to finish given tasks within D days problem.
// # Statement: Given an array task[] of size N denoting
// # amount of work to be done for each task, the problem
// # is to find the minimum amount of work to be done on
// # each day so that all the tasks can be completed in at
// # most D days.
// # Note: On one day work can be done for only one task.
// # Input: task[] = [3, 4, 7, 15], D = 10
// # Output: 4
// # Input: task[] = [30, 20, 22, 4, 21], D = 6
// # Output: 22

#include <iostream>

using namespace std;

int cal_work(int task[], int low, int size)
{
    int temp = 0;
    for (int i = 0; i < size; i++)
    {
        temp += (task[i] + low - 1) / low;
    }
    return temp;
}

int main(void)
{

    int size, days, low = 1;

    cout << "Enter the number of tasks : ";
    cin >> size;

    int task[10];

    cout << "Enter the number of days : ";
    cin >> days;

    for (int i = 0; i < size; i++)
    {
        cout<<"Enter the number: ";
        cin>>task[i];
    }

    while (true)
    {
        int work = cal_work(task, low, size);
        if (work < days)
        {
            cout << "min days: " << low << endl;
        }

        low++;
    }
}