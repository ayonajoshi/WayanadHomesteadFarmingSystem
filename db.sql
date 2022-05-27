/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - homestead1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`homestead1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `homestead1`;

/*Table structure for table `advertisement` */

DROP TABLE IF EXISTS `advertisement`;

CREATE TABLE `advertisement` (
  `adid` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(190) DEFAULT NULL,
  `product_image` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`adid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `advertisement` */

insert  into `advertisement`(`adid`,`product_name`,`product_image`,`description`,`userid`) values 
(5,'hghghj','jbnjbn','nnnkjnk',5);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `userInfo` int(11) DEFAULT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `date` varchar(70) DEFAULT NULL,
  `status` varchar(190) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`userInfo`,`complaint`,`reply`,`date`,`status`) values 
(1,6,'bad\n','pending','2022-03-19','pending'),
(2,6,'rotten','pending','2022-03-19','pending'),
(3,6,'gbgvt\n','pending','2022-03-19','pending');

/*Table structure for table `delivery_boy` */

DROP TABLE IF EXISTS `delivery_boy`;

CREATE TABLE `delivery_boy` (
  `delev_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pin` varchar(60) DEFAULT NULL,
  `post` varchar(170) DEFAULT NULL,
  `image` varchar(150) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`delev_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `delivery_boy` */

insert  into `delivery_boy`(`delev_id`,`name`,`place`,`pin`,`post`,`image`,`email`,`contact`,`lid`) values 
(3,'Chinchu','Karani','673596','Karani','/static/item/Screenshot (2).png','chinchuay@gmail.com','0092736232',3),
(4,'sabvj','vbjhcxgj','673596','fttgt','/static/delivery_boy/back ground image.png','chinchuay@gmail.com','667543884959',4);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feed_id` int(11) NOT NULL AUTO_INCREMENT,
  `ulid` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feed_id`,`ulid`,`feedback`,`date`) values 
(1,1,'qqqq','2016-01-01'),
(2,1,'eeee','1970-01-28'),
(3,6,'gdhuru','2022-03-17');

/*Table structure for table `fertilizer` */

DROP TABLE IF EXISTS `fertilizer`;

CREATE TABLE `fertilizer` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  `image` varchar(170) DEFAULT NULL,
  `specification` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer` */

insert  into `fertilizer`(`fid`,`name`,`type`,`image`,`specification`) values 
(1,'flu','organic','/static/fert_pest/images (37).jpg','hope for it'),
(2,'pint','chemical','/static/fert_pest/images.jpg','spray');

/*Table structure for table `items` */

DROP TABLE IF EXISTS `items`;

CREATE TABLE `items` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `image` varchar(150) DEFAULT NULL,
  `price` varchar(60) DEFAULT NULL,
  `description` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `items` */

insert  into `items`(`item_id`,`name`,`image`,`price`,`description`) values 
(2,'Beetroot','/static/item/download.jpeg','900',' fresh and grownup without chemicals'),
(3,'Kachil(Yam)','/static/item/download.jpg','57778 ','Homely cultivated with organic manure');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) DEFAULT NULL,
  `password` varchar(60) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'bi','888','delivery_boy'),
(2,'no','000','delivery_boy'),
(3,'come','999','delivery_boy'),
(4,'yes','555','delivery_boy'),
(5,'go','333','admin'),
(6,'a','7','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` int(11) DEFAULT NULL,
  `date` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`n_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `offers` */

DROP TABLE IF EXISTS `offers`;

CREATE TABLE `offers` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `offer_id` int(11) DEFAULT NULL,
  `date` varchar(170) DEFAULT NULL,
  `description` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `offers` */

insert  into `offers`(`product_id`,`offer_id`,`date`,`description`) values 
(1,1,'02-02-2020','fgfffdtduyyrydrdfgdedsesesess');

/*Table structure for table `pesticide` */

DROP TABLE IF EXISTS `pesticide`;

CREATE TABLE `pesticide` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  `image` varchar(160) DEFAULT NULL,
  `specification` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `pesticide` */

insert  into `pesticide`(`pid`,`name`,`type`,`image`,`specification`) values 
(4,'small','chemical','/static/fert_pest/download (4).jpg','you are here'),
(6,'small','organic','/static/fert_pest/Annotation 2020-05-04 183543.png','yugujhb'),
(9,'aaaa','chemical','/static/fert_pest/WIN_20200108_13_51_06_Pro.jpg','xcdgdfs'),
(10,'nnnnnnnnnnnnnnn','chemical','/static/fert_pest/download (6).jpg','zxnhgfes'),
(13,'pint','organic','/static/fert_pest/images (1).png','look aside');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`item_id`,`user_id`) values 
(1,2,6),
(2,3,6),
(3,2,6),
(4,3,5),
(5,3,5),
(6,2,6);

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rate_id` int(11) NOT NULL AUTO_INCREMENT,
  `ulid` int(11) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `date` varchar(70) DEFAULT NULL,
  `username` varchar(170) DEFAULT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rate_id`,`ulid`,`rating`,`date`,`username`) values 
(1,1,3.5,'2022-02-02',NULL),
(2,2,5,'2022-02-02',NULL),
(3,5,4.5,'2022-02-02',NULL);

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) DEFAULT NULL,
  `ulid` int(11) DEFAULT NULL,
  `review` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`item_id`,`ulid`,`review`,`date`) values 
(1,2,1,'good one','2020-02-02');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(60) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `image` varchar(150) DEFAULT NULL,
  `gender` varchar(60) DEFAULT NULL,
  `place` varchar(60) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `post` varchar(60) DEFAULT NULL,
  `district` varchar(60) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `latitude` varchar(70) DEFAULT NULL,
  `longitude` varchar(70) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`name`,`image`,`gender`,`place`,`pin`,`post`,`district`,`phone`,`email`,`latitude`,`longitude`,`lid`) values 
(1,'era','','f','goa',13456,'weeh','qqsad',899999987,'se@gmail.com','east','west',1),
(2,'ammu',NULL,'m','ugd',67856,'kg','nvfjn',NULL,NULL,NULL,NULL,2),
(3,'annu',NULL,NULL,NULL,NULL,NULL,NULL,987654532,NULL,NULL,NULL,5);

/*Table structure for table `wishlist` */

DROP TABLE IF EXISTS `wishlist`;

CREATE TABLE `wishlist` (
  `list_id` int(11) NOT NULL AUTO_INCREMENT,
  `ulid` int(11) DEFAULT NULL,
  `itemid` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date` int(11) DEFAULT NULL,
  PRIMARY KEY (`list_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `wishlist` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
