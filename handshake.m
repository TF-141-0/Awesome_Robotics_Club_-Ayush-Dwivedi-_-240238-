disp('base position of Arm A');
xA = input('xA = ');
yA = input('yA = ');

disp('base position of Arm B');
xB = input('xB = ');
yB = input('yB = ');

disp('handshake point');
xH = input('xH = ');
yH = input('yH = ');

disp('link lengths');
L1 = input('L1 = ');
L2 = input('L2 = ');

DA = sqrt((xH - xA)^2 + (yH - yA)^2);
DB = sqrt((xH - xB)^2 + (yH - yB)^2);

minReach = abs(L1 - L2);
maxReach = L1 + L2;

if (DA >= minReach && DA <= maxReach) && (DB >= minReach && DB <= maxReach)
    disp('Handshake possible');
else
    disp('Handshake not possible');
end
