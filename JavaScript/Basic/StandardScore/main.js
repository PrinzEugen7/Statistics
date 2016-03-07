function calc_median(data) 
{
    var half = (data.length/2)|0;
    var temp = data.sort(fn);

    if (temp.length%2) {
        return temp[half];
    }

    return (temp[half-1] + temp[half])/2;
}
