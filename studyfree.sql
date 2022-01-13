/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80027
Source Host           : localhost:3306
Source Database       : studyfree

Target Server Type    : MYSQL
Target Server Version : 80027
File Encoding         : 65001

Date: 2022-01-13 19:45:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add user', '6', 'add_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can change user', '6', 'change_user');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete user', '6', 'delete_user');
INSERT INTO `auth_permission` VALUES ('24', 'Can view user', '6', 'view_user');
INSERT INTO `auth_permission` VALUES ('25', 'Can add celebrity quotes', '7', 'add_celebrityquotes');
INSERT INTO `auth_permission` VALUES ('26', 'Can change celebrity quotes', '7', 'change_celebrityquotes');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete celebrity quotes', '7', 'delete_celebrityquotes');
INSERT INTO `auth_permission` VALUES ('28', 'Can view celebrity quotes', '7', 'view_celebrityquotes');
INSERT INTO `auth_permission` VALUES ('29', 'Can add tags', '8', 'add_tags');
INSERT INTO `auth_permission` VALUES ('30', 'Can change tags', '8', 'change_tags');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete tags', '8', 'delete_tags');
INSERT INTO `auth_permission` VALUES ('32', 'Can view tags', '8', 'view_tags');
INSERT INTO `auth_permission` VALUES ('33', 'Can add article content', '9', 'add_articlecontent');
INSERT INTO `auth_permission` VALUES ('34', 'Can change article content', '9', 'change_articlecontent');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete article content', '9', 'delete_articlecontent');
INSERT INTO `auth_permission` VALUES ('36', 'Can view article content', '9', 'view_articlecontent');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_study_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_study_user_id` FOREIGN KEY (`user_id`) REFERENCES `study_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('7', 'Common', 'celebrityquotes');
INSERT INTO `django_content_type` VALUES ('6', 'Common', 'user');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'FrontEnd', 'articlecontent');
INSERT INTO `django_content_type` VALUES ('8', 'FrontEnd', 'tags');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2022-01-07 09:19:04.318208');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2022-01-07 09:19:04.416964');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2022-01-07 09:19:04.686694');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2022-01-07 09:19:04.735605');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2022-01-07 09:19:04.742586');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2022-01-07 09:19:04.749568');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2022-01-07 09:19:04.756549');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2022-01-07 09:19:04.759541');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2022-01-07 09:19:04.766522');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2022-01-07 09:19:04.773503');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2022-01-07 09:19:04.780485');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0010_alter_group_name_max_length', '2022-01-07 09:19:04.794449');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0011_update_proxy_permissions', '2022-01-07 09:19:04.802465');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0012_alter_user_first_name_max_length', '2022-01-07 09:19:04.809446');
INSERT INTO `django_migrations` VALUES ('15', 'Common', '0001_initial', '2022-01-07 09:19:05.091161');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0001_initial', '2022-01-07 09:19:05.303800');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0002_logentry_remove_auto_add', '2022-01-07 09:19:05.315768');
INSERT INTO `django_migrations` VALUES ('18', 'admin', '0003_logentry_add_action_flag_choices', '2022-01-07 09:19:05.322752');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2022-01-07 09:19:05.359653');
INSERT INTO `django_migrations` VALUES ('20', 'Common', '0002_celebrityquotes', '2022-01-10 07:15:55.048956');
INSERT INTO `django_migrations` VALUES ('21', 'FrontEnd', '0001_initial', '2022-01-11 04:53:22.391935');
INSERT INTO `django_migrations` VALUES ('22', 'FrontEnd', '0002_alter_tags_tag_id', '2022-01-11 04:53:22.397980');
INSERT INTO `django_migrations` VALUES ('23', 'FrontEnd', '0003_articlecontent', '2022-01-13 02:52:03.558768');
INSERT INTO `django_migrations` VALUES ('24', 'FrontEnd', '0004_alter_articlecontent_filepath', '2022-01-13 03:12:34.212729');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0c6zb7pf0bc6zxgro2ra3g7ryoim0twd', '.eJxVUe9P2zAQ_V8itZ_AcX45caUIDdgYKzBUMSQmpOpin2O3iZMlDu028b_jQj9sknX23Xv37Hv-G6xhcno9jTisjQwWQRSc_FurQGzRHgC5AVt3RHTWDaYiBwo5oiO57SQ250fufwIaRu27E8XyQiismMpzWRVxFmMuUpZGEacSExVnosjTPKKp4AVKroDRnMssoiBUxb3oQc797jFYRCeBGddNVxsbLNww4Qf4PoDHBoTmDlpPDJ6njEvxPDHOqJeAFwOuGzygnevHRRi6EaPTtiXCksrYmlh0odOhkeHq9IIkHIqI0RQ5xpIVFVDMEkwFIHBIE3k2mG35WFlR7K5XqD4t97v5YKbyoD5LYBYrv0xbk91eaPDetT5XpkG_xdRPnrwffKiEZAxSiDKy6es56m1583R5efVw_-f7N97_vMMHz7pvr3qW3xbp8ovefH668aVfetntf9iv4yyR_u6xKee9keV1W6_AP6akR-fshyEb43_Rgg1e3wDt0aNW:1n7F1u:tWSEAnKZv41A_GpT4SWHIEA8hhlzddaXtKDdY0c61c8', '2022-01-25 11:09:30.644724');
INSERT INTO `django_session` VALUES ('e6sahijys29j5hfvy6751fr91qovja77', '.eJxVUe9P2zAQ_V8itZ_AcX45caUIDdgYKzBUMSQmpOpin2O3iZMlDu028b_jQj9sknX23Xv37Hv-G6xhcno9jTisjQwWQRSc_FurQGzRHgC5AVt3RHTWDaYiBwo5oiO57SQ250fufwIaRu27E8XyQiismMpzWRVxFmMuUpZGEacSExVnosjTPKKp4AVKroDRnMssoiBUxb3oQc797jFYRCeBGddNVxsbLNww4Qf4PoDHBoTmDlpPDJ6njEvxPDHOqJeAFwOuGzygnevHRRi6EaPTtiXCksrYmlh0odOhkeHq9IIkHIqI0RQ5xpIVFVDMEkwFIHBIE3k2mG35WFlR7K5XqD4t97v5YKbyoD5LYBYrv0xbk91eaPDetT5XpkG_xdRPnrwffKiEZAxSiDKy6es56m1583R5efVw_-f7N97_vMMHz7pvr3qW3xbp8ovefH668aVfetntf9iv4yyR_u6xKee9keV1W6_AP6akR-fshyEb43_Rgg1e3wDt0aNW:1n6kfJ:ZPczdusOfMQomPpZmVgOVpxMdt9VMfXPp4heDYNy28E', '2022-01-24 02:44:09.539123');
INSERT INTO `django_session` VALUES ('wtw0aoj6keoz68hl10p1jzaavb0nilah', '.eJxVUe9P2zAQ_V8itZ_AcX45caUIDdgYKzBUMSQmpOpin2O3iZMlDu028b_jQj9sknX23Xv37Hv-G6xhcno9jTisjQwWQRSc_FurQGzRHgC5AVt3RHTWDaYiBwo5oiO57SQ250fufwIaRu27E8XyQiismMpzWRVxFmMuUpZGEacSExVnosjTPKKp4AVKroDRnMssoiBUxb3oQc797jFYRCeBGddNVxsbLNww4Qf4PoDHBoTmDlpPDJ6njEvxPDHOqJeAFwOuGzygnevHRRi6EaPTtiXCksrYmlh0odOhkeHq9IIkHIqI0RQ5xpIVFVDMEkwFIHBIE3k2mG35WFlR7K5XqD4t97v5YKbyoD5LYBYrv0xbk91eaPDetT5XpkG_xdRPnrwffKiEZAxSiDKy6es56m1583R5efVw_-f7N97_vMMHz7pvr3qW3xbp8ovefH668aVfetntf9iv4yyR_u6xKee9keV1W6_AP6akR-fshyEb43_Rgg1e3wDt0aNW:1n7Czc:3u9cy44esO0ewzOAIMZYRSleM-GYtDdcrxL_MvfE3n0', '2022-01-25 08:59:00.942018');

