#include <cassert>
#include <iostream>
#include "../main.h"


int main() {
    // Test case
    int result = add(1, 1);
    assert(result == 2);
    
    std::cout << "✓ All tests passed" << std::endl;
    return 0;
}