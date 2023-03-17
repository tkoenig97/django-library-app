const alterBookQuantity = (id, quantity, m) => {
    if (m === "A"){
        quantity++
    }
    else{
        quantity--
    }

    axios.put(`/book/${id}/`, {
        quantity : quantity
    })
    .catch((err)=>{
        alert(err)
    })
    .then((response) => {
        if(response.data.success){
            window.location.reload()
        }
    })
}

const deleteABook = (id) =>{
    axios.delete(`/book/${id}/`)
    .catch((err) => {
        alert(err)
    })
    .then((response)=>{
        if(response.data.success){
            window.location.reload()
        }
    })
}