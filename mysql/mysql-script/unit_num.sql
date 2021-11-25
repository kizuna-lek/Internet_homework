CREATE TABLE `unit_num`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `dormitory_num` integer,
    `unit_num` integer NOT NULL,
    `unit_name` varchar(30) NOT NULL
);

INSERT INTO `dormitory`.`unit_num` (`id`,`dormitory_num`,`unit_num`,`unit_name`) VALUES
(1,5,1,'domitory 5 unit 1'),
(2,5,2,'domitory 5 unit 2'),
(3,5,3,'domitory 5 unit 3'),
(4,8,1,'domitory 8 unit 1'),
(5,8,2,'domitory 8 unit 2'),
(6,9,1,'domitory 9 unit 1'),
(7,9,2,'domitory 9 unit 2'),
(8,13,1,'domitory 13 unit 1'),
(9,14,1,'domitory 14 unit 1');
