package main 

func main ( ) { 
	var c int = 10; 
	var r int = 0; 
	
	for i := 1; i <= 5; i = i + 1{ 
		for k := 5; k <= 10; k = k + 2{ 
			for z := 1; z <= 12; z = z + 1{ 
				c = c * 5; 
			} 
			c = c * 10; 
			for z := 1; z <= 12; z = z + 1{ 
				c = c * 5; 
			} 
		} 
		r = r + 1; 
	} 
	
	for r <= 20{ 
		var d int = 10; 
		for d >= 5{ 
			r = r + 1; 
		} 
		r = r + 1; 
	} 
	
	for ok := true; ok; ok = (r<=30) { 
		r = r + 1; 
		for ok := true; ok; ok = (c<=5000) { 
			c = c + 20; 
		} 
		; 
	} 
	; 
	
	return 0; 
} 