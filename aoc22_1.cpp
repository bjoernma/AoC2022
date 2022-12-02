// compile with g++ -Wall -Wextra -Werror aoc22_1.cpp -o aoc22_1 
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <algorithm>
//int max_list(list);

//int max_list(list input) {
//return 0;
//}


int main(void) {

int max1_elf = 0;
int max2_elf = 0;
int max3_elf = 0;
int one_elf = 0;
int top3 = 0;
int cnt = 0;
int t_max1_elf = 0;
int t_max2_elf = 0;
int t_max3_elf = 0;
//int* idx1;
std::string tp;
std::string act;
using namespace std;
std::list<int> max_list;
//std::list<int>::iterator pos = max_list.begin();
fstream file;

file.open("input1.test");
if(file.is_open()) {

  while( getline(file, tp)) {
    cout << tp << "\n";

//        act = tp.strip();
    act = tp;
    if ( act.empty() ) {
      
      if (cnt < 3) {
        t_max1_elf = max2_elf;
        t_max2_elf = max3_elf;
        t_max3_elf = one_elf;
        cnt++;
      }
      if (cnt == 3) { // sort inital values...
        max1_elf = max(t_max1_elf,t_max2_elf,t_max3_elf)
        
      }
      if ( max3_elf < one_elf) {
        max1_elf = max2_elf;
        max2_elf = max3_elf;
        max3_elf = one_elf;
      }
      if ( max2_elf < max3_el

      if ( one_elf > max3_elf ) {
        max1_elf = max2_elf;
        max2_elf = max3_elf;
        max3_elf = one_elf;
      }
      if ( max1_elf < max3_elf) {
        max1_elf = max2_elf;
        max2_elf = max3_elf;
        max3_elf = one_elf;
      }
      cout << "after next elf calc." << "\n";
      std::cout << one_elf << "; Top 3: " << max1_elf << "; " << max2_elf << "; " << max3_elf << "; =" <<max1_elf+max2_elf+max3_elf << "\n";
      one_elf = 0;
    }
    else {
      one_elf += std::stoi(act);
    }
	}
  file.close();
//	max1_elf = std::max(max_list);
/*    idx1 = std::max_element(max_list);
    max1_elf = max_list[idx1]
    max_list.remove(max1_elf);
    max2_elf = std::max_element(max_list);
    max_list.remove(max2_elf);
    max3_elf = std::max_element(max_list);
    max_list.remove(max3_elf);*/
    top3 = max1_elf + max2_elf + max3_elf;

    std::cout << "Top 3: " << max1_elf << "; " << max2_elf << "; " << max3_elf << "; =" <<top3 << "\n";
    cout << "Max1_elf: " << max1_elf << "\n";
    return 0;
}
else return 1;
}
