CREATE TABLE `order_info`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `stu_num` integer NOT NULL,
    `room_name`  varchar(30) NOT NULL,
    `room_mate1` varchar(254) NOT NULL,
    `room_mate2` varchar(254) NOT NULL,
    `room_mate3` varchar(254) NOT NULL
);
