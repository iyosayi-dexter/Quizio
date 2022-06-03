interface user{
    username:String,
    profileImageUrl:String,
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
    date: String,
}

interface chatInterface{
    messages: message[],
    currentChatUserId:number|null,
    currentChatUserUsername:String | null,
    search:String
}

const new_message:message[]= [
    {
        sender:{
            username:'gwen',
            profileImageUrl:'some url',
            id:2
        },
        receiver:{
            username:'dexter',
            profileImageUrl:'test url',
            id:5
        },
        attachments:null,
        text: 'hello there',
        seen: false,
        date: 'may 2 2020, 11:28pm',
    },
    {
        sender:{
            username:'barry',
            profileImageUrl:'some url',
            id:10
        },
        receiver:{
            username:'dexter',
            profileImageUrl:'some url',
            id:5
        },
        attachments:null,
        text: 'Whats up',
        seen: false,
        date: 'May 2 2020, 11:28pm',
    },
    {
        sender:{
            username:'dexter',
            profileImageUrl:'some url',
            id:5
        },
        receiver:{
            username:'dexter',
            profileImageUrl:'some url',
            id:5
        },
        attachments:null,
        text: 'Whats up',
        seen: false,
        date: 'May 2 2020, 11:28pm',
    },
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
        sendMessage(state:chatInterface , new_message:message){
            state.messages = [new_message, ...state.messages]
        },
        markAsRead(state:chatInterface, user:user){
            state.messages = state.messages.map( message => {
                if(message.sender.id === user.id || message.receiver.id === user.id){
                    return {...message , seen:true}
                }
                return message
            })
        }
    }
}

export default chat