/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.6.24 : Database - company
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`company` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `company`;

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `deptno` int(11) NOT NULL,
  `dname` varchar(20) DEFAULT NULL,
  `loc` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`deptno`),
  KEY `index_dept` (`deptno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `dept` */

insert  into `dept`(`deptno`,`dname`,`loc`) values 
(10,'董事部','江东'),
(20,'公关部','四川'),
(30,'武统部','咸阳'),
(40,'财务部','洛阳');

/*Table structure for table `employees` */

DROP TABLE IF EXISTS `employees`;

CREATE TABLE `employees` (
  `empno` int(11) NOT NULL,
  `ename` varchar(20) DEFAULT NULL,
  `job` varchar(40) DEFAULT NULL,
  `MGR` int(11) DEFAULT NULL,
  `hiredate` date DEFAULT NULL,
  `sal` double(10,2) DEFAULT NULL,
  `comm` double(10,2) DEFAULT NULL,
  `deptno` int(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_deptno` (`deptno`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`deptno`) REFERENCES `dept` (`deptno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `employees` */

insert  into `employees`(`empno`,`ename`,`job`,`MGR`,`hiredate`,`sal`,`comm`,`deptno`) values 
(7369,'周瑜','高级公关',7566,'1981-03-21',1800.00,NULL,20),
(7499,'张飞','武装教习',7698,'1982-03-21',2600.00,300.00,30),
(7521,'关二爷','武装副司令',7698,'1983-03-21',2250.00,500.00,30),
(7566,'孙权','经理',7839,'1981-03-21',3975.00,NULL,10),
(7654,'黄忠','武装司令',7698,'1981-03-21',2250.00,1400.00,30),
(7698,'刘备','经理',7839,'1984-03-21',3850.00,NULL,10),
(7782,'曹操','经理',7839,'1985-03-21',3450.00,NULL,10),
(7788,'许褚','武装上将',7782,'1981-03-21',4000.00,NULL,30),
(7839,'汉献帝','董事长',NULL,'1981-03-21',6000.00,NULL,10),
(7844,'魏延','武装上将',7698,'1989-03-21',2500.00,0.00,30),
(7876,'黄盖','人事专员',7566,'1998-03-21',2100.00,NULL,20),
(7902,'荀彧','分析员',7782,'2005-03-12',4000.00,NULL,20),
(7934,'甘宁','中级公关',7782,'1981-03-21',2300.00,NULL,20),
(7952,'马超','武装大校',7698,'2001-03-21',2750.00,0.00,30),
(7953,'吕布','武装教习',7698,'2001-03-21',2750.00,0.00,30);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
