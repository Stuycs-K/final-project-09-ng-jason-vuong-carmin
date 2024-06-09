decrypt: cipher2.py cipher.dat plain.dat
	@python3 cipher2.py cipher.dat plain.dat $(ARGS) output.dat decrypt

encrypt: cipher2.py cipher.dat plain.dat 
	@python3 cipher2.py cipher.dat plain.dat $(ARGS) output.dat encrypt