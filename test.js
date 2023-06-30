const skipper = [1,3,5,4,8,5,2];
// const newArry = [...new Set(skipper)]
let sorted_list = new Map();
sorted_list.set("exists",[]);
sorted_list.set("none",[])
const filterArry = skipper.filter((val) => {
    if(!sorted_list.get("exists").includes(val)){
        // sorted_list.exists.push(val) 
        sorted_list.set("exists",[...sorted_list.get("exists"), val])
    } else{
        // sorted_list.none.push(val)
        sorted_list.set("none",[...sorted_list.get("none"), val])
    }
});
// console.log(filterArry);
console.log(sorted_list.size)
// console.log(skipper)
// console.log(skipper.indexOf(1))
