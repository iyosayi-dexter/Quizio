import {setSeen} from '../../adapters/chat'

interface user{
    username:String,
    profileImageUrl?:String,
    id:number
}
interface attachment {
    attachment_url:String ,
    caption:String[] | null
}
export interface message {
    sender:user,
    receiver:user,
    attachments:attachment[] | null,
    text: String | null,
    seen: boolean,
    date_sent: String,
    id:number
}

interface chatInterface{
    messages: message[],
    currentChatUserId:number|null,
    currentChatUserUsername:String | null,
    search:String
}

const new_message:message[]= [

]

const chat={
    namespaced:true,
    state():chatInterface{
        return {
            messages:[...new_message],
            currentChatUserId:null,
            currentChatUserUsername:null,
            search:''
        }
    },
    mutations:{
        setCurrentChatUserId(state:chatInterface, payload:{id:number , username:String}){
            const {id , username} = payload
            state.currentChatUserId = id
            state.currentChatUserUsername = username
        },

        appendMessage(state:chatInterface , new_message:message){
            console.log(new_message)
            state.messages = [new_message, ...state.messages]
        },

        markAsRead(state:chatInterface, payload:{user:user, token:String}){
            const {user , token} = payload
            state.messages = state.messages.map( message => {
                if(message.sender.id === user.id || message.receiver.id === user.id){
                    if(message.seen === false){
                        setSeen(message.id, token)
                    }
                    return {...message , seen:true}
                }
                return message
            })
        },

        updateMessages(state:chatInterface , messages:message[]){
            state.messages = messages
        }
    }
}

export default chat