CC:=javac
archives:=*.class
remove := rm

ifeq ($(OS),Windows_NT)
	remove := del
endif

all: 
	@$(CC) *.java

run:
	@java Test

clean:
	@$(remove) $(archives)
