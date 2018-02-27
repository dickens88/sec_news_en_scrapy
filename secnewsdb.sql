CREATE TABLE `t_security_en_news_article` (
 `id` bigint(20) NOT NULL AUTO_INCREMENT,
 `title` varchar(100) DEFAULT NULL,
 `content` text,
 `uri` varchar(200) DEFAULT NULL,
 `last_update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
 `src` varchar(200) NOT NULL,
 `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`),
 UNIQUE KEY `idx_sna_t` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=6681 DEFAULT CHARSET=utf8



CREATE TABLE `t_security_en_news_words` (
 `id` bigint(20) NOT NULL AUTO_INCREMENT,
 `title` varchar(100) DEFAULT NULL,
 `key` varchar(200) DEFAULT NULL,
 `val` int(11) DEFAULT NULL,
 `last_update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`),
 UNIQUE KEY `idx_snw_tk` (`title`,`key`),
 KEY `idx_snw_ts` (`last_update_time`)
) ENGINE=InnoDB AUTO_INCREMENT=42641 DEFAULT CHARSET=utf8
