CC=gcc
all:
	# $(CC) -shared vetor.c vetor.h -o libvectors.so
	$(CC) main.c vetor.c vetor.h
clean:
	#rm -f libvectors.so
	rm -f a.out
install:
	install  -m 0644 libvectors.so /usr/local/lib
	install -m 0644 vetor.h vetor.c /usr/local/include

uninstall:
	rm -f /usr/local/lib/libvectors.so
	rm -f /usr/local/include/vetor.h
	rm -f /usr/local/include/vetor.c
