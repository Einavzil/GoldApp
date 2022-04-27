-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema goldapp
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema goldapp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `goldapp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `goldapp` ;

-- -----------------------------------------------------
-- Table `goldapp`.`interest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`interest` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`interest` (
  `interest_id` INT NOT NULL AUTO_INCREMENT,
  `interest` VARCHAR(90) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  PRIMARY KEY (`interest_id`),
  UNIQUE INDEX `interest_UNIQUE` (`interest` ASC) VISIBLE,
  UNIQUE INDEX `interest_id_UNIQUE` (`interest_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`event` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`event` (
  `event_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(90) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `address_line` VARCHAR(75) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `city` VARCHAR(70) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `zipcode` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `country` VARCHAR(55) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `information` MEDIUMTEXT CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `interest_interest_id` INT NOT NULL,
  PRIMARY KEY (`event_id`),
  INDEX `fk_event_interest1_idx` (`interest_interest_id` ASC) VISIBLE,
  CONSTRAINT `fk_event_interest1`
    FOREIGN KEY (`interest_interest_id`)
    REFERENCES `goldapp`.`interest` (`interest_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`group` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`group` (
  `group_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(90) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `description` MEDIUMTEXT CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  PRIMARY KEY (`group_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`info` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`info` (
  `info_id` INT NOT NULL AUTO_INCREMENT,
  `heading` VARCHAR(70) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL COMMENT 'Name or a heading',
  `phone` INT NOT NULL,
  `type` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `category` ENUM('general', 'mentalHelp') CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL COMMENT 'Only 2 types (mental health or just helpful such as volunteers information etc.)',
  `description` MEDIUMTEXT CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  PRIMARY KEY (`info_id`),
  UNIQUE INDEX `info_id_UNIQUE` (`info_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`location` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`location` (
  `location_id` INT NOT NULL AUTO_INCREMENT,
  `place` VARCHAR(100) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  PRIMARY KEY (`location_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`location_has_event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`location_has_event` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`location_has_event` (
  `location_location_id` INT NOT NULL,
  `event_event_id` INT NOT NULL,
  PRIMARY KEY (`location_location_id`, `event_event_id`),
  INDEX `fk_location_has_event_event1_idx` (`event_event_id` ASC) VISIBLE,
  INDEX `fk_location_has_event_location1_idx` (`location_location_id` ASC) VISIBLE,
  CONSTRAINT `fk_location_has_event_event1`
    FOREIGN KEY (`event_event_id`)
    REFERENCES `goldapp`.`event` (`event_id`),
  CONSTRAINT `fk_location_has_event_location1`
    FOREIGN KEY (`location_location_id`)
    REFERENCES `goldapp`.`location` (`location_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`location_has_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`location_has_info` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`location_has_info` (
  `location_location_id` INT NOT NULL,
  `info_info_id` INT NOT NULL,
  PRIMARY KEY (`location_location_id`, `info_info_id`),
  INDEX `fk_location_has_info_info1_idx` (`info_info_id` ASC) VISIBLE,
  INDEX `fk_location_has_info_location1_idx` (`location_location_id` ASC) VISIBLE,
  CONSTRAINT `fk_location_has_info_info1`
    FOREIGN KEY (`info_info_id`)
    REFERENCES `goldapp`.`info` (`info_id`),
  CONSTRAINT `fk_location_has_info_location1`
    FOREIGN KEY (`location_location_id`)
    REFERENCES `goldapp`.`location` (`location_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`user` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`user` (
  `email` VARCHAR(90) NOT NULL,
  `fname` VARCHAR(30) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NOT NULL,
  `lname` VARCHAR(30) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NULL DEFAULT NULL,
  `username` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NULL,
  `pwd` VARCHAR(90) NOT NULL,
  `phone` INT NULL DEFAULT NULL,
  `facebook_connect` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_esperanto_ci' NULL DEFAULT NULL,
  `location_location_id` INT NOT NULL,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE,
  UNIQUE INDEX `facebook_connect_UNIQUE` (`facebook_connect` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  PRIMARY KEY (`email`),
  INDEX `fk_user_location1_idx` (`location_location_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_location1`
    FOREIGN KEY (`location_location_id`)
    REFERENCES `goldapp`.`location` (`location_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`user_has_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`user_has_group` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`user_has_group` (
  `group_group_id` INT NOT NULL,
  `user_email` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`group_group_id`, `user_email`),
  INDEX `fk_user_has_group_group1_idx` (`group_group_id` ASC) VISIBLE,
  INDEX `fk_user_has_group_user1_idx` (`user_email` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_group_group1`
    FOREIGN KEY (`group_group_id`)
    REFERENCES `goldapp`.`group` (`group_id`),
  CONSTRAINT `fk_user_has_group_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `goldapp`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


-- -----------------------------------------------------
-- Table `goldapp`.`user_has_interest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `goldapp`.`user_has_interest` ;

CREATE TABLE IF NOT EXISTS `goldapp`.`user_has_interest` (
  `interest_interest_id` INT NOT NULL,
  `user_email` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`interest_interest_id`, `user_email`),
  INDEX `fk_user_has_interest_interest1_idx` (`interest_interest_id` ASC) VISIBLE,
  INDEX `fk_user_has_interest_user1_idx1` (`user_email` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_interest_interest1`
    FOREIGN KEY (`interest_interest_id`)
    REFERENCES `goldapp`.`interest` (`interest_id`),
  CONSTRAINT `fk_user_has_interest_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `goldapp`.`user` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_esperanto_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
