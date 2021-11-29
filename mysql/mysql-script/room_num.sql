CREATE TABLE `room_num`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `dormitory_num` integer NOT NULL,
    `unit_num` integer NOT NULL,
    `room_name`  varchar(30) NOT NULL,
    `male` bool NOT NULL,
    `all_beds` integer NOT NULL,
    `free_beds` integer NOT NULL
);

INSERT INTO `dormitory`.`room_num`(`id`,`dormitory_num`,`unit_num`,`room_name`,`male`,`all_beds`,`free_beds`) VALUES
(1,5,1,'5101',TRUE,6,6),
(2,5,1,'5102',TRUE,6,6),
(3,5,2,'5201',FALSE,6,6),
(4,5,2,'5202',FALSE,6,6),
(5,5,3,'5301',TRUE,6,6),
(6,5,3,'5302',TRUE,6,6),
(7,8,1,'8101',TRUE,6,6),
(8,8,2,'8201',TRUE,6,6),
(9,9,1,'9101',TRUE,6,6),
(10,9,2,'9201',TRUE,6,6),
(11,13,1,'13101',FALSE,6,6),
(12,14,1,'14101',TRUE,6,6);

