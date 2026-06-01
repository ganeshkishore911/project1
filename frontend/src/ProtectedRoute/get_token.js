export const getToken =()=>{
    const cookies=document.cookie.split(";")

    const accessToken =cookies.find((cookies)=>
    cookie.trim().startsWith("access_token="))
    return accessToken ? accesssToken.split("=")[1]:null

}

