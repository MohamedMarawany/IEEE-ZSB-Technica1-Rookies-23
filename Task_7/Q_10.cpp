#include <iostream>
#include<bits/stdc++.h>
 
using namespace std;
 
int toggle(int n)
{
    if(n == 1){
        return 0;
    }
    else if(n == 0){
        return 1;
    }
}
 
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);
 
    int arr_1[3][3];
    int arr_2[3][3] = { {1,1,1}, {1,1,1}, {1,1,1} };
 
    for(int i = 0 ; i < 3 ; i++){
        for(int j = 0 ; j < 3 ; j++){
            cin >> arr_1[i][j];
            if(arr_1[i][j] % 2 != 0){
                arr_2[i][j] = toggle(arr_2[i][j]);
                if(i <= 1){
                    arr_2[i + 1][j] = toggle(arr_2[i + 1][j]);
                }
                if(j <= 1){
                    arr_2[i][j + 1]  = toggle(arr_2[i][j + 1]);
                }
                if (i >= 1){
                    arr_2[i - 1][j] = toggle(arr_2[i - 1][j]);
                }
                if (j >= 1 ){
                    arr_2[i][j - 1] = toggle(arr_2[i][j - 1]);
                }
            }
        }
    }
 
    for(int i = 0 ; i < 3 ; i++){
        for(int j = 0 ; j < 3 ; j++){
            cout << arr_2[i][j];
        }
        cout << endl;
    }
}
