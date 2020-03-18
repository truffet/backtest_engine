from init import setup_env
from update_db import update

def main():

	#setup environment (create db & tables)
	setup_env()

	#upload new data to database
	update()



main()