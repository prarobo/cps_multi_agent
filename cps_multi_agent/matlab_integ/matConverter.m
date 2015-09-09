function outMat = matConverter(inMat, matType, numAgents)
% Function to transform the input matrices from python into the required format

machineIDLen = numAgents*6+4
switch matType
    case 'alph'
        numElements = length(inMat);
        outMat = char(zeros(numElements,3));
        for i=1:numElements
            outMat(i,:)=inMat{i};
        end
    case 'states'
        numElements = length(inMat);
        outMat = char(zeros(numElements,machineIDLen));
        for i=1:numElements
            outMat(i,:)=inMat{i};
        end
    case 'trans'
        numElements = length(inMat);
        outMat = char(zeros(numElements,3,machineIDLen));
        for i=1:numElements
            outMat(i,1,:)=inMat{i}{1};
            outMat(i,2,:)=inMat{i}{2};
            outMat(i,3,1:3)=inMat{i}{3};
            outMat(i,3,4:end)=' ';
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


