x = rand(1,24);
y = rand(1,24);
z = rand(1,24);
sz = 40;
%colors = jet(24);
%a=abs(rand(24,3));

scatter3(x, y, z, sz,'r', 'filled')
scatter3(x, y, z, sz,a, 'filled')
%colorbar('YTick', linspace(0, 1, 24), 'YTickLabel', 1:12)
