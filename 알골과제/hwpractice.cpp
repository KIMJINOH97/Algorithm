#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> sorted(100000000);
vector <int> v[6];
vector <int> v2[6];

void merge(int o, int low, int mid, int high){
   int i,j,k;
   i=low;
   j=mid+1;
   k=low;
   
   while(i<=mid && j<=high){
      if(v[o][i]<v[o][j]){
         sorted[k]=v[o][i];
         i++;
      }
      else{
         sorted[k]=v[o][j];
         j++;
      }
      k++;
   }
   if(i>mid){
      for(int l=j; l<=high; l++){
         sorted[k++]=v[o][l];
      }
   }
   else{
      for(int l=i; l<=mid; l++){
         sorted[k++]=v[o][l];
      }
   }
   for(int i=low; i<=high; i++){
      v[o][i]=sorted[i];
   }
}
void merge_sort(int order, int low, int high){
   int mid;
   if(low<high){
      mid=(low+high)/2;
      merge_sort(order,low, mid);
      merge_sort(order,mid+1, high);
      merge(order,low, mid, high);   
   }
}


void swap(int o,int a, int b){
   int temp=v2[o][a];
   v2[o][a]=v2[o][b];
   v2[o][b]=temp;
}

int partition(int o,int left, int right){
   int pivot=v2[o][left];
   int low=left+1;
   int high=right;
   
   while(low<=high){
      while(low<=right && pivot>=v2[o][low]){
         low++;
      }
      while(high>=(left+1) && pivot<=v2[o][high]){
         high--;
      }
      if(low<=high){
         swap(o,low,high);
      }
   }
   swap(o,left,high);
   return high;
}

void quick_sort(int o,int low, int high){
   if(low<=high){
      int pivot=partition(o,low,high);
      quick_sort(o,low,pivot-1);
      quick_sort(o,pivot+1,high);
   }
   
}

int main(){
   srand((unsigned int)time(NULL));
   int n;
   for(int i=0; i<6; i++){
      cin>>n;
      for(int j=0; j<n; j++){
         v[i].push_back(rand());
         v2[i].push_back(rand());
         }   
   }
   cout<<"input complete"<<endl;
      
   for(int i=0; i<3; i++){   
   sort(v[i].begin(), v[i].end());
   sort(v2[i].begin(), v2[i].end());
   }   
   
   for(int i=0; i<3; i++){
      clock_t startTime = clock();
      merge_sort(i, 0, v[i].size()-1);
      printf("%lf\n", (float)(clock() - startTime)/CLOCKS_PER_SEC);
   }


   for(int i=0; i<3; i++){
      clock_t startTime = clock();
      quick_sort(i, 0, v[i].size()-1);
      printf("%lf\n", (float)(clock() - startTime)/CLOCKS_PER_SEC);
   }

   for(int i=3; i<6; i++){
      clock_t startTime = clock();
      merge_sort(i, 0, v[i].size()-1);
      printf("%lf\n", (float)(clock() - startTime)/CLOCKS_PER_SEC);
   }

   
   for(int i=3; i<6; i++){
      clock_t startTime = clock();
      quick_sort(i, 0, v[i].size()-1);
      printf("%lf\n", (float)(clock() - startTime)/CLOCKS_PER_SEC);
   }
   return 0;
}