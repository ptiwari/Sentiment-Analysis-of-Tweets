
%addpath('/Users/parastiwari/libsvm-3.17/matlab') % assume your libsvm is installed in 'libsvm/matlab'
% [heart_scale_label, heart_scale_inst] = libsvmread('/Users/parastiwari/libsvm-3.17/heart_scale');
% model = svmtrain(heart_scale_label, heart_scale_inst, '-c 1 -g 0.07');
% [predict_label, accuracy, dec_values] = svmpredict(heart_scale_label, heart_scale_inst, model); % test the training data

% c is the trade-off parameter
c=1;
load '/Users/parastiwari/cse514/project/mycode/train.txt';
xTr = spconvert(train);
yTr = dlmread('/Users/parastiwari/cse514/project/mycode/train_labels.txt');
model = svmtrain(yTr, xTr', '-s 0 -t 0 -c 30');

load '/Users/parastiwari/cse514/project/mycode/test.txt';
xTe = spconvert(test);
yTe = zeros(size(xTe,2),1);
yTe = dlmread('/Users/parastiwari/cse514/project/mycode/test_labels.txt');
preds = svmpredict(yTe, xTe', model); % make predictions
max(preds)
min(preds)



