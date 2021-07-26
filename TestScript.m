clc;clear;

%Simulated data parameters.
start=20;
step_depth=0.5;
upper_depth=100;
upper_bound_x=2;
lower_bound_x=0;
upper_bound_y=4;
lower_bound_y=0;
upper_noise_x=4;
upper_noise_y=10;
actual_points=10;
noisy_points=50;
intensity_actual=600;
intensity_noise=100;

%Number of simulations
steps=10;

%Algorithm specifications
k=8;
thres=0.3;

%color specifications
color=[1 0 0];

% writerObj = VideoWriter('original_data','MPEG-4'); % Name it.
% writerObjFilter = VideoWriter('filtered_data','MPEG-4'); % Name it.
% writerObjFilter.FrameRate=10;
% writerObj.FrameRate = 10; % How many frames per second.
% open(writerObj);
% open(writerObjFilter);

for i=1:steps 
[Cloud,Intensity]= SimulatedData(upper_bound_x,lower_bound_x,upper_bound_y,lower_bound_y,upper_noise_x,upper_noise_y,upper_depth,actual_points,noisy_points,start,intensity_actual,intensity_noise);
% [Cloud,Intensity]=discard(Cloud,k,thres,Intensity);
 fraction=Intensity./max(Intensity);
 figure(i)
 scatter3(Cloud(1,:),Cloud(3,:),Cloud(2,:),[],color.*fraction,'filled');hold on;
axis([-4 4 0 100 -10 10])
view(5,5)
% frame = getframe(gcf); 
% % writeVideo(writerObj, frame);   
% close 
% 
% 
% [Cloud_1,Intensity_1]=discard(Cloud,k,thres,Intensity);
% fraction=Intensity_1./max(Intensity_1);
% %[Cloud_1,Intensity_1]=sliceDiscard(Cloud,Intensity,k,thres,5);
% [Cloud_2,Intensity_2]=sliceDiscardOverlap(Cloud,Intensity,k,thres,5);
% 
% scatter3(Cloud_1(1,:),Cloud_1(3,:),Cloud_1(2,:),[],color.*fraction,'filled');hold on;
% axis([-4 4 0 100 -10 10])
% view(5,5)
% % frame = getframe(gcf); 
% % writeVideo(writerObjFilter, frame);   
% close 
save(['SumalateCloud_' num2str(i) '.mat'],'Cloud','Intensity')
start=start+step_depth;
end
% close(writerObj);
% close(writerObjFilter);

