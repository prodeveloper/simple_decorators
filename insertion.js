var arr = [5,4,2,6,1]
let array_len = arr.length 

for (j= 2; j<array_len; j++){
    let key = arr[j]
    let i = j-1
    while (i>0 && arr[i]> key){
        arr[i+1]=arr[i]
        i = i-1
    }
    arr[i+1] = key
    console.log(arr)
}
console.log("final answer", arr)