INSERT INTO `myapp_class` VALUES ('1', 'xiaoban', 'one');
INSERT INTO `myapp_class` VALUES ('2', 'zhongban', 'two');
INSERT INTO `myapp_class` VALUES ('3', 'daban', 'three');
INSERT INTO `myapp_class` VALUES ('4', 'yinianji', 'four');
INSERT INTO `myapp_class` VALUES ('5', 'ernianji', 'five');

INSERT INTO `myapp_teacher` VALUES ('1', 'yuwenlaoshi');
INSERT INTO `myapp_teacher` VALUES ('2', 'shuxuelaoshi');
INSERT INTO `myapp_teacher` VALUES ('3', 'yingyulaoshi');


INSERT INTO `myapp_teacher_myClass` VALUES ('1', '1', '1');
INSERT INTO `myapp_teacher_myClass` VALUES ('2', '1', '2');
INSERT INTO `myapp_teacher_myClass` VALUES ('3', '1', '3');
INSERT INTO `myapp_teacher_myClass` VALUES ('4', '1', '4');
INSERT INTO `myapp_teacher_myClass` VALUES ('5', '1', '5');
INSERT INTO `myapp_teacher_myClass` VALUES ('6', '2', '1');
INSERT INTO `myapp_teacher_myClass` VALUES ('7', '2', '2');
INSERT INTO `myapp_teacher_myClass` VALUES ('8', '2', '3');
INSERT INTO `myapp_teacher_myClass` VALUES ('9', '3', '3');


INSERT INTO `myapp_studentdetail` VALUES ('1', 171, 65, 'http://blog.lyz.com');
INSERT INTO `myapp_studentdetail` VALUES ('2', 168, 51, 'http://blog.xyl.com');
INSERT INTO `myapp_studentdetail` VALUES ('3', 176, 60, 'http://blog.hq.com');
INSERT INTO `myapp_studentdetail` VALUES ('4', 178, 85, 'http://blog.wzg.com');
INSERT INTO `myapp_studentdetail` VALUES ('5', 178, 86, 'http://blog.fb.com');
INSERT INTO `myapp_studentdetail` VALUES ('6', 180, 90, 'http://blog.zxl.com');
INSERT INTO `myapp_studentdetail` VALUES ('7', 165, 75, 'http://blog.ghj.com');


INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('1', 'lyz', '1', '1');
INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('2', 'xyl', '2', '1');
INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('3', 'hq', '3', '2');
INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('4', 'wzg', '4', '2');
INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('5', 'fb', '5', '2');
INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('6', 'zxl', '6', '3');
INSERT INTO `myapp_student`(id,name,detail_id,myClass_id) VALUES ('7', 'ghj', '7', '3');