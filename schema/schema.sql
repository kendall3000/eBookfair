-- MySQL Script generated by MySQL Workbench
-- Wed Nov  8 20:38:35 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`CUSTOMER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CUSTOMER` (
  `cus_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cus_lname` VARCHAR(45) NOT NULL,
  `cus_fname` VARCHAR(45) NOT NULL,
  `cus_initial` VARCHAR(45) NULL,
  `cus_email` VARCHAR(128) NOT NULL,
  `cus_phone` VARCHAR(12) NOT NULL,
  `cus_phone_country` VARCHAR(3) NOT NULL,
  PRIMARY KEY (`cus_id`),
  UNIQUE INDEX `cus_code_UNIQUE` (`cus_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`INVOICE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`INVOICE` (
  `inv_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cus_id` INT UNSIGNED NOT NULL,
  `inv_date` DATETIME NOT NULL,
  `inv_address_line1` VARCHAR(128) NOT NULL,
  `inv_address_line2` VARCHAR(128) NULL,
  `inv_address_city` VARCHAR(128) NOT NULL,
  `inv_address_region` VARCHAR(128) NOT NULL,
  `inv_address_country` VARCHAR(128) NOT NULL,
  `inv_address_postalcode` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`inv_id`),
  UNIQUE INDEX `inv_number_UNIQUE` (`inv_id` ASC) VISIBLE,
  INDEX `fk_INVOICE_CUSTOMER_idx` (`cus_id` ASC) VISIBLE,
  CONSTRAINT `fk_INVOICE_CUSTOMER`
    FOREIGN KEY (`cus_id`)
    REFERENCES `mydb`.`CUSTOMER` (`cus_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CATEGORY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CATEGORY` (
  `cat_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cat_name` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE INDEX `pc_id_UNIQUE` (`cat_id` ASC) VISIBLE,
  UNIQUE INDEX `cat_name_UNIQUE` (`cat_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PRODUCT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PRODUCT` (
  `prod_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prod_name` VARCHAR(128) NOT NULL,
  `prod_descript` VARCHAR(2048) NOT NULL,
  `prod_price` DECIMAL(8,2) UNSIGNED NOT NULL,
  `prod_stock` INT UNSIGNED NOT NULL,
  `cat_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`prod_id`),
  UNIQUE INDEX `prod_code_UNIQUE` (`prod_id` ASC) VISIBLE,
  INDEX `fk_PRODUCT_CATEGORY1_idx` (`cat_id` ASC) VISIBLE,
  CONSTRAINT `fk_PRODUCT_CATEGORY1`
    FOREIGN KEY (`cat_id`)
    REFERENCES `mydb`.`CATEGORY` (`cat_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DISCOUNT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DISCOUNT` (
  `disc_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `disc_code` VARCHAR(16) NOT NULL,
  `disc_start` DATETIME NOT NULL,
  `disc_end` DATETIME NOT NULL,
  `disc_amount` DECIMAL(2,2) UNSIGNED NOT NULL DEFAULT 0.0,
  PRIMARY KEY (`disc_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`LINE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`LINE` (
  `inv_id` INT UNSIGNED NOT NULL,
  `line_id` INT UNSIGNED NOT NULL,
  `line_quantity` INT UNSIGNED NOT NULL,
  `prod_id` INT UNSIGNED NOT NULL,
  `disc_id` INT UNSIGNED NULL,
  `line_total` DECIMAL(8,2) UNSIGNED NOT NULL COMMENT 'The monetary amount that the items in this line were sold for, after a discount was applied.',
  PRIMARY KEY (`inv_id`, `line_id`),
  UNIQUE INDEX `line_number_UNIQUE` (`line_id` ASC) VISIBLE,
  INDEX `fk_LINE_INVOICE1_idx` (`inv_id` ASC) VISIBLE,
  INDEX `fk_LINE_PRODUCT1_idx` (`prod_id` ASC) VISIBLE,
  INDEX `fk_LINE_DISCOUNT1_idx` (`disc_id` ASC) VISIBLE,
  CONSTRAINT `fk_LINE_INVOICE1`
    FOREIGN KEY (`inv_id`)
    REFERENCES `mydb`.`INVOICE` (`inv_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_LINE_PRODUCT1`
    FOREIGN KEY (`prod_id`)
    REFERENCES `mydb`.`PRODUCT` (`prod_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_LINE_DISCOUNT1`
    FOREIGN KEY (`disc_id`)
    REFERENCES `mydb`.`DISCOUNT` (`disc_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`IMAGES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`IMAGES` (
  `prod_id` INT UNSIGNED NOT NULL,
  `img_id` INT UNSIGNED NOT NULL,
  `img_filename` VARCHAR(128) NOT NULL,
  `img_desc` VARCHAR(256) NULL,
  PRIMARY KEY (`prod_id`, `img_id`),
  CONSTRAINT `fk_PRODUCTIMAGES_PRODUCT1`
    FOREIGN KEY (`prod_id`)
    REFERENCES `mydb`.`PRODUCT` (`prod_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
