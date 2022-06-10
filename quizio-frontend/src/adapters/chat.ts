import {REST_API_URL} from './globals'

export const loadMessages =async  (token:String)=>{
    const Authorization = `Bearer ${token}`
    const config = {
        method:"GET",
        headers : {
            Authorization
        }
    }

    try{
        const res = await fetch(`${REST_API_URL}/chat/retrieve-messages/`, config)
        if(res.status === 200){
            const data = await res.json()
            return data
        }
        return []
    }catch{
        return []
    }
}

export const setSeen= async (message_id:number,token:String)=>{
    const Authorization = `Bearer ${token}`
    const body = JSON.stringify({message_id})
    const config = {
        method:"POST",
        headers: {
            'Content-type':'application/json',
            Authorization
        },
        body
    }
    try{
        await fetch(`${REST_API_URL}/chat/set-seen/`, config)
    }catch{
    }
}