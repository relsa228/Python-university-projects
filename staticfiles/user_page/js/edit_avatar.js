const new_avatar = document.getElementById("avatar_edit")
const avatar = document.getElementById("avatar")
const aprove_btn = document.getElementById("aprove_btn")
new_avatar.addEventListener("change", ev => {
    const formatdata = new FormData()
    formatdata.append("image", ev.target.files[0])
    fetch("https://api.imgur.com/3/image/", {
        method: "post",
        headers: {
            Authorization: "Client-ID 47489ea753a5295"
        },
        body: formatdata
    }).then(data=>data.json()).then(data=>{
        avatar.src = data.data.link
        aprove_btn.value = data.data.link
    })
})