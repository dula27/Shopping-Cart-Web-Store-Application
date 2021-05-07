CREATE TABLE people (
  fname     varchar(250) not null,
  loginId   varchar(250) not null,
  email     varchar(250) not null,
  pass      varchar(250) not null,
  primary key (loginId)
);

CREATE TABLE category (
  cname     varchar(25) not null,
  cid       int(1),
  primary key (cid),
  unique (cname)
);

CREATE TABLE product (
  pid       int(3),
  pname     varchar(250) not null,
  quantity  int(4),
  price     float(5),
  cid       int(1),
  primary key (pid),
  unique (pname),
  foreign key (cid) references category(cid)
);

CREATE TABLE orders (
  orderDate date,
  orderID   varchar(15),
  loginId   varchar(250) not null,
  total     float(6),
  primary key   (orderID),
  foreign key (loginId) references people(loginId)
);

CREATE TABLE orderItems (
  orderItem int(3),
  orderID   varchar(15),
  pid       int(3),
  qty       int(3),
  sumPrice  float(6),
  primary key   (orderItem),
  foreign key (pid) references product(pid),
  foreign key (orderID) references orders(orderID)
);

INSERT INTO category VALUES ('Fragnance','1');
INSERT INTO category VALUES ('Make up','2');
INSERT INTO category VALUES ('Hair','3');
INSERT INTO category VALUES ('Face','4');
INSERT INTO category VALUES ('Body','5');
INSERT INTO category VALUES ('Bath','6');

INSERT INTO product VALUES (001, 'Versace Eros', 34, 59.99, 1);
INSERT INTO product VALUES (002, 'Versace Dylan Blue', 22, 62.99, 1);
INSERT INTO product VALUES (003, 'Versace Eros Flame', 16, 75.99, 1);
INSERT INTO product VALUES (004, 'Versace Pour Homme', 54, 49.99, 1);
INSERT INTO product VALUES (005, 'Versace Yello Diamond', 29, 69.99, 1);
INSERT INTO product VALUES (006, 'Versace Crystal Noir', 17, 70.99, 1);
INSERT INTO product VALUES (007, 'Bleu De Chanel', 16, 98.00, 1);
INSERT INTO product VALUES (008, 'Allure Home Chanel', 12, 125.00, 1);
INSERT INTO product VALUES (009, 'Le Lion De Chanel', 8, 200.00, 1);

INSERT INTO product VALUES (010, 'Weightless Foundation SPF-15', 43, 49.00, 2);
INSERT INTO product VALUES (011, 'Highlighting Powder Pink', 21, 48.00, 2);
INSERT INTO product VALUES (012, 'Highlighting Powder Golden', 18, 48.00, 2);
INSERT INTO product VALUES (013, 'Shadow Stick Bronze', 24, 30.00, 2);
INSERT INTO product VALUES (014, 'Crushed Lip Color', 14, 29.00, 2);
INSERT INTO product VALUES (015, 'Crushed Lip Liquid', 19, 29.00, 2);
INSERT INTO product VALUES (016, 'Smokey Eye Mascara', 43, 32.00, 2);
INSERT INTO product VALUES (017, 'Skin Foundation Stick', 15, 18.00, 2);
INSERT INTO product VALUES (018, 'Bronzing Powder', 25, 44.00, 2);
INSERT INTO product VALUES (019, 'Full Cover Concealer', 30, 52.00, 2);

INSERT INTO product VALUES (020, 'Hair Wax', 12, 15.00, 3);
INSERT INTO product VALUES (021, 'Hair Settling Spray', 18, 9.99, 3);
INSERT INTO product VALUES (022, 'Hair Gel', 43, 4.99, 3);
INSERT INTO product VALUES (023, 'Pomade', 18, 8.00, 3);
INSERT INTO product VALUES (024, 'Dry Shampoo', 17, 18.00, 3);
INSERT INTO product VALUES (025, 'Hair Color Brown', 86, 7.88, 3);
INSERT INTO product VALUES (026, 'Frizzy Shampoo', 54, 12.99, 3);
INSERT INTO product VALUES (027, 'After Shave', 46, 11.00, 3);
INSERT INTO product VALUES (028, 'Castor Hair Oil', 28, 8.47, 3);
INSERT INTO product VALUES (029, 'Trimmer', 9, 33.53, 3);

INSERT INTO product VALUES (030, 'Essence-Lotion', 12, 12.00, 4);
INSERT INTO product VALUES (031, 'Sunblock SPF-30', 19, 18.00, 4);
INSERT INTO product VALUES (032, 'Mango Lip Butter', 22, 4.00, 4);
INSERT INTO product VALUES (033, 'Strawberry Lip Butter', 21, 4.00, 4);
INSERT INTO product VALUES (034, 'Orange Face Mask', 18, 6.50, 4);
INSERT INTO product VALUES (035, 'Charcoal Face Mask', 26, 6.50, 4);
INSERT INTO product VALUES (036, '100% Natural Shea Butter', 33, 15.00, 4);
INSERT INTO product VALUES (037, 'Coffee Energising Cleanser', 17, 21.99, 4);
INSERT INTO product VALUES (038, 'Face Moisturizer', 33, 34.00, 4);
INSERT INTO product VALUES (039, 'Skin Exfoliator', 29, 9.00, 4);

INSERT INTO product VALUES (040, 'Face Oil', 10, 11.00, 5);
INSERT INTO product VALUES (041, 'Zesty Lemon Scrub', 23, 18.00, 5);
INSERT INTO product VALUES (042, 'Cool Cucumber Routine', 15, 15.00, 5);
INSERT INTO product VALUES (043, 'Blueberry Body Exfoliate', 14, 23.00, 5);
INSERT INTO product VALUES (044, 'Body Scrub Lemon', 19, 16.50, 5);
INSERT INTO product VALUES (045, 'Body Scrub Orange', 36, 16.50, 5);
INSERT INTO product VALUES (046, 'Dry Grape Seed Exfoliate', 6, 13.50, 5);
INSERT INTO product VALUES (047, 'Glowing British Rose Care Bag', 7, 10.99, 5);
INSERT INTO product VALUES (048, 'Sweetening Mango Little Pack', 12, 41.00, 5);
INSERT INTO product VALUES (049, 'Coconut Body Lotion', 15, 7.00, 5);

INSERT INTO product VALUES (050, 'Shower Bath Sponge', 13, 11.99, 6);
INSERT INTO product VALUES (051, 'Back Scrubber', 25, 12.99, 6);
INSERT INTO product VALUES (052, 'Organic Oil', 26, 13.99, 6);
INSERT INTO product VALUES (053, 'Soaking Salt', 38, 15.99, 6);
INSERT INTO product VALUES (054, 'Rabbit Bath Bomb', 29, 14.99, 6);
INSERT INTO product VALUES (055, 'Satin Black Bath Bomb', 17, 18.99, 6);
INSERT INTO product VALUES (056, 'Butter Ball Bath Soother', 14, 17.99, 6);
INSERT INTO product VALUES (057, 'Freaky Peach Bath Bomb', 7, 16.99, 6);
INSERT INTO product VALUES (058, 'Nivea Shower Gel', 11, 12.99, 6);
INSERT INTO product VALUES (059, 'Body Conditioner', 20, 19.99, 6);

