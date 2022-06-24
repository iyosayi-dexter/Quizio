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
            cacheInSession('courses',data)
            return data
        }
        return []
    }catch(err){
        return []
    }
}

export const fetchLessons=async()=>{
    const lessons = sessionStorage.getItem('lessons')

    if(lessons !== undefined && lessons !== null){
        const lessons_arr = JSON.parse(lessons!)
        if(lessons_arr.length> 0){
            return lessons_arr
        }
    }

    const config = {
        method:'GET',
    }
    try{
        const res = await fetch(`${REST_API_URL}/lessons/`, config)
        if(res.status === 200){
            const data = await res.json()
            cacheInSession('lessons', data)
            return data
        }
        return []
    }catch(err){
        return []
    }
}


export const fetchLessonDetail= async (slug:string) =>{
    const config = {
        method:'GET',
    }
    try{
        const res = await fetch(`${REST_API_URL}/lessons/${slug}/`, config)
        if(res.status === 200){
            const data = await res.json()
            return {
                is404:false,
                data:data
            }
        }
        return {
            is404:true,
            data:null
        }
    }catch(err){
        return {
            is404:true,
            data:null
        }
    }
}

const cacheInSession=(key:string , data:{title:string, id:number, thumbnail:string }[])=>{
    sessionStorage.setItem(key, JSON.stringify(data))
}