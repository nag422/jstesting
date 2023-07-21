function mergeSort(arr){
    if (arr.length <= 1){
        return arr
    }
     const mid = Math.floor(arr.length / 2);
     const leftArr = arr.slice(0,mid);
     const rightArr = arr.slice(mid);
    return merge(mergeSort(leftArr),mergeSort(rightArr));
}

function merge(leftArr, rightArr){
    const sorted_list = []
    while(leftArr.length && rightArr.length){
        if(leftArr[0] <= rightArr[0]){
            const rightshiftedarr = leftArr.shift();
            if(!(sorted_list.includes(rightshiftedarr))){
                sorted_list.push(rightshiftedarr)
            }
            
        } else {
            const shiftedarry = rightArr.shift();
            if(!(sorted_list.includes(shiftedarry))){
                sorted_list.push(shiftedarry)
            }
        }
    }
    return [...sorted_list, ...leftArr, ...rightArr]
}
let arr = [5, 8, 12, 56, 8, 20, -2, 4, -6, 3535, 3454, 8, 20, -2, 4, -6, 3535, 3454]
console.log(mergeSort(arr));
