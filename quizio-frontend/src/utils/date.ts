export const getCurrentDateTime=():string=>{
    const months: String[] = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'Jun' , 'Jul' , 'Aug' , 'Sep' , 'Oct' , 'Nov' , 'Dec']
    const date = new Date()
    const month = date.getMonth()
    const day = date.getDate()
    const year = date.getFullYear()

    const time:String = (()=>{
        if(date.getHours() > 12){
            return `${date.getHours()-12}:${date.getMinutes()}pm`
        }else if(date.getHours() === 12){
            return  `${date.getHours()}:${date.getMinutes()}pm`
        }
        return `${date.getHours()}:${date.getMinutes()}am`
    })()

    return `${months[month]} ${day} ${year}, ${time}`
}