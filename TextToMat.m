
% File is created by Mr. Ishan Jindal..
% copyright by the Author..
% you can use thic code for personnel research use, no commercial use is 
% allowable.

clc;clear all;close all

fileID = fopen('/Users/ishanjindal/Downloads/aaaa.txt','r');
Intro = textscan(fileID,'%s',2,'Delimiter','\n');
disp(Intro{1});
InputText = textscan(fileID,'lambda(microns)(%d,1)');
NumCols = InputText{1};
Lambda = textscan(fileID,'%f','delimiter',',');
Lambda_val = ceil(1000*Lambda{1});
clear Lambda
InputText = textscan(fileID,'ratio factor(1,%d)');
NumCols = InputText{1};
Ratio = textscan(fileID,'%f','delimiter',',');
Ratio_val = Ratio{1};
for i =1:1:numel(Ratio_val)
    if Ratio_val > 1
        Ratio_val(i) = 1;
    end
end
clear Ratio
InputText = textscan(fileID,'ratio shape:transmission: Re(T) vs position(%d,%d)');
NumCols = InputText{1};
NumRows = InputText{2};
Final = textscan(fileID,'%f','delimiter',',');
Final_val = reshape(Final{1},[NumRows,NumCols])';
clear Final
for i=1:1:20
    hold on
    Val = i-Ratio_val(i) + Final_val(:,i);
    plot(Lambda_val,Val)
end



Input = [Lambda_val, Final_val];
save input_mat.mat Input




