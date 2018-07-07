//https://www.apronus.com/music/flashpiano.htm

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

d=[15, 18, 15, 15, 18, 15, 12, 5, 3, 2, 11, 7, 12, 5, 3, 12, 5, 3, 15, 18, 15, 2, 11, 7, 15, 18, 15, 15, 18, 15, 12, 5, 3, 2, 11, 7, 12, 5, 3, 12, 5, 3, 15, 18, 15, 2, 11, 7, 15, 18, 15, 15, 18, 15, 12, 5, 3, 2, 11, 7];

for(i=0; i<d.length; i+=1){
    presspianokey(Math.round(50+d[i]*30/19));
	await sleep(300);
}
