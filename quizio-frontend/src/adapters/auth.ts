import { REST_API_URL , decode_jwt} from "./globals"



export const loginRequest = async (credentails: {email:String , password:String})=>{
    const body = JSON.stringify(credentails)
    const config = {
        method:'POST',
        headers:{
            'Content-type':'application/json'
        },
        body
    }

    try{
        const res = await fetch(`${REST_API_URL}/auth/token/`, config)
        if (res.status===200){
            const tokens = await res.json()
            const user = decode_jwt(tokens.access)
            return {
                tokens,
                user
            }
        }
        return {}
    }catch(err){
        return {}
    }
}

interface signupInterface {
    username:string,
    password:string,
    re_password:string,
    email:string
}

export const signupRequest= async (data:signupInterface)=>{
    const body = JSON.stringify(data)
    const config = {
        method:'POST',
        headers:{
            'Content-type':'application/json'
        },
        body
    }

    try{
        const res = await fetch(`${REST_API_URL}/api/auth/signup/`,config)
        if(res.status === 201){
            return true
        }
        return false
    }catch(err){
        return false
    }

}
const storeRefresh=(token:string)=>{

}