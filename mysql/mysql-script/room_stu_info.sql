CREATE TABLE `room_stu_info`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `room_id` integer NOT NULL,
    `room_name` varchar(30) NOT NULL,
    `room_mate1` varchar(254) NOT NULL,
    `room_mate2` varchar(254) NOT NULL,
    `room_mate3` varchar(254) NOT NULL,
    `room_mate4` varchar(254) NOT NULL,
    `room_mate5` varchar(254) NOT NULL,
    `room_mate6` varchar(254) NOT NULL
);
