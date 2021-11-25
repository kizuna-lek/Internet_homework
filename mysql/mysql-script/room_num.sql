CREATE TABLE `room_num`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `dormitory_num` integer,
    `unit_num` integer NOT NULL,
    `room_name`  varchar(30) NOT NULL,
    `male` bool NOT NULL,
    `all_beds` integer NOT NULL,
    `free_beds` integer NOT NULL
);
