/*
Navicat MySQL Data Transfer

Source Server         : mysql8.0
Source Server Version : 80027
Source Host           : localhost:3306
Source Database       : studyfree

Target Server Type    : MYSQL
Target Server Version : 80027
File Encoding         : 65001

Date: 2022-01-18 16:59:54
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
INSERT INTO `django_session` VALUES ('jjief2tguqil1x51g5rtvpo3gvid04t0', '.eJxVUe9P2zAQ_V8itZ_AcX45caUIDdgYKzBUMSQmpOpin2O3iZMlDu028b_jQj9sknX23Xv37Hv-G6xhcno9jTisjQwWQRSc_FurQGzRHgC5AVt3RHTWDaYiBwo5oiO57SQ250fufwIaRu27E8XyQiismMpzWRVxFmMuUpZGEacSExVnosjTPKKp4AVKroDRnMssoiBUxb3oQc797jFYRCeBGddNVxsbLNww4Qf4PoDHBoTmDlpPDJ6njEvxPDHOqJeAFwOuGzygnevHRRi6EaPTtiXCksrYmlh0odOhkeHq9IIkHIqI0RQ5xpIVFVDMEkwFIHBIE3k2mG35WFlR7K5XqD4t97v5YKbyoD5LYBYrv0xbk91eaPDetT5XpkG_xdRPnrwffKiEZAxSiDKy6es56m1583R5efVw_-f7N97_vMMHz7pvr3qW3xbp8ovefH668aVfetntf9iv4yyR_u6xKee9keV1W6_AP6akR-fshyEb43_Rgg1e3wDt0aNW:1n9hFC:SH4lGE_axOcO8Q57eqEvVGXl0i3_ppeJ_n8wvlCTk2Y', '2022-02-01 13:41:22.957412');

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
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci,
  `time` datetime(6) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `study_notebook_user_id_id_a3be7223_fk_study_user_id` (`user_id_id`),
  CONSTRAINT `study_notebook_user_id_id_a3be7223_fk_study_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `study_user` (`id`),
  CONSTRAINT `study_notebook_chk_1` CHECK ((`status` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

-- ----------------------------
-- Records of study_notebook
-- ----------------------------
INSERT INTO `study_notebook` VALUES ('9', '1', '456', '---\ntitle: 编写测试用例\ndate: 2021-01-20 10:34:59\ntags: Test\n---\n\n## 概述\n\n采用什么方法才能写出比较完善的测试用例呢？\n\n要做好两类事情\n![](/api/static/images/img_notebook_9_1642484507.png)\n\n\n\n- 不断地 搜集需求，整理需求\n- 采用一定的方法，根据整理的需求编写测试用例。\n\n## 搜集、整理需求\n\n### 过程描述\n\n在编写测试用例前，最重要的前提是什么？\n\n就是要尽可能的 `搜集` 完整系统的 `需求、设计` 。\n\n但是注意：即使开发人员给的需求、设计文档看起来已经比较全面，规范了，测试人员仍然要自己 `整理、分类、组合` 需求。\n\n因为 实践证明，开发人员 **不可能** 给出 `详细到、格式规范到 可以直接对应 产生测试用例` 的 需求、设计文档。\n\n里面肯定 有遗漏、或者细节不清楚 的地方，甚至会有 矛盾、错误\n\n所以我们在 `需求整理` 过程中：\n\n- 寻找是否有遗漏的 需求点（测试点）![](/api/static/images/img_notebook_9_1642484525.png)\n\n\n  有不少隐含 需求点（测试点） ，是需求文档中没有提到的，需要你自己找出来\n\n  或者 有的功能点 文档 只是一带而过，细节没有描述清楚，必须要搞清楚\n\n- 发现需求设计 有 矛盾错误的地方，及时和 产品组、开发人员 沟通\n\n- 不断的将需求进行 合理的 分类、组合， 记录在你自己的测试需求文档中\n\n  需求文档中，功能的分类组织的形式，并不一定是最好的，甚至可能是不正确的，测试人员需要根据自己的经验重新组织\n\n  而且，我们需要把前面发现 开发人员给的需求设计文档中 的 遗漏、细节不清楚的地方 在自己的 测试需求文档中记录下来。\n\n知道了这些要点后，具体怎么操作呢？\n\n- 反复看需求文档几遍，先搞懂文章中的各个功能点的含义\n\n- 创建自己的 测试需求文档，重新整理、分类记录功能点\n\n  整理记录过程中，详细的品读需求，思考，有意识的 关注上面说到的注意点\n\n- 上面的过程 从 需求阶段 到 测试阶段不断迭代\n\n  因为产品的整个开发过程中，决定 会 不断的改变，前面的需求设计文档里面的内容未必是有效的。\n\n  所以要根据 搜集到的 改变的信息，不断的重复上面的过程。\n\n  实际上，测试需求文档 和 测试用例 是 直到测试过程中，都应该不断更新的。\n\n最终的 测试需求文档，就是做为 测试用例 的输入材料。\n\n```vue\nimport {createApp} from \'vue\'\nimport App from \'./App.vue\'\nimport router from \'./router\'\nimport store from \'./store\'\n\n// 全局样式\nimport \'./styles/index.less\'\nimport VueParticles from \'vue-particles\'\n\n// makeDown 编辑器\nimport \'github-markdown-css\'\n\n\n// element ui 逐渐库\nimport ElementPlus from \'element-plus\'\n\n// 加载element 逐渐库 样式\nimport \'element-plus/dist/index.css\'\n\ncreateApp(App).use(store).use(ElementPlus).use(router).use(VueParticles).mount(\'#app\')\n\n```\n\n## 编写测试用例\n\n需求整理好以后，采用什么方法才能写出比较完善的测试用例呢？\n\n网上流传的编写测试用例方法有很多，我们总结最重要的就是\n\n- 根据测试需求建立用例分类\n- 边界值法\n- 错误猜测法\n- 因素/场景组合法\n\n### 建立用例分类\n\n很好理解，就是根据前面 整理的测试需求 对应写出测试功能点分类\n\n### 边界值\n\n边界值往往是系统处理最容易出问题的地方。\n\n边界值法 就是 对测试输入的边界内、边界上、边界外 的三种取值 都做覆盖的测试。\n\n比如用户注册功能，要求用户名的长度为 6-20 个字符, 那么就应该对 用户名字符串长度为 0，3，5，6，7，15，19，20，21，1000 等这些取值都进行覆盖，比较稳妥。\n\n需求设计文档，往往对边界情况没有明确写出来，需要测试人员 和 开发 人工沟通确定后，写出测试需求。\n\n### 错误猜测\n\n其实上面讲的边界值法，就是典型的错误猜测。\n\n还有其他的错误猜测\n\n比如：\n\n测试管理员登录功能， 那么系统中是否 有老师、学生 账号，对管理员登录是否有影响呢？\n\n再比如，在 `老师` 登录界面，却输入 `学生` 账号、密码，系统是否能正确提示呢？\n\n不好说，所以这些也可以在写测试用例时，作为考虑因素。可以标记为测试优先级 较低。\n\n有些场景的错误猜测类型的测试用例，是通用的，可以作为经验 记录下来。\n\n比如，用户注册功能，测试 用户名中是否包含中文、标点符号等。\n\n再比如，用户登录功能，测试 用户不从登录界面登录，直接访问登录成功后的页面。\n\n错误猜测，虽说 是凭 经验 和 直觉，实际上 和 你对系统实现内部机制 了解程度 紧密相关的。\n\n你越了解系统的实现细节和原理，越了解相关基础知识，错误猜测的 直觉 越准确，写的测试用例越有针对性。\n\n比如这个功能说明\n\n```\n创建题目时，可以为题目添加解题视频，解题视频格式只支持 mp4 格式的视频。\n```\n\n一般测试人员可以想到，编写测试用例涵盖上传 mp4 格式的视频 和 其他格式的视频。\n\n但是如果你了解多媒体的知识，就会知道 mp4 只是一个多媒体容器格式（container）。里面的视频 还有多种压缩格式，比如 MPEG-H Part 2 (H.265/HEVC), MPEG-4 Part 10 (H.264/AVC) 和 MPEG-4 Part 2。\n\n那么这些格式的视频是不是也应该都测试一下呢，测试用例优先级有多高呢？\n\n如果 你了解 产品 的实现原理， 就可以做出准确的判断\n\n如果你没有这方面的基础知识，是无论如何想不到这样的 测试用例的，并且不能做出比较准确的判断的。\n\n所以前面课程，我们说，测试人员也要尽可能的了解 系统的内部实现，并且学习相关基础知识。\n\n### 因素/场景组合\n\n因素/场景组合法，类似网上流传的 判定表 方法。\n\n测试用例 本质上 就是 描述：\n\n在 `某种场景条件` 下，对系统的进行怎样的操作（输入），系统应该有什么的反映（输出）。\n\n所谓 某种场景 ，就是系统处于什么样 的 `环境` ，包括 `外部环境` 和 `内部数据环境` 。\n\n- 外部环境\n\n  比如：硬件（CPU/内存/硬盘/网卡 等）配置、网络带宽配置、温度、操作系统、数据库、缓存软件系统 等\n\n  外部环境通常是对 `性能测试` 影响比较大。\n\n- 内部数据环境\n\n  指 软件系统的内部数据设置。\n\n  比如： 数据库关键记录 数量的设置 对 `性能测试` 影响 至关重要。\n\n  而对 `功能测试` 来说，一个功能，其相关业务数据状态，对行为的影响是 决定性的。\n\n  比如：\n\n  要测试 老师创建作业任务 要下发给学生 这个功能 ，那么 `老师所在班级的有没有学生` 这个数据状态 就是 影响 行为的 重要场景/因素。\n\n  再比如：\n\n  要测试 老师 编辑、删除作业的功能， 那么 该作业是否已经发布给学生就是 影响 行为的 重要场景/因素。\n\n所以 测试用例的完善性，很大情况下，取决于你能找到多少 产品在使用过程中的 ，导致系统行为的 `场景` 或者 `因素` 。\n\n因素组合法，就是 尽可能多的找到 这些 因素，记录下来，在写测试用例的时候 进行 `组合` 。\n', '2022-01-18 13:42:32.528181', '1');

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
INSERT INTO `study_user` VALUES ('pbkdf2_sha256$260000$4xg0fMFTefqOr3vvboVdVs$lu647cbrXNQsCCP2H3h9/2o1cZXLVBIHiqyR642ZRSs=', '2022-01-18 13:41:22.938865', '1', 'jiangnan', '', '', '', '1', '1', '2022-01-07 09:19:38.585700', '1', '1', '姜楠', 'https://tse1-mm.cn.bing.net/th/id/R-C.39a81604e9e2d68ba0e53e4caea9a43d?rik=Vbnc8wIRefAKxw&riu=http%3a%2f%2fimg.wxcha.com%2ffile%2f201903%2f20%2fbcd66a4a15.jpg&ehk=LYDDGTPzOJ9pZNeT%2fPmGp67M84KFhjEYL%2fqhKoxUnHs%3d&risl=&pid=ImgRaw&r=0', null);
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
