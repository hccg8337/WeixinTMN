-- MySQL dump 10.13  Distrib 5.6.34, for Linux (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.6.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `action_action`
--

DROP TABLE IF EXISTS `action_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cnname` varchar(50) NOT NULL,
  `comments` varchar(200) NOT NULL,
  `state` int(11) NOT NULL,
  `moduleid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `action_action_moduleid_id_3318c863_fk_module_module_id` (`moduleid_id`),
  CONSTRAINT `action_action_moduleid_id_3318c863_fk_module_module_id` FOREIGN KEY (`moduleid_id`) REFERENCES `module_module` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_action`
--

LOCK TABLES `action_action` WRITE;
/*!40000 ALTER TABLE `action_action` DISABLE KEYS */;
/*!40000 ALTER TABLE `action_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add module',7,'add_module'),(20,'Can change module',7,'change_module'),(21,'Can delete module',7,'delete_module'),(25,'Can add game',9,'add_game'),(26,'Can change game',9,'change_game'),(27,'Can delete game',9,'delete_game'),(28,'Can add action',10,'add_action'),(29,'Can change action',10,'change_action'),(30,'Can delete action',10,'delete_action'),(31,'Can add date2 games template',11,'add_date2gamestemplate'),(32,'Can change date2 games template',11,'change_date2gamestemplate'),(33,'Can delete date2 games template',11,'delete_date2gamestemplate'),(34,'Can add games template',12,'add_gamestemplate'),(35,'Can change games template',12,'change_gamestemplate'),(36,'Can delete games template',12,'delete_gamestemplate'),(37,'Can add log',13,'add_log'),(38,'Can change log',13,'change_log'),(39,'Can delete log',13,'delete_log'),(40,'Can add nodes line',14,'add_nodesline'),(41,'Can change nodes line',14,'change_nodesline'),(42,'Can delete nodes line',14,'delete_nodesline'),(43,'Can add node relationship',15,'add_noderelationship'),(44,'Can change node relationship',15,'change_noderelationship'),(45,'Can delete node relationship',15,'delete_noderelationship'),(46,'Can add node',16,'add_node'),(47,'Can change node',16,'change_node'),(48,'Can delete node',16,'delete_node'),(49,'Can add custom user',17,'add_customuser'),(50,'Can change custom user',17,'change_customuser'),(51,'Can delete custom user',17,'delete_customuser'),(52,'Can add nodes template',18,'add_nodestemplate'),(53,'Can change nodes template',18,'change_nodestemplate'),(54,'Can delete nodes template',18,'delete_nodestemplate'),(55,'Can add role',19,'add_role'),(56,'Can change role',19,'change_role'),(57,'Can delete role',19,'delete_role'),(58,'Can add users group',20,'add_usersgroup'),(59,'Can change users group',20,'change_usersgroup'),(60,'Can delete users group',20,'delete_usersgroup'),(61,'Can add config',21,'add_config'),(62,'Can change config',21,'change_config'),(63,'Can delete config',21,'delete_config'),(64,'Can add msg structure',22,'add_msgstructure'),(65,'Can change msg structure',22,'change_msgstructure'),(66,'Can delete msg structure',22,'delete_msgstructure'),(67,'Can add msg state',23,'add_msgstate'),(68,'Can change msg state',23,'change_msgstate'),(69,'Can delete msg state',23,'delete_msgstate'),(70,'Can add msg',24,'add_msg'),(71,'Can change msg',24,'change_msg'),(72,'Can delete msg',24,'delete_msg'),(73,'Can add weixin config',25,'add_weixinconfig'),(74,'Can change weixin config',25,'change_weixinconfig'),(75,'Can delete weixin config',25,'delete_weixinconfig');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config_config`
--

DROP TABLE IF EXISTS `config_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config_config`
--

LOCK TABLES `config_config` WRITE;
/*!40000 ALTER TABLE `config_config` DISABLE KEYS */;
/*!40000 ALTER TABLE `config_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_customuser`
--

DROP TABLE IF EXISTS `custom_user_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_user_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unionid` varchar(100) DEFAULT NULL,
  `nickname` varchar(50) NOT NULL,
  `userid` varchar(100) DEFAULT NULL,
  `code` varchar(100) DEFAULT NULL,
  `openid` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_customuser_unionid_9a6384c9_uniq` (`unionid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_customuser`
--

LOCK TABLES `custom_user_customuser` WRITE;
/*!40000 ALTER TABLE `custom_user_customuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_customuser_actions`
--

DROP TABLE IF EXISTS `custom_user_customuser_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_user_customuser_actions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `action_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_customuser_actions_customuser_id_c9a03882_uniq` (`customuser_id`,`action_id`),
  KEY `custom_user_customuser_ac_action_id_54b6b096_fk_action_action_id` (`action_id`),
  CONSTRAINT `custom_user__customuser_id_06681434_fk_custom_user_customuser_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user_customuser` (`id`),
  CONSTRAINT `custom_user_customuser_ac_action_id_54b6b096_fk_action_action_id` FOREIGN KEY (`action_id`) REFERENCES `action_action` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_customuser_actions`
--

LOCK TABLES `custom_user_customuser_actions` WRITE;
/*!40000 ALTER TABLE `custom_user_customuser_actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_customuser_actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_customuser_games`
--

DROP TABLE IF EXISTS `custom_user_customuser_games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_user_customuser_games` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_customuser_games_customuser_id_fa501a9a_uniq` (`customuser_id`,`game_id`),
  KEY `custom_user_customuser_games_game_id_ef95b028_fk_game_game_id` (`game_id`),
  CONSTRAINT `custom_user__customuser_id_f05aa39d_fk_custom_user_customuser_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user_customuser` (`id`),
  CONSTRAINT `custom_user_customuser_games_game_id_ef95b028_fk_game_game_id` FOREIGN KEY (`game_id`) REFERENCES `game_game` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_customuser_games`
--

LOCK TABLES `custom_user_customuser_games` WRITE;
/*!40000 ALTER TABLE `custom_user_customuser_games` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_customuser_games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_customuser_nodes`
--

DROP TABLE IF EXISTS `custom_user_customuser_nodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_user_customuser_nodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_customuser_nodes_customuser_id_22085203_uniq` (`customuser_id`,`node_id`),
  KEY `custom_user_customuser_nodes_node_id_d3389cc5_fk_node_node_id` (`node_id`),
  CONSTRAINT `custom_user__customuser_id_1a5c64c7_fk_custom_user_customuser_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user_customuser` (`id`),
  CONSTRAINT `custom_user_customuser_nodes_node_id_d3389cc5_fk_node_node_id` FOREIGN KEY (`node_id`) REFERENCES `node_node` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_customuser_nodes`
--

LOCK TABLES `custom_user_customuser_nodes` WRITE;
/*!40000 ALTER TABLE `custom_user_customuser_nodes` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_customuser_nodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_customuser_roles`
--

DROP TABLE IF EXISTS `custom_user_customuser_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_user_customuser_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_customuser_roles_customuser_id_14fce458_uniq` (`customuser_id`,`role_id`),
  KEY `custom_user_customuser_roles_role_id_99847734_fk_role_role_id` (`role_id`),
  CONSTRAINT `custom_user__customuser_id_8451290f_fk_custom_user_customuser_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user_customuser` (`id`),
  CONSTRAINT `custom_user_customuser_roles_role_id_99847734_fk_role_role_id` FOREIGN KEY (`role_id`) REFERENCES `role_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_customuser_roles`
--

LOCK TABLES `custom_user_customuser_roles` WRITE;
/*!40000 ALTER TABLE `custom_user_customuser_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_customuser_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_customuser_usersgroups`
--

DROP TABLE IF EXISTS `custom_user_customuser_usersgroups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_user_customuser_usersgroups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `usersgroup_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_customuser_usersgroup_customuser_id_ca8f2443_uniq` (`customuser_id`,`usersgroup_id`),
  KEY `custom_user__usersgroup_id_d369ca43_fk_users_group_usersgroup_id` (`usersgroup_id`),
  CONSTRAINT `custom_user__customuser_id_b8170785_fk_custom_user_customuser_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user_customuser` (`id`),
  CONSTRAINT `custom_user__usersgroup_id_d369ca43_fk_users_group_usersgroup_id` FOREIGN KEY (`usersgroup_id`) REFERENCES `users_group_usersgroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_customuser_usersgroups`
--

LOCK TABLES `custom_user_customuser_usersgroups` WRITE;
/*!40000 ALTER TABLE `custom_user_customuser_usersgroups` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_customuser_usersgroups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (10,'action','action'),(1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(21,'config','config'),(5,'contenttypes','contenttype'),(17,'custom_user','customuser'),(9,'game','game'),(11,'games_template','date2gamestemplate'),(12,'games_template','gamestemplate'),(13,'log','log'),(7,'module','module'),(24,'msg','msg'),(23,'msg','msgstate'),(22,'msg','msgstructure'),(16,'node','node'),(15,'node','noderelationship'),(14,'node','nodesline'),(18,'nodes_template','nodestemplate'),(19,'role','role'),(6,'sessions','session'),(20,'users_group','usersgroup'),(25,'weixin_interface','weixinconfig');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-02-09 02:51:11.034158'),(2,'auth','0001_initial','2017-02-09 02:51:12.985614'),(3,'admin','0001_initial','2017-02-09 02:51:13.413163'),(4,'admin','0002_logentry_remove_auto_add','2017-02-09 02:51:13.530000'),(5,'contenttypes','0002_remove_content_type_name','2017-02-09 02:51:14.121513'),(6,'auth','0002_alter_permission_name_max_length','2017-02-09 02:51:14.227771'),(7,'auth','0003_alter_user_email_max_length','2017-02-09 02:51:14.296762'),(8,'auth','0004_alter_user_username_opts','2017-02-09 02:51:14.325692'),(9,'auth','0005_alter_user_last_login_null','2017-02-09 02:51:14.380380'),(10,'auth','0006_require_contenttypes_0002','2017-02-09 02:51:14.385003'),(11,'auth','0007_alter_validators_add_error_messages','2017-02-09 02:51:14.423192'),(12,'auth','0008_alter_user_username_max_length','2017-02-09 02:51:14.498079'),(13,'module','0001_initial','2017-02-09 02:51:14.534961'),(14,'sessions','0001_initial','2017-02-09 02:51:14.617675'),(15,'module','0002_auto_20170209_1101','2017-02-09 03:01:46.876714'),(16,'action','0001_initial','2017-02-09 08:29:17.532225'),(17,'role','0001_initial','2017-02-09 08:29:17.848307'),(18,'nodes_template','0001_initial','2017-02-09 08:29:17.924126'),(19,'game','0001_initial','2017-02-09 08:29:18.186885'),(20,'node','0001_initial','2017-02-09 08:29:18.645825'),(21,'users_group','0001_initial','2017-02-09 08:29:18.684009'),(22,'custom_user','0001_initial','2017-02-09 08:29:19.007841'),(23,'custom_user','0002_auto_20170209_1628','2017-02-09 08:29:19.576654'),(24,'games_template','0001_initial','2017-02-09 08:29:19.751546'),(25,'log','0001_initial','2017-02-09 08:29:19.965168'),(26,'users_group','0002_usersgroup_nodes','2017-02-09 08:29:20.134377'),(27,'config','0001_initial','2017-02-22 05:01:37.248178'),(28,'custom_user','0003_auto_20170222_1301','2017-02-22 05:01:37.791605'),(29,'node','0002_auto_20170222_1301','2017-02-22 05:01:38.283179'),(30,'nodes_template','0002_auto_20170222_1301','2017-02-22 05:01:38.604360'),(31,'game','0002_auto_20170222_1301','2017-02-22 05:01:39.193946'),(32,'games_template','0002_auto_20170222_1301','2017-02-22 05:01:39.421188'),(33,'log','0002_auto_20170222_1301','2017-02-22 05:01:39.533408'),(34,'msg','0001_initial','2017-02-22 05:01:39.772327'),(35,'role','0002_auto_20170222_1301','2017-02-22 05:01:39.876981'),(36,'weixin_interface','0001_initial','2017-02-22 05:01:40.134101');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_game`
--

DROP TABLE IF EXISTS `game_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_game` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `workstarttime` datetime(6) NOT NULL,
  `workendtime` datetime(6) NOT NULL,
  `workextratime` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `place` varchar(50) NOT NULL,
  `gamestarttime` datetime(6) NOT NULL,
  `comments` varchar(200) NOT NULL,
  `state` int(11) NOT NULL,
  `nodestemplateid_id` int(11),
  PRIMARY KEY (`id`),
  KEY `g_nodestemplateid_id_c4770543_fk_nodes_template_nodestemplate_id` (`nodestemplateid_id`),
  CONSTRAINT `g_nodestemplateid_id_c4770543_fk_nodes_template_nodestemplate_id` FOREIGN KEY (`nodestemplateid_id`) REFERENCES `nodes_template_nodestemplate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_game`
--

LOCK TABLES `game_game` WRITE;
/*!40000 ALTER TABLE `game_game` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games_template_date2gamestemplate`
--

DROP TABLE IF EXISTS `games_template_date2gamestemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games_template_date2gamestemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `gamestemplate_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `games_template_date2gamestemplate_date_2649214d_uniq` (`date`,`gamestemplate_id`),
  KEY `gam_gamestemplate_id_73c10672_fk_games_template_gamestemplate_id` (`gamestemplate_id`),
  CONSTRAINT `gam_gamestemplate_id_73c10672_fk_games_template_gamestemplate_id` FOREIGN KEY (`gamestemplate_id`) REFERENCES `games_template_gamestemplate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games_template_date2gamestemplate`
--

LOCK TABLES `games_template_date2gamestemplate` WRITE;
/*!40000 ALTER TABLE `games_template_date2gamestemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `games_template_date2gamestemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games_template_gamestemplate`
--

DROP TABLE IF EXISTS `games_template_gamestemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games_template_gamestemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `comments` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games_template_gamestemplate`
--

LOCK TABLES `games_template_gamestemplate` WRITE;
/*!40000 ALTER TABLE `games_template_gamestemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `games_template_gamestemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games_template_gamestemplate_gameids`
--

DROP TABLE IF EXISTS `games_template_gamestemplate_gameids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games_template_gamestemplate_gameids` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gamestemplate_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `games_template_gamestemplate_game_gamestemplate_id_153d05c9_uniq` (`gamestemplate_id`,`game_id`),
  KEY `games_template_gamestemplate_ga_game_id_32b1a93f_fk_game_game_id` (`game_id`),
  CONSTRAINT `gam_gamestemplate_id_810415b6_fk_games_template_gamestemplate_id` FOREIGN KEY (`gamestemplate_id`) REFERENCES `games_template_gamestemplate` (`id`),
  CONSTRAINT `games_template_gamestemplate_ga_game_id_32b1a93f_fk_game_game_id` FOREIGN KEY (`game_id`) REFERENCES `game_game` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games_template_gamestemplate_gameids`
--

LOCK TABLES `games_template_gamestemplate_gameids` WRITE;
/*!40000 ALTER TABLE `games_template_gamestemplate_gameids` DISABLE KEYS */;
/*!40000 ALTER TABLE `games_template_gamestemplate_gameids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_log`
--

DROP TABLE IF EXISTS `log_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` datetime(6) NOT NULL,
  `objectid` int(11) NOT NULL,
  `detail` longtext NOT NULL,
  `actionid_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `log_log_actionid_id_be8676ed_fk_action_action_id` (`actionid_id`),
  KEY `log_log_userid_id_57af476e_fk_custom_user_customuser_id` (`userid_id`),
  CONSTRAINT `log_log_actionid_id_be8676ed_fk_action_action_id` FOREIGN KEY (`actionid_id`) REFERENCES `action_action` (`id`),
  CONSTRAINT `log_log_userid_id_57af476e_fk_custom_user_customuser_id` FOREIGN KEY (`userid_id`) REFERENCES `custom_user_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_log`
--

LOCK TABLES `log_log` WRITE;
/*!40000 ALTER TABLE `log_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module_module`
--

DROP TABLE IF EXISTS `module_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cnname` varchar(50) NOT NULL,
  `comments` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `module_module_no_00b08231_uniq` (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module_module`
--

LOCK TABLES `module_module` WRITE;
/*!40000 ALTER TABLE `module_module` DISABLE KEYS */;
/*!40000 ALTER TABLE `module_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msg_msg`
--

DROP TABLE IF EXISTS `msg_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msg_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `createtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msg_msg`
--

LOCK TABLES `msg_msg` WRITE;
/*!40000 ALTER TABLE `msg_msg` DISABLE KEYS */;
/*!40000 ALTER TABLE `msg_msg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msg_msgstate`
--

DROP TABLE IF EXISTS `msg_msgstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msg_msgstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` int(11) NOT NULL,
  `msgid_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `msg_msgstate_msgid_id_b8615a97_fk_msg_msg_id` (`msgid_id`),
  KEY `msg_msgstate_userid_id_7e34eb99_fk_custom_user_customuser_id` (`userid_id`),
  CONSTRAINT `msg_msgstate_msgid_id_b8615a97_fk_msg_msg_id` FOREIGN KEY (`msgid_id`) REFERENCES `msg_msg` (`id`),
  CONSTRAINT `msg_msgstate_userid_id_7e34eb99_fk_custom_user_customuser_id` FOREIGN KEY (`userid_id`) REFERENCES `custom_user_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msg_msgstate`
--

LOCK TABLES `msg_msgstate` WRITE;
/*!40000 ALTER TABLE `msg_msgstate` DISABLE KEYS */;
/*!40000 ALTER TABLE `msg_msgstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msg_msgstructure`
--

DROP TABLE IF EXISTS `msg_msgstructure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msg_msgstructure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `no` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msg_msgstructure`
--

LOCK TABLES `msg_msgstructure` WRITE;
/*!40000 ALTER TABLE `msg_msgstructure` DISABLE KEYS */;
/*!40000 ALTER TABLE `msg_msgstructure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `node_node`
--

DROP TABLE IF EXISTS `node_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `node_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type` int(11) NOT NULL,
  `deadline` datetime(6) DEFAULT NULL,
  `notifytime` int(11) NOT NULL,
  `comments` varchar(200) NOT NULL,
  `state` int(11) NOT NULL,
  `gameid_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `node_node_gameid_id_2a19a729_fk_game_game_id` (`gameid_id`),
  CONSTRAINT `node_node_gameid_id_2a19a729_fk_game_game_id` FOREIGN KEY (`gameid_id`) REFERENCES `game_game` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `node_node`
--

LOCK TABLES `node_node` WRITE;
/*!40000 ALTER TABLE `node_node` DISABLE KEYS */;
/*!40000 ALTER TABLE `node_node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `node_noderelationship`
--

DROP TABLE IF EXISTS `node_noderelationship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `node_noderelationship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nodeid_id` int(11) NOT NULL,
  `parentnodeid_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `node_noderelationship_nodeid_id_36884625_fk_node_node_id` (`nodeid_id`),
  KEY `node_noderelationship_parentnodeid_id_fef48f5a_fk_node_node_id` (`parentnodeid_id`),
  CONSTRAINT `node_noderelationship_nodeid_id_36884625_fk_node_node_id` FOREIGN KEY (`nodeid_id`) REFERENCES `node_node` (`id`),
  CONSTRAINT `node_noderelationship_parentnodeid_id_fef48f5a_fk_node_node_id` FOREIGN KEY (`parentnodeid_id`) REFERENCES `node_node` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `node_noderelationship`
--

LOCK TABLES `node_noderelationship` WRITE;
/*!40000 ALTER TABLE `node_noderelationship` DISABLE KEYS */;
/*!40000 ALTER TABLE `node_noderelationship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `node_nodesline`
--

DROP TABLE IF EXISTS `node_nodesline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `node_nodesline` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` int(11) NOT NULL,
  `nextnodeid_id` int(11) NOT NULL,
  `prevnodeid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `node_nodesline_nextnodeid_id_3f7001dc_fk_node_node_id` (`nextnodeid_id`),
  KEY `node_nodesline_prevnodeid_id_5fa0e37d_fk_node_node_id` (`prevnodeid_id`),
  CONSTRAINT `node_nodesline_nextnodeid_id_3f7001dc_fk_node_node_id` FOREIGN KEY (`nextnodeid_id`) REFERENCES `node_node` (`id`),
  CONSTRAINT `node_nodesline_prevnodeid_id_5fa0e37d_fk_node_node_id` FOREIGN KEY (`prevnodeid_id`) REFERENCES `node_node` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `node_nodesline`
--

LOCK TABLES `node_nodesline` WRITE;
/*!40000 ALTER TABLE `node_nodesline` DISABLE KEYS */;
/*!40000 ALTER TABLE `node_nodesline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodes_template_nodestemplate`
--

DROP TABLE IF EXISTS `nodes_template_nodestemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nodes_template_nodestemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `comments` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodes_template_nodestemplate`
--

LOCK TABLES `nodes_template_nodestemplate` WRITE;
/*!40000 ALTER TABLE `nodes_template_nodestemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `nodes_template_nodestemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodes_template_nodestemplate_nodeids`
--

DROP TABLE IF EXISTS `nodes_template_nodestemplate_nodeids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nodes_template_nodestemplate_nodeids` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nodestemplate_id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nodes_template_nodestemplate_node_nodestemplate_id_cbf9b217_uniq` (`nodestemplate_id`,`node_id`),
  KEY `nodes_template_nodestemplate_no_node_id_dd2e4691_fk_node_node_id` (`node_id`),
  CONSTRAINT `nod_nodestemplate_id_f227da54_fk_nodes_template_nodestemplate_id` FOREIGN KEY (`nodestemplate_id`) REFERENCES `nodes_template_nodestemplate` (`id`),
  CONSTRAINT `nodes_template_nodestemplate_no_node_id_dd2e4691_fk_node_node_id` FOREIGN KEY (`node_id`) REFERENCES `node_node` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodes_template_nodestemplate_nodeids`
--

LOCK TABLES `nodes_template_nodestemplate_nodeids` WRITE;
/*!40000 ALTER TABLE `nodes_template_nodestemplate_nodeids` DISABLE KEYS */;
/*!40000 ALTER TABLE `nodes_template_nodestemplate_nodeids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_role`
--

DROP TABLE IF EXISTS `role_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `cnname` varchar(50) DEFAULT NULL,
  `comments` varchar(200) NOT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `cnname` (`cnname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_role`
--

LOCK TABLES `role_role` WRITE;
/*!40000 ALTER TABLE `role_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_role_actions`
--

DROP TABLE IF EXISTS `role_role_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_role_actions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `action_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_role_actions_role_id_fe08c360_uniq` (`role_id`,`action_id`),
  KEY `role_role_actions_action_id_88b215e8_fk_action_action_id` (`action_id`),
  CONSTRAINT `role_role_actions_action_id_88b215e8_fk_action_action_id` FOREIGN KEY (`action_id`) REFERENCES `action_action` (`id`),
  CONSTRAINT `role_role_actions_role_id_9b83271c_fk_role_role_id` FOREIGN KEY (`role_id`) REFERENCES `role_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_role_actions`
--

LOCK TABLES `role_role_actions` WRITE;
/*!40000 ALTER TABLE `role_role_actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_role_actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_group_usersgroup`
--

DROP TABLE IF EXISTS `users_group_usersgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_group_usersgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `comments` varchar(200) NOT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_group_usersgroup`
--

LOCK TABLES `users_group_usersgroup` WRITE;
/*!40000 ALTER TABLE `users_group_usersgroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_group_usersgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_group_usersgroup_nodes`
--

DROP TABLE IF EXISTS `users_group_usersgroup_nodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_group_usersgroup_nodes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usersgroup_id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_group_usersgroup_nodes_usersgroup_id_d4627e3e_uniq` (`usersgroup_id`,`node_id`),
  KEY `users_group_usersgroup_nodes_node_id_808192c9_fk_node_node_id` (`node_id`),
  CONSTRAINT `users_group__usersgroup_id_4730fd76_fk_users_group_usersgroup_id` FOREIGN KEY (`usersgroup_id`) REFERENCES `users_group_usersgroup` (`id`),
  CONSTRAINT `users_group_usersgroup_nodes_node_id_808192c9_fk_node_node_id` FOREIGN KEY (`node_id`) REFERENCES `node_node` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_group_usersgroup_nodes`
--

LOCK TABLES `users_group_usersgroup_nodes` WRITE;
/*!40000 ALTER TABLE `users_group_usersgroup_nodes` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_group_usersgroup_nodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weixin_interface_weixinconfig`
--

DROP TABLE IF EXISTS `weixin_interface_weixinconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weixin_interface_weixinconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weixin_interface_weixinconfig`
--

LOCK TABLES `weixin_interface_weixinconfig` WRITE;
/*!40000 ALTER TABLE `weixin_interface_weixinconfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `weixin_interface_weixinconfig` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-22 13:05:17
