#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x;  // Pointer storing the address of x

    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", (void*)&x);
    printf("Pointer Address: %p\n", (void*)ptr);
    printf("Pointer Dereference: %d\n", *ptr);

    return 0;
}

