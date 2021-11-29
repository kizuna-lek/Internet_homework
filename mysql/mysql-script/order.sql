CREATE TABLE `order`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `stu_num` varchar(254),
    `dormitory_num` integer NOT NULL,
    `male` bool NOT NULL,
    `people_num` integer NOT NULL,
    `is_correct` bool NOT NULL
);
