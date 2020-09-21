CC := gcc
CFLAGS := ./src/main.c ./inc/bme280.c -I ./inc/ -o bin/main

SRCFILES := $(wildcard *.c)

all: $(SRCFILES)
	$(CC) $(CFLAGS)