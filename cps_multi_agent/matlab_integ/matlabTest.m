function [] = matlabTest(inArr)

%temp1=size(inArr)
inArr
celldisp(inArr)

%outArr = matConverter(inArr, 'labels')
%display('start')
%outArr.R00E01TR
%size(outArr)
%display('start')
%outArr.R00E00TR

%temp=load('policy.mat');
%temp1=temp.policy;

%outVal = cellfun(@size,inArr,'UniformOutput',false)
%outClass = cellfun(@class,inArr,'UniformOutput',false)
%singleVal = [size(inArr{1}{1}),size(inArr{1}{2}),size(inArr{1}{3})]
%singleClass = [class(inArr{1}{1}),class(inArr{1}{2}),class(inArr{1}{3})]

end

function outMat = matConverter(inMat, matType)

switch matType
    case 'alph'
        numElements = length(inMat);
        outMat = char(zeros(numElements,2));
        for i=1:numElements
            outMat(i,:)=inMat{i};
        end
    case 'states'
        numElements = length(inMat);
        outMat = char(zeros(numElements,8));
        for i=1:numElements
            outMat(i,:)=inMat{i};
        end
    case 'trans'
        numElements = length(inMat);
        outMat = char(zeros(numElements,3,8));
        for i=1:numElements
            outMat(i,1,:)=inMat{i}{1};
            outMat(i,2,:)=inMat{i}{2};
            outMat(i,3,1:2)=inMat{i}{3};
            outMat(i,3,3:end)=' ';
        end
    case 'labels'
        stateList = cell(length(inMat),1);
        for i=1:length(inMat)
            stateList{i} = inMat{i}{1};
        end
        stateList = unique(stateList);
        
        numStates = length(stateList);
        numLabels = round(length(inMat)/numStates);
        if numStates*numLabels ~= length(inMat)
            error('Mismatch in label numbers\n');
        end
                
        for i=1:numStates
            stateName = inMat{(i-1)*4+1}{1};
            for j=1:numLabels
                labelName = inMat{(i-1)*4+j}{2};
                labelValue = inMat{(i-1)*4+j}{3};
                outMat.(stateName).(labelName)=labelValue;
            end
        end
end
end
