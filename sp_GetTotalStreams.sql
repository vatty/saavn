USE `saavn`;
DROP procedure IF EXISTS `sp_GetTotalStreams`;

DELIMITER $$
USE `saavn`$$
CREATE PROCEDURE `sp_GetTotalStreams` ()
BEGIN
    select sum(streams) from language_dataset;
END$$

DELIMITER ;