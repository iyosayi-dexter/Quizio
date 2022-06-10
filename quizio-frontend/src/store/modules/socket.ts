import {BACKEND_HOST} from '../../adapters/globals'

interface socket {
    connection:null|WebSocket
}

interface attachment{
    attachment_url:string,
    attachment_caption:string
}

interface socket_message {
    receiver:{
        username:string,
        id:number
    },
    text:string| null,
    attachments: attachment[]|null,
}

const get_websocket_url=(token:string):string=>{
    return `ws:${BACKEND_HOST}/ws/chat?token=${token}`
}

const socket = {
    namespaced:true,
    state(): socket{
        return {
            connection:null
        }
    },
    mutations:{
        connect:function(state:socket, payload:{token:string, callback:Function}){
            const {token , callback} = payload
            state.connection = new WebSocket(get_websocket_url(token))
            state.connection.onmessage = function(e){
                callback(e.data)
            }
        },
        send:function(state:socket, payload:socket_message){
            state.connection?.send(JSON.stringify(payload))
        },
        disconnect:function(state:socket){
            if(state.connection === null){
                return
            }
            state.connection.close(0)
        }
    }
}

export default socket