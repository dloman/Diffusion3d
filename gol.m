x=[transpose(1:10)];
for i=1:2:10
y=[i*ones(1,10)];
for j=1:2:10
z=[j*ones(1,10)];

sz = 40;
%colors = jet(24);
a=abs(rand(10,3));

%scatter3(x, y, z, sz,'r', 'filled')
hs=scatter3(x, y, z, sz,a, 'filled')
hold on
%colorbar('YTick', linspace(0, 1, 24), 'YTickLabel', 1:12)
end
end
alpha(hs,.5); 
