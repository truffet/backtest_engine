#!/bin/bash
bash ../../init/manage_db.sh create bitmex
cat init_table.sql | $OMNISCI_PATH/bin/omnisql -u truffet -p bodyboard
python update_db.py
# to check if successful:
# bash ../../init/manage_db.sh list