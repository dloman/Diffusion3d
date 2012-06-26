x = rand(1,24);
y = rand(1,24);
z = rand(1,24);
sz = 40;
colors = jet(12);
scatter3(x, y, z, sz, colors, 'filled')
colorbar('YTick', linspace(0, 1, 12), 'YTickLabel', 1:12)
