USE `saavn`;
DROP procedure IF EXISTS `sp_GetTotalUids`;

DELIMITER $$
USE `saavn`$$
CREATE PROCEDURE `sp_GetTotalUids` ()
BEGIN
    select count(uid) from language_dataset;
END$$

DELIMITER ;