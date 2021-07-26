%Flying pixels removal script. 

%Input
%dict: 3xN matrix ,   where N is the number of points living in the cloud. 
%k:integer point threshold. Minimum number of points living within the range of the radial threshold.
%thres: radial threshold. Radius of the ball (see documentation) drawn  around each point.
%intensity: N x 1 vector. Reflectivity of each point in the cloud. 

%Output
%dict: 3 x K matrix, post processed point cloud of K points living in 3 dimensions. 
%intensity: K x 1 vector. reflectivity of post processed point cloud.

%Author: Kostantinos Voulgaris
%date: 15/10/2020.

function [dict,intensity,indexes]=discard(dict,k,thres,intensity)


c=sum(dict.*dict);%c: 1xN vector. Stores the squarred magnitude of each point in the cloud.  
[~,columns]=size(dict);
s=zeros(columns,1);%s is a sparse Nx1 vector initialised with 0s. The non zero entries contain the index of the pixels which will be characterised as flying pixels after the termination of the loop.
for i=1:columns
    distance=(c(i)-2*(dict(:,i)'*dict)+c);    
    if sum(distance<thres)<k  %check how many points live within the radial threshold. If it is below  the integer point threshold k then it is characterised as a flying pixel and its index is stored in s. 
        s(i,1)=i;
    end
    
end
indexes=nonzeros(s);
dict(:,indexes)=[];%Discard from the cloud the points which are characterised as flying pixels. 
intensity(indexes)=[];
end