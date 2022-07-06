-- 0x0E. SQL - More queries
-- Alex Senges
CREATE User 
IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL PRIVILEGES ON * . * TO `user_0d_1`@`localhost`;
FLUSH PRIVILEGES;

