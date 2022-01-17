/*
Navicat MySQL Data Transfer

Source Server         : mysql8.0
Source Server Version : 80027
Source Host           : localhost:3306
Source Database       : studyfree

Target Server Type    : MYSQL
Target Server Version : 80027
File Encoding         : 65001

Date: 2022-01-17 16:50:57
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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

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
INSERT INTO `auth_permission` VALUES ('37', 'Can add pay config', '10', 'add_payconfig');
INSERT INTO `auth_permission` VALUES ('38', 'Can change pay config', '10', 'change_payconfig');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete pay config', '10', 'delete_payconfig');
INSERT INTO `auth_permission` VALUES ('40', 'Can view pay config', '10', 'view_payconfig');
INSERT INTO `auth_permission` VALUES ('41', 'Can add phone code', '11', 'add_phonecode');
INSERT INTO `auth_permission` VALUES ('42', 'Can change phone code', '11', 'change_phonecode');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete phone code', '11', 'delete_phonecode');
INSERT INTO `auth_permission` VALUES ('44', 'Can view phone code', '11', 'view_phonecode');
INSERT INTO `auth_permission` VALUES ('45', 'Can add email code', '12', 'add_emailcode');
INSERT INTO `auth_permission` VALUES ('46', 'Can change email code', '12', 'change_emailcode');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete email code', '12', 'delete_emailcode');
INSERT INTO `auth_permission` VALUES ('48', 'Can view email code', '12', 'view_emailcode');
INSERT INTO `auth_permission` VALUES ('49', 'Can add note book', '13', 'add_notebook');
INSERT INTO `auth_permission` VALUES ('50', 'Can change note book', '13', 'change_notebook');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete note book', '13', 'delete_notebook');
INSERT INTO `auth_permission` VALUES ('52', 'Can view note book', '13', 'view_notebook');

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('7', 'Common', 'celebrityquotes');
INSERT INTO `django_content_type` VALUES ('12', 'Common', 'emailcode');
INSERT INTO `django_content_type` VALUES ('11', 'Common', 'phonecode');
INSERT INTO `django_content_type` VALUES ('6', 'Common', 'user');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'FrontEnd', 'articlecontent');
INSERT INTO `django_content_type` VALUES ('13', 'FrontEnd', 'notebook');
INSERT INTO `django_content_type` VALUES ('8', 'FrontEnd', 'tags');
INSERT INTO `django_content_type` VALUES ('10', 'Pay', 'payconfig');
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

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
INSERT INTO `django_migrations` VALUES ('25', 'Pay', '0001_initial', '2022-01-14 04:59:18.431532');
INSERT INTO `django_migrations` VALUES ('26', 'Pay', '0002_auto_20220114_1639', '2022-01-14 08:39:27.815852');
INSERT INTO `django_migrations` VALUES ('27', 'Common', '0003_phonecode', '2022-01-15 00:28:00.731550');
INSERT INTO `django_migrations` VALUES ('28', 'Pay', '0003_alter_payconfig_deadline', '2022-01-15 00:28:00.848296');
INSERT INTO `django_migrations` VALUES ('29', 'Common', '0004_alter_phonecode_status', '2022-01-15 00:29:04.242596');
INSERT INTO `django_migrations` VALUES ('30', 'Common', '0005_auto_20220115_1614', '2022-01-15 16:15:04.984521');
INSERT INTO `django_migrations` VALUES ('31', 'Common', '0006_auto_20220115_1637', '2022-01-15 16:37:36.164763');
INSERT INTO `django_migrations` VALUES ('32', 'FrontEnd', '0005_notebook', '2022-01-17 15:21:54.920745');
INSERT INTO `django_migrations` VALUES ('33', 'FrontEnd', '0006_alter_notebook_content', '2022-01-17 15:39:49.495747');

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
INSERT INTO `django_session` VALUES ('3f3fcxjzm9kkt5md95s2kwq4agh5n0il', 'e30:1n8Fpf:kYWQ7OyDNgsTnD6V2AN-_wRTy-KYNUtazn0znuaWrwU', '2022-01-28 06:13:03.186106');
INSERT INTO `django_session` VALUES ('qnn9b91jm704d1p5nhxh6mgwau0efkj0', '.eJxVUe9P2zAQ_V8itZ_AcX45caUIDdgYKzBUMSQmpOpin2O3iZMlDu028b_jQj9sknX23Xv37Hv-G6xhcno9jTisjQwWQRSc_FurQGzRHgC5AVt3RHTWDaYiBwo5oiO57SQ250fufwIaRu27E8XyQiismMpzWRVxFmMuUpZGEacSExVnosjTPKKp4AVKroDRnMssoiBUxb3oQc797jFYRCeBGddNVxsbLNww4Qf4PoDHBoTmDlpPDJ6njEvxPDHOqJeAFwOuGzygnevHRRi6EaPTtiXCksrYmlh0odOhkeHq9IIkHIqI0RQ5xpIVFVDMEkwFIHBIE3k2mG35WFlR7K5XqD4t97v5YKbyoD5LYBYrv0xbk91eaPDetT5XpkG_xdRPnrwffKiEZAxSiDKy6es56m1583R5efVw_-f7N97_vMMHz7pvr3qW3xbp8ovefH668aVfetntf9iv4yyR_u6xKee9keV1W6_AP6akR-fshyEb43_Rgg1e3wDt0aNW:1n9Le4:aA17DnMt-qB3VB0iP1OrhX1JxnYcjJBrEXYyIGFMwnY', '2022-01-31 14:37:36.293498');

-- ----------------------------
-- Table structure for `pay_config`
-- ----------------------------
DROP TABLE IF EXISTS `pay_config`;
CREATE TABLE `pay_config` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `coins` int DEFAULT NULL,
  `exp` int DEFAULT NULL,
  `lv` int DEFAULT NULL,
  `deadline` datetime(6) NOT NULL,
  `user_id_id` bigint NOT NULL,
  `qd` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pay_config_user_id_id_3a9ecdb7_fk_study_user_id` (`user_id_id`),
  CONSTRAINT `pay_config_user_id_id_3a9ecdb7_fk_study_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `study_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of pay_config
-- ----------------------------
INSERT INTO `pay_config` VALUES ('1', '99999949', '14845', '4', '2022-01-21 13:01:16.000000', '1', '1');
INSERT INTO `pay_config` VALUES ('3', '0', '0', '0', '2022-01-15 00:30:11.836636', '3', '0');
INSERT INTO `pay_config` VALUES ('4', '50', '500', '1', '2022-01-15 00:34:42.204227', '4', '1');
INSERT INTO `pay_config` VALUES ('5', '0', '0', '0', '2022-01-15 16:41:37.649082', '5', '0');
INSERT INTO `pay_config` VALUES ('6', '50', '500', '1', '2022-01-15 17:25:52.065186', '6', '1');
INSERT INTO `pay_config` VALUES ('7', '0', '0', '0', '2022-01-15 19:25:44.850759', '7', '0');
INSERT INTO `pay_config` VALUES ('8', '0', '0', '0', '2022-01-15 21:48:21.203757', '8', '0');

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
-- Table structure for `study_email_code`
-- ----------------------------
DROP TABLE IF EXISTS `study_email_code`;
CREATE TABLE `study_email_code` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `status` int unsigned NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `study_email_code_chk_1` CHECK ((`status` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_email_code
-- ----------------------------
INSERT INTO `study_email_code` VALUES ('1', 'M2ZWGZ', '2', '896333574@qq.com', '2022-01-15 21:48:20.468639');

-- ----------------------------
-- Table structure for `study_notebook`
-- ----------------------------
DROP TABLE IF EXISTS `study_notebook`;
CREATE TABLE `study_notebook` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` int unsigned NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `content` longtext COLLATE utf8mb4_unicode_520_ci,
  `time` datetime(6) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `study_notebook_user_id_id_a3be7223_fk_study_user_id` (`user_id_id`),
  CONSTRAINT `study_notebook_user_id_id_a3be7223_fk_study_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `study_user` (`id`),
  CONSTRAINT `study_notebook_chk_1` CHECK ((`status` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_notebook
-- ----------------------------
INSERT INTO `study_notebook` VALUES ('1', '1', '默认标题', '1', '2022-01-17 15:33:52.080650', '1');
INSERT INTO `study_notebook` VALUES ('2', '1', '默认标题', '2', '2022-01-17 15:34:04.958010', '1');
INSERT INTO `study_notebook` VALUES ('3', '1', '默认标题', '3', '2022-01-17 15:34:24.242875', '1');
INSERT INTO `study_notebook` VALUES ('4', '1', '默认标题', '请在此输入内容，支持markdown语法', '2022-01-17 15:40:21.302742', '1');

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
  `email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usertype` int unsigned NOT NULL,
  `realName` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `aviator` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `desc` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `study_user_realName_59693a89` (`realName`),
  CONSTRAINT `study_user_chk_1` CHECK ((`usertype` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_user
-- ----------------------------
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$4xg0fMFTefqOr3vvboVdVs$lu647cbrXNQsCCP2H3h9/2o1cZXLVBIHiqyR642ZRSs=', '2022-01-17 14:37:36.273004', '1', 'jiangnan', '', '', '', '1', '1', '2022-01-07 09:19:38.585700', '1', '1', '姜楠', 'https://tse1-mm.cn.bing.net/th/id/R-C.39a81604e9e2d68ba0e53e4caea9a43d?rik=Vbnc8wIRefAKxw&riu=http%3a%2f%2fimg.wxcha.com%2ffile%2f201903%2f20%2fbcd66a4a15.jpg&ehk=LYDDGTPzOJ9pZNeT%2fPmGp67M84KFhjEYL%2fqhKoxUnHs%3d&risl=&pid=ImgRaw&r=0', null);
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$QSlfBsdK117kakMSLBnnVB$ZpY7ckayrYsm5JcZFNNLIfZqFCovwu3KUXK7AEJayQw=', '2022-01-15 00:34:52.490355', '0', 'jncss', '', '', '', '0', '1', '2022-01-15 00:30:11.559788', '3', '1000', '', null, '无评价');
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$Osk4XCKVnxM4ylyB5HTnwE$IR+XenJSlvDq9pem6PZiNcgJS/iV0yp2mVzZx/iLtyo=', '2022-01-15 00:35:24.336949', '0', 'jn11', '', '', '', '0', '1', '2022-01-15 00:34:42.048282', '4', '1000', '', null, '无评价');
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$rbn7NoRJqb1wgxKqH1XhTd$Cl9TpJ2NtpD3FX9Yikozdu+ilBJKtwegCpO4itKMQBQ=', null, '0', 'cs11', '', '', '896333574@qq.com', '0', '1', '2022-01-15 16:41:37.327930', '5', '1000', '', null, '无评价');
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$taepkAi1lsdqNaRxmBaBuq$eJsEIIcNo6/i1S18tud2fvmS5siCpNgTQWMslvz6ZR8=', '2022-01-15 17:25:52.821804', '0', 'cs22', '', '', '896333574@qq.com', '0', '1', '2022-01-15 17:25:51.629864', '6', '1000', '', null, '无评价');
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$ZrFmb72x2TI0zpnXiiC0cs$zeJ7T1zd3NgPqkhWteqPitfPbPv9PM21qu6daTcuJqY=', '2022-01-15 19:25:45.559804', '0', 'cs33', '', '', '896333574@qq.com', '0', '1', '2022-01-15 19:25:44.674948', '7', '1000', '', null, '无评价');
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$0APOmnpeflAed4SsnROapt$b7jxhWEs7aPN4v6rHn9+g5D2QyXsVfPVnWb4RynpOcU=', '2022-01-15 21:54:34.332687', '0', 'cs44', '', '', '896333574@qq.com', '0', '1', '2022-01-15 21:48:20.901004', '8', '1000', '', null, '无评价');

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
