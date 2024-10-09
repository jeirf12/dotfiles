CC:=javac
archives:=*.jar
folder:=bin
remove:=rm
removeFolder:=rmdir

ifeq ($(OS),Windows_NT)
	remove:=del
	removeFolder:=rd /s/q
endif

all: 
	@$(CC) -d bin -sourcepath src src/negocio/*
	@$(CC) -d bin -sourcepath src src/presentacion/* -cp bin
	@jar cf main.jar -C bin .

run:
	@java -cp main.jar Test

clean:
	@$(remove) $(archives)
	@$(removeFolder) $(folder)
