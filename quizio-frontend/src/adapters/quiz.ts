import {REST_API_URL} from './globals'

export const fetchQuestions=async (test_config : {course:string, dur:string, nques:string, mode:string})=>{

    const {course , nques , mode} = test_config

    const body = JSON.stringify({course , nques , mode: mode.toUpperCase()})
    const config = {
        method:'POST',
        headers: {
            'Content-type':'application/json'
        },
        body
    }

    try{
        const res = await fetch(`${REST_API_URL}/quiz/questions/`, config)
        if(res.status === 200){
            const data = await res.json()
            return data
        }
        return []
    }catch(err){
        return []
    }
}

export const submitTest= async(users_answers:{id:number, choice:string}[], course:string, mode:string)=>{
    const body = JSON.stringify({users_answers, course, mode})
    const config = {
        method:'POST',
        headers:{
            'Content-type':'application/json'
        },
        body
    }

    try {
        const res = await fetch(`${REST_API_URL}/quiz/submit/`, config)
        if(res.status===200){
            const data = await res.json()
            return data
        }

    }catch(err){

    }
}


export const sendChallange = async(course:{title:string , id:number}, challanger:{username:string, id:string}, token:string)=>{
    const body = JSON.stringify({course, challanger})
    const Authorization = `Bearer ${token}`
    const config = {
        method:'POST',
        headers:{
            'Content-type':'application/json',
            Authorization
        },
        body
    }
    try{
        const res = await fetch(`${REST_API_URL}/quiz/challange/` , config)
        if(res.status === 200 ){
            const data = await res.json()
            return data
        }
        return null
    }
    catch(err){
        return null
    }
}