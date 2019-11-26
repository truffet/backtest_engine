#!/bin/bash
if [ $# -eq 1 ] && [ "$1" = "help" ]; then
	printf "\ncreate [database_name] [database_name2] ...	>>	create one or more databases\n"
	printf "delete [database_name] [database_name2] ...	>>	delete one or more databases\n"
	printf "list	                                        >>	list of existing databases\n"

elif [ $# -eq 1 ] && [ "$1" = "list" ]; then
	echo "Listing existing databases"
	echo "\l" > temp.txt
	cat temp.txt | $OMNISCI_PATH/bin/omnisql -u truffet -p bodyboard
	rm temp.txt

elif [ $# -gt 1 ]; then

	if [ "$1" = "create" ]; then
		while [ "$2" != "" ]; do
			echo "creating database $2 if it does not exist already"
			echo "CREATE DATABASE IF NOT EXISTS $2 (owner = 'truffet');" > temp.txt
	 		cat temp.txt | $OMNISCI_PATH/bin/omnisql -u truffet -p bodyboard
	 		rm temp.txt
			echo "Execution over"
			shift
		done

	elif [ "$1" = "delete" ]; then
		while [ "$2" != "" ]; do
			echo "Deleting database $2 if it exists"
			echo "DROP DATABASE IF EXISTS $2;" > temp.txt
	 		cat temp.txt | $OMNISCI_PATH/bin/omnisql -u truffet -p bodyboard
	 		rm temp.txt
			echo "Execution over"
			shift
		done
	
	else
		echo "Use the 'help' argument to list available commands"
	
	fi

else
	echo "Use the 'help' argument to list available commands"

fi