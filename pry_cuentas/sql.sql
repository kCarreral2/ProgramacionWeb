-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.1.38-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para crud
CREATE DATABASE IF NOT EXISTS `crud` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `crud`;

-- Volcando estructura para tabla crud.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `idgrupo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT '',
  PRIMARY KEY (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla crud.grupo: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`idgrupo`, `descripcion`) VALUES
	(2, 'Activo'),
	(3, 'Pasivo'),
	(4, 'Patrimonio'),
	(5, 'Ingreso');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla crud.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `idplancuenta` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(100) NOT NULL DEFAULT '0',
  `grupoid` int(11) NOT NULL,
  `descripcion` varchar(100) DEFAULT '',
  `naturaleza` varchar(100) DEFAULT '',
  `estado` bit(1) NOT NULL,
  PRIMARY KEY (`idplancuenta`),
  KEY `grupoid` (`grupoid`),
  CONSTRAINT `FK_plancuenta_grupo` FOREIGN KEY (`grupoid`) REFERENCES `grupo` (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla crud.plancuenta: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `plancuenta` DISABLE KEYS */;
INSERT INTO `plancuenta` (`idplancuenta`, `codigo`, `grupoid`, `descripcion`, `naturaleza`, `estado`) VALUES
	(1, '001', 2, 'Caja', 'D', b'1'),
	(2, 'G002', 3, 'Banco', 'D', b'0');
/*!40000 ALTER TABLE `plancuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
