import { REST_API_URL } from "./globals";



export const fetchCourses=async ()=>{
    const courses = sessionStorage.getItem('courses')

    if(courses !== undefined && courses !== null){
        const courses_arr = JSON.parse(courses!)
        if(courses_arr.length> 0){
            return courses_arr
        }
    }

    const config = {
        method:'GET',
    }
    try{
        const res = await fetch(`${REST_API_URL}/course/`, config)
        if(res.status === 200){
            const data = await res.json()
            cacheInSession(data)
            return data
        }
        return []
    }catch(err){
        return []
    }
}



const cacheInSession=(data:{title:string, id:number, thumbnail:string }[])=>{
    sessionStorage.setItem('courses', JSON.stringify(data))
}