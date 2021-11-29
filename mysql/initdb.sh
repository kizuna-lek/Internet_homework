#! /bin/bash
mysql -uroot -p$MYSQL_ROOT_PASSWORD <<EOF

source /usr/local/sql/init.sql
source /usr/local/sql/user_info.sql
source /usr/local/sql/dormitory_num.sql
source /usr/local/sql/unit_num.sql
source /usr/local/sql/room_num.sql
source /usr/local/sql/order.sql
source /usr/local/sql/order_info.sql
source /usr/local/sql/room_stu_info.sql
