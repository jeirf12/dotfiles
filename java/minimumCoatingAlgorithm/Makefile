CC:=javac
archives:=*.jar
folder:=bin
remove:=rm
removeFolder:=rm -rf

ifeq ($(OS),Windows_NT)
	remove:=del
	removeFolder:=rd /s/q
endif

all: 
	@$(CC) -d bin -sourcepath src src/negocio/*
	@$(CC) -d bin -sourcepath src src/presentacion/* -cp bin
	@jar cf minimumCoatingAlgorithm.jar -C bin .

run:
	@java -cp minimumCoatingAlgorithm.jar Test

clean:
	@$(remove) $(archives)
	@$(removeFolder) $(folder)

