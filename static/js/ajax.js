function like(slug, id){
    var element = document.getElementById('like')
    var count = document.getElementById('count')
    $.get(`/like/${slug}/${id}`).then(response =>{
        if(response['response'] === 'liked'){
            element.className = 'fa fa_heart'
            count.innerText = Number(count.innerText) + 1

        }else{
            element.className = 'fa fa_heart-o'
            count.innerText = Number(count.innerText) - 1
        }
    })
}
