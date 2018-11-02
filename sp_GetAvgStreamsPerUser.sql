USE `saavn`;
DROP procedure IF EXISTS `sp_GetAvgStreamsPerUser`;

DELIMITER $$
USE `saavn`$$
CREATE PROCEDURE `sp_GetAvgStreamsPerUser` ()
BEGIN
    select avg(streams) from language_dataset;
END$$

DELIMITER ;