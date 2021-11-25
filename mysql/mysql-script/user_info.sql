CREATE TABLE user_info(
    id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stu_num varchar(254) UNIQUE,
    name varchar(30) NOT NULL,
    male bool NOT NULL
);

/* 表中的stu_num（学号）设置成字符串格式是为了与auth表中的对应起来 */