-- ----------------------------
-- Table structure for `study_articlecontent`
-- ----------------------------
DROP TABLE IF EXISTS `study_articlecontent`;
CREATE TABLE `study_articlecontent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` int unsigned NOT NULL,
  `images` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `filePath` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `tag_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `study_articleContent_tag_id_id_9b6029d1_fk_study_tags_id` (`tag_id_id`),
  CONSTRAINT `study_articleContent_tag_id_id_9b6029d1_fk_study_tags_id` FOREIGN KEY (`tag_id_id`) REFERENCES `study_tags` (`id`),
  CONSTRAINT `study_articlecontent_chk_1` CHECK ((`status` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_articlecontent
-- ----------------------------
INSERT INTO `study_articlecontent` VALUES ('1', '1', 'images/python-default.png', 'md/编写测试用例.md', '5');
INSERT INTO `study_articlecontent` VALUES ('2', '1', 'images/python-default.png', null, '6');
INSERT INTO `study_articlecontent` VALUES ('3', '1', 'images/python-default.png', null, '7');

-- ----------------------------
-- Table structure for `study_cq`
-- ----------------------------
DROP TABLE IF EXISTS `study_cq`;
CREATE TABLE `study_cq` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `author` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_cq
-- ----------------------------
INSERT INTO `study_cq` VALUES ('1', '为每个想学习知识的人提供一个少走弯路的平台', null);
INSERT INTO `study_cq` VALUES ('2', '海纳百川，有容乃大；壁立于仞，无欲则刚。', '林则徐');
INSERT INTO `study_cq` VALUES ('3', '休息与工作的关系，正如眼睑与眼睛的关系。', '泰戈尔');

-- ----------------------------
-- Table structure for `study_tags`
-- ----------------------------
DROP TABLE IF EXISTS `study_tags`;
CREATE TABLE `study_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `tag_id` int DEFAULT NULL,
  `tage_type` int unsigned NOT NULL,
  `status` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `study_tags_chk_1` CHECK ((`tage_type` >= 0)),
  CONSTRAINT `study_tags_chk_2` CHECK ((`status` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_tags
-- ----------------------------
INSERT INTO `study_tags` VALUES ('1', 'Python', null, '1', '1');
INSERT INTO `study_tags` VALUES ('2', 'Docker', null, '1', '1');
INSERT INTO `study_tags` VALUES ('3', 'Python基础', '1', '2', '1');
INSERT INTO `study_tags` VALUES ('4', 'Python进阶', '1', '2', '1');
INSERT INTO `study_tags` VALUES ('5', 'list', '3', '3', '1');
INSERT INTO `study_tags` VALUES ('6', 'str', '3', '3', '1');
INSERT INTO `study_tags` VALUES ('7', '目录操作', '4', '3', '1');

-- ----------------------------
-- Table structure for `study_user`
-- ----------------------------
DROP TABLE IF EXISTS `study_user`;
CREATE TABLE `study_user` (
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usertype` int unsigned NOT NULL,
  `realName` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `aviator` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `desc` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `study_user_realName_59693a89` (`realName`),
  CONSTRAINT `study_user_chk_1` CHECK ((`usertype` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_user
-- ----------------------------
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$4xg0fMFTefqOr3vvboVdVs$lu647cbrXNQsCCP2H3h9/2o1cZXLVBIHiqyR642ZRSs=', '2022-01-11 11:09:30.542902', '1', 'jiangnan', '', '', '', '1', '1', '2022-01-07 09:19:38.585700', '1', '1', '姜楠', null, 'https://tse1-mm.cn.bing.net/th/id/R-C.39a81604e9e2d68ba0e53e4caea9a43d?rik=Vbnc8wIRefAKxw&riu=http%3a%2f%2fimg.wxcha.com%2ffile%2f201903%2f20%2fbcd66a4a15.jpg&ehk=LYDDGTPzOJ9pZNeT%2fPmGp67M84KFhjEYL%2fqhKoxUnHs%3d&risl=&pid=ImgRaw&r=0', null);

-- ----------------------------
-- Table structure for `study_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `study_user_groups`;
CREATE TABLE `study_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `study_user_groups_user_id_group_id_195e46be_uniq` (`user_id`,`group_id`),
  KEY `study_user_groups_group_id_0e3055d7_fk_auth_group_id` (`group_id`),
  CONSTRAINT `study_user_groups_group_id_0e3055d7_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `study_user_groups_user_id_3f1cb524_fk_study_user_id` FOREIGN KEY (`user_id`) REFERENCES `study_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `study_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `study_user_user_permissions`;
CREATE TABLE `study_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `study_user_user_permissions_user_id_permission_id_cd7eec3c_uniq` (`user_id`,`permission_id`),
  KEY `study_user_user_perm_permission_id_3b5f4dbc_fk_auth_perm` (`permission_id`),
  CONSTRAINT `study_user_user_perm_permission_id_3b5f4dbc_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `study_user_user_permissions_user_id_b48e818a_fk_study_user_id` FOREIGN KEY (`user_id`) REFERENCES `study_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_user_user_permissions
-- ----------------------------
