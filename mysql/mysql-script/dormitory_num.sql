CREATE TABLE `dormitory_num`(
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `dormitory_name` varchar(30) NOT NULL,
    `dormitory_num` integer UNIQUE
);

INSERT INTO `dormitory`.`dormitory_num` (`id`,`dormitory_name`,`dormitory_num`) VALUES
(1,'number 5',5),
(2,'number 8',8),
(3,'number 9',9),
(4,'number 13',13),
(5,'number 14',14);
