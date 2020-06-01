#include <stdio.h>
#include <stdlib.h>

#define PAGE_SIZE 1024

void calc(int logical_address) {
    int page_number;
    int offset;
    page_number = (int) logical_address / PAGE_SIZE;
    offset = logical_address % PAGE_SIZE;
    printf("logical_address=%i, page_number=%i, offset=%i\n", logical_address, page_number, offset);
}

int main() {
    calc(2456);
    calc(16382);
    calc(30000);
    calc(4385);
    exit(0);
}
