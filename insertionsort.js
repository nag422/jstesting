function insertionSort(arr){
    for(let i = 1; i < arr.length; i++){
        let numberToInsert = arr[i]
        console.log("numbertoinsert: ", numberToInsert)
        let j = i - 1;
        console.log("j: ",j)
        while(j >= 0 && arr[j] > numberToInsert) { 
            arr[j+1] = arr[j]
            console.log(`while arr[j+1]: ${arr[j+1]} and arr[j]: ${arr[j]} numbertoInsert: ${numberToInsert}`)
            j = j-1
            console.log('while j value: ',j)
        }
        arr[j+1] = numberToInsert
        console.log("final number toinsert: ", numberToInsert);
        console.log( "final arr[j+1]: ", arr[j+1]);
    }
}

const arr = [8, 20, -2, 4, -6, 12, 46, 84]
insertionSort(arr)
console.log(arr)