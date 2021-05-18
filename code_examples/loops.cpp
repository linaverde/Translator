int main() {
    int c = 10;
    int r = 0;

    for (int i = 1; i <= 5; i = i + 1) {
        r = r + 1;
    }

    while (r <= 20) {
        r = r + 1;
    }

    do {
        r = r + 1;
    } 
    while (r <= 30);

    return 0;
}