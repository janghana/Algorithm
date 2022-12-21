#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);
 
    int init, N;
    int count = 0;
    std::cin >> init;
 
    N = init;
 
    do {
        N = (N % 10) * 10 + ((N / 10) + (N % 10)) % 10;
 
        count++;
    } while (init != N);
    std::cout << count;
    
    return 0;
}
