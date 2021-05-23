int main() {
    int c = 10;
    int r = 0;

    for (int i = 1; i <= 5; i = i + 1) { 
        for (int k = 5; k <= 10; k = k + 2){ 
            for (int z = 1; z <= 12; z = z + 1) { 
                c = c * 5;
            }   
            c = c * 10;
            for (int z = 1; z <= 12; z = z + 1) {  
                c = c * 5;
            }   
        }
        r = r + 1;
    }

    while (r <= 20) {
        int d = 10;
        while (d >= 5){
            r = r + 1;
        }
        r = r + 1;
    }

    do {
        r = r + 1;
        do{
            c = c + 20;
        }
        while (c <= 5000);
    }
    while (r <= 30);

    return 0;
}