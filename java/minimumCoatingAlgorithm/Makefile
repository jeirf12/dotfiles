CC:=javac
archives:=*.class

ifeq ($(OS),Windows_NT)
	remove := del
else
	remove := rm
endif

all: 
	@$(CC) *.java

run:
	@java Test

clean:
	@$(remove) $(archives)
