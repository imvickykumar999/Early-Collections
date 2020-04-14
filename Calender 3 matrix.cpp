/*
Wanna Find any day between year 2001 and 2100

...Try to find Day on your next Birthday ;)

Press < RUN > ...(at bottom right)
---------------------------------
Write year as 19 (for example)
Press Enter

Write month as 12
Press Enter

Write date as 27
Press Submit

>>> You will get output as Friday ??
*/


#include <iostream>
using namespace std;
#define t 40

char year[28] = {'A', 'B', 'C', 'K', 'F', 'G', 'A', 'I', 'D', 'E', 'F', 'N', 'B', 'C', 'D', 'L', 'G', 'A', 'B', 'J', 'E', 'F', 'G', 'H', 'C', 'D', 'E', 'M'};
int month[2][12] = {{1, 4, 4, 7, 2, 5, 7, 3, 6, 1, 4, 6}, {1, 4, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7}};
char day[7][10] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
int i, k, j, y, m, d, one[100], two[14][12];

void setyear();
void setmonth(int p, int q);

int main()
{
    setyear();
    setmonth(7, 0);
    setmonth(14, 1);
        while (1)
    {
    //  xy:
        for (k = 0; k < t; k++)
            cout << "_";
        cout << "\n\nFormat is YY/MM/DD...";
        cout << "\nEnter Year (2001 to 2100) : ";
        cin >> y;
        cout << "Enter Month : ";
        cin >> m;
        cout << "Enter Date : ";
        cin >> d;
        if (y < 1 || y > 100 || m < 1 || m > 12 || d < 1 || d > 31)
        {
            cout << "\nThis Date does not exist... Try Again!!!\n";
            //    goto xy;
            return 0;
        }
        cout << "\nD'day is ";
        cout << day[(d - 1 + two[one[y - 1] - 1][m - 1]) % 7];
        cout << endl;
    }
    return 0;
}

void setyear()
{
    for (i = j = 0; i < 99; i++)
    {
        j %= 28;
        one[i] = int(year[j++]) - 64;
        //        cout<<i+1<<"\t"<<(one[i])<<endl;
    }
    one[99]=5;
}

void setmonth(int p, int q)
{
    for (i = p - 7; i < p; i++)
    {
        for (j = 0; j < 12; j++)
        {
            month[q][j] %= 7;
            two[i][j] = month[q][j]++;
            //                cout<<two[i][j]<<"\t";
        }
        //        cout<<endl;
    }
    //    cout<<endl;
}
