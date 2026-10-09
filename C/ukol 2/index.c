#include <stdio.h>

int main(void) {
    int box = 6;
    int choco = 125;
    float price = 1.45;

    int res = choco / box;

    printf("%d\n", res);

    int mod = choco % box;
    printf("%d\n", mod);
    
    int total = choco * price;
    printf("%d\n", total);

    return 0;
}