int main() {
    
    int a = 10;
    int b = 20;
    int c = 0;
    bool too = true;
    bool foo = false;
    bool roo;

    c = a + b;
    c = a - b;
    c = a * b;
    c = a / b;
    c = a % b;

    roo = ! foo;
    roo = too || foo;
    roo = foo && too;

    foo = a > b;
    foo = a < b;
    foo = a >= b;
    foo = a <= b;
    foo = a == b;
    foo = a != b;

    return 0;
}