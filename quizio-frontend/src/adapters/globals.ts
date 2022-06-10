import jwt_decode from 'jwt-decode'
export const REST_API_URL= 'http://localhost:8000/api'

export const decode_jwt=(token:string)=> jwt_decode(token)

export const BACKEND_HOST='127.0.0.1:8000'