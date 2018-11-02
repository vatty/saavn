USE `saavn`;
DROP procedure IF EXISTS `sp_GetUniqueTotalUids`;

DELIMITER $$
USE `saavn`$$
CREATE PROCEDURE `sp_GetUniqueTotalUids` ()
BEGIN
    select count(distinct uid) from language_dataset;
END$$

DELIMITER ;