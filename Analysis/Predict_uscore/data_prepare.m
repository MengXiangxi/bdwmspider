clc;
clear;
train = readtable('uscore_train.csv');
test = readtable('uscore_test.csv');
uscore = readtable('uscore_all.csv');
uscore_x = ([uscore.login, uscore.post, uscore.life, ...
    uscore.ycf, uscore.isBM, uscore.isManager]);
uscore_y = (uscore.uscore);
train_x = ([train.login, train.post, train.life, ...
    train.ycf, train.isBM, train.isManager]);
train_y = (train.uscore);
test_x = ([test.login, test.post, test.life, ...
    test.ycf, test.isBM, test.isManager]);
test_y = (test.uscore);
nnstart